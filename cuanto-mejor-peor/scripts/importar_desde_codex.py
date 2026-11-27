#!/usr/bin/env python3
"""Inventaria y copia archivos del proyecto Codex local al clon de vsalesa/books.

POR DEFECTO SOLO HACE SIMULACION. La opción --apply copia sin borrar ni sobrescribir
archivos distintos. No hace commits ni push: el autor debe revisar antes de publicar,
porque el repositorio de destino es publico.

Uso:
  python scripts/importar_desde_codex.py "C:/.../outputs" --repo "C:/.../books"
  python scripts/importar_desde_codex.py "C:/.../outputs" --repo "C:/.../books" --apply
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ALLOWED = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".pdf", ".docx", ".md", ".txt", ".json", ".zip"}
DENY_PARTS = {".git", ".venv", "venv", "node_modules", "__pycache__", "secrets", ".ssh"}
DENY_NAMES = {".env", ".env.local", "credentials.json", "id_rsa", "id_ed25519"}
MAX_BYTES = 110 * 1024 * 1024


def digest(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            sha.update(chunk)
    return sha.hexdigest()


def group(path: Path) -> str:
    name = "/".join(path.parts).casefold()
    extension = path.suffix.casefold()
    if extension in {".pdf", ".docx"}:
        return "ediciones/material_recuperado"
    if extension == ".zip":
        return "materiales/paquetes"
    if extension in {".md", ".txt", ".json"}:
        return "materiales/fuentes_locales"
    if "personaje" in name or "retrato" in name or "galeria" in name:
        return "ilustraciones/personajes"
    if "portada" in name or "cubierta" in name:
        return "ilustraciones/portada"
    if "matriz" in name or "competencia_integridad" in name:
        return "ilustraciones/matriz"
    if "apertura" in name or "capitulo" in name or "prólogo" in name or "epilogo" in name:
        return "ilustraciones/aperturas"
    return "ilustraciones/otras"


def safe_name(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name).strip(" .") or "sin_nombre"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", type=Path, help="Carpeta fuente exportada desde Codex")
    ap.add_argument("--repo", type=Path, required=True, help="Clon local de vsalesa/books")
    ap.add_argument("--apply", action="store_true", help="Copiar realmente los ficheros")
    args = ap.parse_args()

    source = args.source.expanduser().resolve()
    repo = args.repo.expanduser().resolve()
    dest_root = repo / "cuanto-mejor-peor"
    if not source.is_dir():
        ap.error(f"No existe la carpeta fuente: {source}")
    if not (repo / ".git").exists():
        ap.error(f"No es un clon Git: {repo}")
    if source == repo or repo in source.parents or source in repo.parents:
        ap.error("La fuente y el repositorio no pueden contenerse mutuamente")

    remote = subprocess.run(
        ["git", "-C", str(repo), "remote", "get-url", "origin"],
        capture_output=True, text=True, check=False,
    ).stdout.strip().lower()
    if "vsalesa/books" not in remote:
        ap.error(f"El origin no apunta a vsalesa/books: {remote!r}")

    seen = {}
    manifest = []
    skipped = []
    files = sorted(p for p in source.rglob("*") if p.is_file())
    for path in files:
        relative = path.relative_to(source)
        if any(part.lower() in DENY_PARTS for part in relative.parts):
            skipped.append({"name": path.name, "reason": "carpeta excluida"})
            continue
        if path.name.lower() in DENY_NAMES or path.suffix.lower() not in ALLOWED:
            skipped.append({"name": path.name, "reason": "tipo o nombre excluido"})
            continue
        size = path.stat().st_size
        if size > MAX_BYTES:
            skipped.append({"name": path.name, "reason": "mayor de 110 MiB"})
            continue

        sha = digest(path)
        # Repetidos identicos en la importacion no se copian varias veces.
        if sha in seen:
            skipped.append({"name": path.name, "reason": f"duplicado exacto de {seen[sha]}"})
            continue
        seen[sha] = path.name
        folder = group(relative)
        dst = dest_root / folder / safe_name(path.name)
        if dst.exists() and digest(dst) != sha:
            dst = dst.with_name(dst.stem + "__" + sha[:12] + dst.suffix)
        state = "existente-igual" if dst.exists() and digest(dst) == sha else "pendiente"
        if args.apply and state == "pendiente":
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dst)
            if digest(dst) != sha:
                raise RuntimeError(f"Falló la verificación SHA256: {dst}")
            state = "copiado"
        manifest.append({
            "source_name": str(relative).replace("\\", "/"),
            "repo_path": str(dst.relative_to(repo)).replace("\\", "/"),
            "sha256": sha,
            "bytes": size,
            "status": state,
        })

    result = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source_directory_name": source.name,
        "applied": bool(args.apply),
        "files": manifest,
        "skipped": skipped,
    }
    out = dest_root / "materiales" / "MANIFEST_IMPORTACION_LOCAL.json"
    if args.apply:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "mode": "COPY" if args.apply else "DRY-RUN",
        "accepted": len(manifest), "skipped": len(skipped),
        "new_or_pending": sum(x["status"] in {"pendiente", "copiado"} for x in manifest),
        "total_bytes": sum(x["bytes"] for x in manifest),
        "manifest_path": str(out) if args.apply else None,
    }, ensure_ascii=False, indent=2))
    if not args.apply:
        print("Sin cambios. Repite con --apply tras revisar que no hay archivos privados.")
    else:
        print("Copia completada y verificada. Revisa antes de git add/commit/push.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
