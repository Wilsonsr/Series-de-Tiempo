# Trazabilidad de la reorganización

Fecha de reorganización: 2026-08-07.

## Criterios

- Python quedó como ruta académica principal.
- R se conservó bajo `r_opcional/` o `complementarios/`.
- No se eliminó ningún archivo.
- Los duplicados exactos se preservaron en `99_revision_manual/duplicados/`.
- Los archivos con errores almacenados se separaron de la ruta del estudiante.
- Los datos se movieron de `Data/` a `03_datos/`.
- Las imágenes se movieron de `Data/` y `Notebooks-Python/` a `assets/images/`.
- Los HTML generados se separaron de sus fuentes.

## Mapa general

| Ubicación anterior | Ubicación nueva |
|---|---|
| `Notebooks-Python/` | `02_clases/<modulo>/python/` o `99_revision_manual/` |
| `Cuadernos R/*.Rmd`, `*.R` | `02_clases/<modulo>/r_opcional/` o recursos complementarios |
| `Cuadernos R/*.html` | `06_recursos/renderizados/r/` |
| `Data/` | `03_datos/<tema>/`, `assets/images/` o recursos complementarios |
| Duplicados y copias | `99_revision_manual/duplicados/` |
| Archivos con errores | `99_revision_manual/errores_ejecucion/` |
| Material con datos faltantes | `99_revision_manual/datos_faltantes/` |
| Artefactos de sesión y logs | `99_revision_manual/posibles_obsoletos/` |

Git puede detectar los movimientos por similitud de contenido. Las rutas internas conocidas a `Data/`, `/bases/` y descargas locales fueron actualizadas mecánicamente sin alterar resultados estadísticos.

