# Estado de producción — 27 noviembre 2026

## Confirmado

- [x] REV03 creada y aplicada con 25 operaciones documentadas: [manuscrito revisado](fuentes/MANUSCRITO_V4_06_1_REV03_CIERRES_APLICADOS.md). No se altera REV02.1.
- [x] PDF ilustrado local V4.06.1 REV03 de **134 páginas A5** generado a partir de PDF original y arte gráfico, sin desbordamientos de texto detectados. SHA-256 `d945fd4ea4c4bbec0b881d8be8daf5cedbfa7426303f4444788f74880a810641`.
- [x] Workflow [compilar-cuanto-mejor-peor-rev03.yml](https://github.com/vsalesa/books/actions/workflows/compilar-cuanto-mejor-peor-rev03.yml) creado para publicar **PDF de lectura** desde fuente revisada y miniaturas de Canva.

- [x] Repo `vsalesa/books` accesible y con permiso de escritura. Carpeta `cuanto-mejor-peor/` creada.
- [x] Última **versión Canva** verificada: `DAHauUTL81o`, V4.06.1 REV02.1, 139 páginas A5.
- [x] Respaldos textuales en GitHub: extracción del contenido de Canva REV02.1, extracción de lectura DOCX V4.06 y fuente Markdown V4.04 (**tres orígenes diferentes**).
- [x] Propuesta editorial **ANTES → DESPUÉS** de 12 cierres y ajustes de continuidad, con fragmentos literales y traslados entre capítulos: [ANEXO_CAMBIOS_LITERALES_CIERRES_REV02_1_2026-11-27.md](editorial/ANEXO_CAMBIOS_LITERALES_CIERRES_REV02_1_2026-11-27.md). **Solo propuesta; sin cambios a manuscrito/Canva/PDF**.
- [x] Registro maestro histórico de 42 personajes y documentación editorial/historial conservados.
- [x] Identificadas las seis ilustraciones nuevas y sus referencias Canva.
- [x] Ejemplares V4.06 PDF y Word originales localizados en los archivos de conversación; aún **no están subidos como binarios** a este repositorio.

## No confirmado / pendiente

- [x] **PDF binario de lectura REV03 confirmado en GitHub**: [descarga](ediciones/V4_06_1_REV03/Cuanto_mejor_peor_V4_06_1_REV03_LECTURA_GITHUB.pdf), 134 páginas A5, 5.735.198 bytes, SHA-256 `6991b224b39ef2771b6270f2d174f65d3df78d8c4ba2e327491e5df182b11b4c`. Workflow [ejecución #3](https://github.com/vsalesa/books/actions/runs/46047657471) correcta.
- [ ] **Subir PDF ilustrado local de alta resolución REV03** (44.008.375 bytes, hash distinto); el PDF de lectura alojado en GitHub utiliza miniaturas, no los originales de impresión.

- [ ] Comprobar si existe en una sesión Codex inaccesible una versión posterior a REV02.1; el informe aportado por el usuario del 12/11 describe también REV02.1, no otra versión.
- [ ] Recuperar los binarios originales **V4.06.1 REV02.1** del entorno local de Codex: PDF recompuesto, ZIP de materiales, seis PNG nuevos, manifest de imágenes, Word sincronizado si existe. La ruta `C:/Users/adria/Documents/Codex/2026-11-12/referenced-chatgpt-conversation-this-is-an/outputs/` solo es accesible en el equipo del autor, no desde este entorno.
- [ ] Subir a GitHub los archivos gráficos y binarios con su SHA-256, dimensiones, color y licencia; **no declarar respaldados enlaces Canva ni miniaturas extraídas como originales**.
- [ ] Verificar el paquete de 42 retratos **fisonómicamente distintos** contra el manuscrito y la galería Canva. Las capturas compartidas son evidencia visual; no garantizan disponer de PNG individuales de imprenta.
- [ ] Cotejar íntegramente el Word V4.06 con los 974 párrafos de REV02.1 y cerrar el problema de espacios en los extractores.
- [ ] Generar y renderizar Word V4.06.1 sincronizado; todavía no está verificado.
- [ ] Revisión editorial del manuscrito para continuidad, referencias de actualidad, viudas/huérfanas, erratas, cortes y composición.
- [ ] Revisión KDP/preimpresión (resolución, perfil de grises, imágenes, corte, sangrado, negros, tipografía).

## Regla de trabajo

- Archivo **vigente** y archivo **histórico** son conceptos distintos.
- No reconstruir una edición posterior a partir de un manuscrito más viejo sin etiquetarla.
- Todo enlace, PDF, DOCX y PNG nuevo debe registrarse en `materiales/INVENTARIO.md`, indicando procedencia y estado real de subida.
- Cada cambio editorial se escribe en un nuevo registro versionado con fecha, contenido y validación.
