# Plan de continuación — Cuanto mejor, peor

**Actualizado:** 27 de noviembre de 2026  
**Base de maquetación Canva:** **V4.06.1 REV02.1** — **139 páginas A5**, Canva `DAHauUTL81o` ([abrir edición](https://www.canva.com/design/DAHauUTL81o/edit)).  
**Autor:** Víctor Salesa Sanz.

## Revisión literaria posterior: REV03 (27-11-2026)

**Ya aplicada** y versionada: [manuscrito revisado](fuentes/MANUSCRITO_V4_06_1_REV03_CIERRES_APLICADOS.md) y [PDF REV03 de lectura en GitHub](ediciones/V4_06_1_REV03/Cuanto_mejor_peor_V4_06_1_REV03_LECTURA_GITHUB.pdf), **134 páginas A5**. El PDF de lectura se recompiló con 30 miniaturas (no maestros gráficos); el PDF local de alta resolución (44 MB) todavía no está respaldado en GitHub. No declarar REV03 certificada para KDP.

## Resumen ejecutivo

El libro tiene manuscrito satírico ampliado, 14 capítulos, prólogo y epílogo, galería de **42 personajes** y **16 aperturas ilustradas**. La composición REV02.1 corrigió problemas graves de letras acentuadas, ñ, palabras pegadas y párrafos cortados provocados por importaciones anteriores. Se repusieron banderolas, títulos y capitulares; se integraron seis escenas nuevas para las aperturas de capítulos 7, 9, 11, 12, 13 y 14. La última entrega del entorno Codex local (12-11-2026 17:20) que compartió el autor también describe la REV02.1, **no una versión posterior**.

**Todavía no es un libro certificado para imprenta.** Queda verificar la integridad textual frente al DOCX original, cerrar un Word editable de REV02.1, respaldar los PNG/PDF/DOCX originales como binarios en GitHub y completar revisión literaria y gráfica.

## Qué está realmente disponible EN GitHub

| Área | Ubicación | Calidad |
|---|---|---|
| Manuscrito recompuesto REV02 (texto de edición) | [fuentes/MANUSCRITO_RECUPERADO_V4_06_REV02.md](fuentes/MANUSCRITO_RECUPERADO_V4_06_REV02.md) | Copia textual de trabajo; cotejo integral pendiente |
| Extracción de lectura REV02.1 desde Canva | [fuentes/V4_06_1_REV02_1_Canva_extraccion_texto.txt](fuentes/V4_06_1_REV02_1_Canva_extraccion_texto.txt) | Captura total de lectura, pero puede juntar párrafos; no maquetación |
| Manuscrito V4.04 histórico | [fuentes/MANUSCRITO_V4_04_REVISION_LITERARIA_01.md](fuentes/MANUSCRITO_V4_04_REVISION_LITERARIA_01.md) | Edición antigua — NO vigente |
| Extracción DOCX V4.06 | [fuentes/V4_06_DOCX_original_extraccion_lectura.txt](fuentes/V4_06_DOCX_original_extraccion_lectura.txt) | No sustituye OOXML binario |
| Registro maestro 42 personajes | [personajes/REPARTO_MAESTRO_CERRADO_V1.md](personajes/REPARTO_MAESTRO_CERRADO_V1.md) | Fuente histórica de nombres; revalidar roles contra REV02.1 |
| Normas aprobadas | [editorial/GUIA_DE_ESTILO.md](editorial/GUIA_DE_ESTILO.md) | Criterios de edición y maquetación |
| Decisiones detalladas del chat | [editorial/HISTORIAL_DECISIONES_Y_ERRORES.md](editorial/HISTORIAL_DECISIONES_Y_ERRORES.md) | Conserva preferencias, errores y reglas |
| Historial | [versiones/README.md](versiones/README.md) | Identifica versiones Canva |
| Inventario de originales y nuevos PNG | [materiales/INVENTARIO.md](materiales/INVENTARIO.md) | Diferencia recursos realmente subidos y enlaces externos |
| Importación desde Codex local | [scripts/importar_desde_codex.py](scripts/importar_desde_codex.py) | Importador con SHA-256, dry-run y protección contra sobrescritura |

El PDF REV02.1 de **43.785.411 bytes** fue recuperado de la Biblioteca en noviembre de 2026, pero su **archivo binario todavía no se ha subido a GitHub**. Tampoco se han subido los originales PNG y ZIP. Los enlaces Canva **no son un respaldo binario**.

## Orden de trabajo y seguimiento en GitHub Issues

| Orden | Issue | Entregable / criterio |
|---:|---|---|
| **1** | [#1 — Respaldo binario de archivos y originales](https://github.com/vsalesa/books/issues/1) | PDF vigente, DOCX fuente, PNG de ilustraciones/portada/matriz, hashes y manifest |
| **2** | [#2 — Word REV02.1 sincronizado y cotejo textual](https://github.com/vsalesa/books/issues/2) | DOCX íntegro editable cotejado con las 16 aperturas y todos los párrafos |
| **3** | [#3 — Auditoría de retratos de 42 personajes](https://github.com/vsalesa/books/issues/3) | Un retrato correcto y distinto por personaje, con fuente original verificada |
| **4** | [#4 — Revisión literaria y ampliación con criterio](https://github.com/vsalesa/books/issues/4) | Lectura por capítulos, continuidad y eventual ampliación sin relleno |
| **5** | [#5 — QA editorial y preimpresión KDP](https://github.com/vsalesa/books/issues/5) | PDF final, índice, A5, sangrado, grises y verificación página por página |

Las issues 2 y 3 pueden avanzar en paralelo una vez fijados archivos maestros. La revisión de imprenta se ejecutará al final. No es necesario esperar a las 180 páginas para evaluar narrativamente cada capítulo.

## Riesgos principales que NO deben repetirse

- **Texto:** la importación a Canva produjo diacríticos descompuestos, espacios perdidos, tildes extrañas y rótulos pegados. Mantener DOCX como fuente editable fiable y cotejarlo con REV02.1.
- **Personajes:** en fases anteriores se inventaron nombres, cambiaron roles y se duplicaron rostros. Mantener la lista maestra, distinguir caras y respetar los 42 nombres.
- **Ilustraciones:** evitar escenas repetidas, PNG recortados de baja resolución, imágenes de ejemplo y fondos que parezcan pegados.
- **Edición:** capítulos en página nueva; 16 banderolas con ilustraciones con aire, títulos completos, letra capitular; matriz solo como imagen profesional.
- **Progreso:** no confundir «creado en Canva», «guardado en el repositorio» y «verificado para imprenta». Cada entrega actualiza un archivo, una issue y una versión identificable.
- **Repositorio público:** antes de publicar binarios de trabajo, revisar privacidad, derechos de imágenes y posibles archivos que no se quieran compartir.

## Fuentes de decisión

- [Historia detallada de acuerdos](editorial/HISTORIAL_DECISIONES_Y_ERRORES.md)
- [Guía de estilo definitiva](editorial/GUIA_DE_ESTILO.md)
- [Canva de edición vigente](https://www.canva.com/design/DAHauUTL81o/edit)

## Próxima acción inequívoca

**Resolver la issue #1: subir los originales binarios** desde los archivos ya recuperados y los materiales del Codex local. Una vez existan realmente en GitHub y se hayan actualizado los checksums, cotejar el DOCX original y producir el Word sincronizado (#2).

**No se ha comprobado el contenido interno de la máquina local de Codex**; el último reporte aportado por el autor coincide con REV02.1.
