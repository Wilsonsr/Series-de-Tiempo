# Trazabilidad de la reorganización

Fecha de reorganización: 2026-08-07.

## Criterios

- Python quedó como ruta académica principal.
- Todos los notebooks de Python se reunieron en una sola carpeta.
- R se conservó en una carpeta independiente de material opcional.
- No se eliminó ningún archivo.
- Los duplicados exactos se preservaron en `99_revision_manual/duplicados/`.
- Las variantes, borradores y notebooks con errores almacenados se conservaron con nombres descriptivos dentro de la carpeta única de Python.
- Los datos se movieron de `Data/` a `03_datos/`.
- Las imágenes se movieron de `Data/` y `Notebooks-Python/` a `assets/images/`.
- Los HTML generados en R se conservaron junto al material opcional, dentro de `renderizados/`.

## Mapa general

| Ubicación anterior | Ubicación nueva |
|---|---|
| Notebooks de Python dispersos | `Notebooks-Python/` |
| `Cuadernos R/*.Rmd`, `*.R` | `Cuadernos-R-opcional/` |
| `Cuadernos R/*.html` | `Cuadernos-R-opcional/renderizados/` |
| `Data/` | `03_datos/<tema>/`, `assets/images/` o recursos complementarios |
| Duplicados y copias | `99_revision_manual/duplicados/` |
| Variantes y borradores de notebooks | `Notebooks-Python/`, identificados en el nombre |
| Artefactos de sesión y logs | `99_revision_manual/posibles_obsoletos/` |

Git puede detectar los movimientos por similitud de contenido. Las rutas internas conocidas a `Data/`, `/bases/` y descargas locales fueron actualizadas mecánicamente sin alterar resultados estadísticos.
