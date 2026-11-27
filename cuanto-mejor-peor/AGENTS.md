# Instrucciones permanentes del proyecto — Cuanto mejor, peor

## Fuente de control

- Repositorio principal: `https://github.com/vsalesa/books`.
- Carpeta de proyecto: `cuanto-mejor-peor/`.
- **Por defecto, cada archivo, documento, fuente, ilustración o entrega nueva del libro debe guardarse en GitHub en esta carpeta.**
- Un archivo generado únicamente en un contenedor, una carpeta de Codex, la Biblioteca de ChatGPT o Canva **no se considera entregado ni respaldado** hasta que se haya incorporado al repositorio y comprobado su existencia.
- Canva sigue siendo el editor de diseño. Mantener el ID y enlace de cada revisión en el repositorio; guardar también una exportación PDF/DOCX de esa versión en GitHub cuando sea posible.

## Procedimiento para cada entrega

1. Comprobar la última versión vigente en `README.md`, `PLAN_DE_CONTINUACION.md`, `versiones/README.md` y los issues abiertos antes de modificar contenido.
2. Crear o actualizar el material en la subcarpeta adecuada: `fuentes/`, `editorial/`, `personajes/`, `ilustraciones/`, `ediciones/`, `materiales/`, `versiones/` o `scripts/`.
3. Usar nombres claros y versionados, sin sobrescribir una edición histórica aprobada. Conservar originales y variantes relevantes.
4. Subir los bytes del archivo a GitHub, no solo el nombre, una ruta local, una extracción textual o un enlace de Canva. Para binarios, verificar tamaño y SHA-256. Para ficheros grandes, usar Git LFS o una Release si procede.
5. Confirmar mediante lectura/listado en GitHub que el archivo existe. Comunicar el enlace exacto y el commit/versión cuando proceda.
6. Actualizar `materiales/INVENTARIO.md`, `SEGUIMIENTO.md` y el issue correspondiente, diferenciando **subido**, **solo disponible localmente**, **en Canva** y **pendiente**.
7. Si la subida falla o la herramienta no admite el binario, informar del impedimento y ofrecer una vía verificable. **Nunca afirmar que está en GitHub si no se ha subido realmente**.

## Privacidad y publicación

El repositorio `vsalesa/books` es **público**. Antes de subir archivos, inspeccionar si contienen datos personales de terceros, secretos, credenciales, información privada, imágenes sin autorización o material ajeno al proyecto. Ante contenido sensible, no publicarlo automáticamente: solicitar decisión sobre destino seguro o redactar una versión pública.

## Edición literaria y gráfica

- Versión vigente comprobada al redactar esta norma (27-11-2026): **V4.06.1 REV02.1**, 139 páginas A5, Canva `DAHauUTL81o`.
- Seguir `editorial/GUIA_DE_ESTILO.md` y `editorial/HISTORIAL_DECISIONES_Y_ERRORES.md`.
- Mantener la lista maestra y la identidad de los 42 personajes; revisar la calidad gráfica y la distinción de rostros.
- No confundir respaldo textual extraído de Canva con el original Word/PDF.
- La revisión final de imprenta y el Word editable sincronizado siguen pendientes.

## Respuesta al autor

Al entregar un documento nuevo, incluir **el enlace de GitHub** correspondiente como enlace principal. Se pueden añadir PDF de previsualización, Canva y otras copias secundarias, pero no sustituir el respaldo del repositorio por ellas.
