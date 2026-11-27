# Inventario de materiales y estado de subida (27-11-2026)

> **Regla:** solo `subido a GitHub` significa que los bytes están dentro de `vsalesa/books`. Un ID de Canva, una ruta de Codex o una captura no equivale a copia de seguridad binaria.

## Resumen

| Material | Localizado | Estado en GitHub |
|---|---|---|
| Texto extraído de Canva V4.06.1 REV02.1 (139 páginas) | Sí, 211.023 caracteres / 33.366 grupos no blancos | **SUBIDO** — [fuentes/V4_06_1_REV02_1_Canva_extraccion_texto.txt](../fuentes/V4_06_1_REV02_1_Canva_extraccion_texto.txt) |
| Extracción de lectura del DOCX original V4.06 | Sí | **SUBIDO** — [fuentes/V4_06_DOCX_original_extraccion_lectura.txt](../fuentes/V4_06_DOCX_original_extraccion_lectura.txt) |
| Manuscrito literario V4.04 (Markdown) | Sí | **SUBIDO** — [fuentes/MANUSCRITO_V4_04_REVISION_LITERARIA_01.md](../fuentes/MANUSCRITO_V4_04_REVISION_LITERARIA_01.md) |
| Reparto maestro V1, 42 personajes | Sí | **SUBIDO** — [personajes/REPARTO_MAESTRO_CERRADO_V1.md](../personajes/REPARTO_MAESTRO_CERRADO_V1.md) |
| PDF vigente REV02.1 (139 páginas) | **Sí, en Canva**, archivo original local Codex no transferido | **NO SUBIDO** |
| DOCX vigente REV02.1 sincronizado | No consta validado | **NO EXISTE VALIDADO** |
| PDF + DOCX fuente V4.06 (129 páginas) | Sí, originales recuperados del chat | **NO SUBIDOS COMO BINARIOS** |
| ZIP de transferencia V4.06.1 (aprox. 43 MB, 67 entradas) | Sí, recuperado; contiene 60 colocaciones de imágenes del V4.06 anterior | **NO SUBIDO COMO BINARIO** |
| 42 recortes de retratos V4.06 | Sí, dentro del ZIP anterior (no equivalen necesariamente a imágenes originales de impresión) | **NO SUBIDOS COMO BINARIOS** |
| 16 ilustraciones de apertura V4.06 | Sí, dentro del ZIP anterior | **NO SUBIDOS COMO BINARIOS** |
| Portada original y lámina matriz | Sí, dentro del ZIP anterior | **NO SUBIDOS COMO BINARIOS** |
| 6 nuevas ilustraciones apertura V4.06.1 | Sí, cargadas como recursos de Canva | **NO SUBIDAS COMO PNG A GITHUB** |
| Páginas de retratos generadas en conversación | Sí, varias generaciones locales; hay variantes y duplicados históricos | **NO SUBIDAS COMO BINARIOS** |
| Nuevas capturas de la carpeta `ilustraciones` de Codex | Compartidas por el autor, no equivalen a PNG originales | **PENDIENTES DE INVENTARIO BINARIO** |

## Edición vigente

- **Canva V4.06.1 REV02.1:** [DAHauUTL81o](https://www.canva.com/design/DAHauUTL81o/edit), 139 páginas A5
- **Historial:** [../versiones/README.md](../versiones/README.md)

## Seis PNG nuevos registrados en la biblioteca de Canva

| Capítulo | Tema | Canva media_id | Página que reemplazaban en V4.06 |
|---:|---|---|---:|
| 7 | Informe, filtraciones y documentación | `MAHat1rl8l0` | 62 |
| 9 | Periódico, café y tostada | `MAHat29Ts_Y` | 80 |
| 11 | Votación del patio escolar | `MAHat7wSkHw` | 98 |
| 12 | Club de petanca y registros de socios | `MAHat83rOok` | 108 |
| 13 | La Parada, cierre y despedida | `MAHat73UE0E` | 114 |
| 14 | Fotografía y publicidad institucional | `MAHauI26720` | 123 |

Estos seis assets fueron confirmados como PNG de 1536 × 1024 px en Canva. Su existencia en la biblioteca de Canva **no significa que se hayan subido a GitHub**. Fueron incorporados en la edición de trabajo de 129 páginas y figuran en la REV02.1.

## Fuentes gráficas originales históricas

El ZIP `CUANTO_MEJOR_PEOR_TRANSFERENCIA_V4_06_1.zip` incluye:
- `imagenes_base/portada/pag_001_portada.png` (1772 × 2512 px)
- `imagenes_base/matriz/pag_076_matriz.jpeg`
- `imagenes_base/personajes/`: 42 retratos recortados de páginas 4–14
- `imagenes_base/aperturas/`: 16 ilustraciones de apertura, nombradas por página y capítulo
- `INVENTARIO_IMAGENES_V4_06.json`: rutas, página, dimensiones, SHA-256, xref y ppp efectivos
- Fuente PDF y DOCX V4.06, registro de personajes y plan editorial

Este inventario pertenece a la versión fuente **V4.06**, no al arte final **REV02.1**. La galería extraída puede tener resolución menor que el arte generado original. El ZIP registra tres usos exactamente duplicados en la V4.06: páginas 15/108, 17/123 y 91/114, corregidos conceptualmente con las seis sustituciones posteriores.

## Láminas de retratos individuales generadas en el chat

Estas diez **páginas completas** existen en el material de conversación en PNG. Constituyen referencias para el estilo e identidad, pero **no son las 42 caras como PNG maestros independientes**:

1. `ayuntamiento_y_despacho_retratos_municipales.png`
2. `vecindario_y_barra_retratos_del_barrio.png`
3. `intermediarios_y_contactos_retratos_en_tinta.png`
4. `guía_de_poder_y_oposición.png`
5. `guía_de_personajes_justicia_y_cloacas.png`
6. `guía_de_personajes_medios_y_estrategia.png`
7. `guía_de_personajes_trabajo_y_calle.png`
8. `otros_protagonistas_del_pueblo.png`
9. `administración_y_técnicos_en_viñetas.png`
10. `secundarios_institucionales_en_retratos.png`

## Procedimiento para terminar la sincronización

1. Recuperar del Codex local el ZIP `CUANTO_MEJOR_PEOR_V4_06_1_REV02_1_MATERIALES.zip` y los PNG originales de `ilustraciones`.
2. Identificar hashes SHA-256 y eliminar solo **copias exactas**; mantener variantes gráficas en `ilustraciones/variantes/`.
3. Subir los binarios a GitHub en `ediciones/V4_06_1_REV02_1/`, `ilustraciones/personajes/`, `ilustraciones/aperturas/`, `ilustraciones/portada/`, `ilustraciones/matriz/`. Si se supera el tamaño conveniente para Git, considerar Git LFS o Releases.
4. Actualizar este inventario con `subido`, URL y hash por recurso.
5. Conservar los PDF y Word anteriores en `versiones/historicas/` o referencias de procedencia, sin mezclar con arte final.

**Precaución:** `vsalesa/books` es un repositorio **público**. Si hubiera imágenes, borradores o archivos de trabajo que el autor no quiera publicar, no deben subirse sin revisar su contenido.
