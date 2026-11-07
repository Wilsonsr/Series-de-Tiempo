# Informe de cambios — `15_Cointegracion_VECM_Mejorado.ipynb`, versión 2

**Base de trabajo:** la versión del notebook que estaba en la carpeta el 31 de octubre de 2026, incluidas las ediciones del autor (se eliminaron las notas que comparaban con el cuaderno original y una pregunta del Módulo 5; esas eliminaciones se respetaron).
**Respaldo:** la versión anterior se guardó como `15_Cointegracion_VECM_Mejorado_respaldo_2026-10-31.ipynb`.
**Datos:** `datos_vecm.csv` no se modificó.
**Ejecución:** 82 celdas, ejecución completa en kernel limpio sin errores ni avisos (≈ 15 s). Python 3.13, numpy 2.5.3, pandas 2.3.3, scipy 1.18.1, statsmodels 0.14.5, matplotlib 3.11.2, seaborn 0.13.2. La versión anterior, ejecutada por el autor con statsmodels 0.14.6 en Windows, produjo resultados numéricos idénticos a los de este entorno.

---

## 1. Errores econométricos encontrados y su corrección

| # | Dónde (v1) | Problema | Corrección (v2) |
|---|---|---|---|
| 1 | Módulo 7, celda de la constante | Se estimaba el VECM con `deterministic="co"` y se tomaba $\mu_0$ de un segundo modelo `"ci"` para construir el ECT y escribir el equilibrio: se mezclaban parámetros de dos especificaciones. | Todo el análisis usa una sola especificación, `"ci"` (constante restringida): selección de rezagos, prueba de rango, estimación, ECT, IRF, *bootstrap* y pronósticos. `"co"` se conserva solo como sensibilidad, leída con sus propios parámetros (Módulo 7.1). |
| 2 | Módulo 6 | La prueba de rango usaba `coint_johansen(det_order=0)` (caso 3: constante sin restringir) mientras el modelo de interés era de constante restringida (caso 2), que `coint_johansen` no ofrece. Además, los valores críticos del caso 3 suponen deriva en los niveles, que los datos no tienen (variación media nula, p ≈ 0.78). Esto producía la ambigüedad "r = 1 o r = 2". | Se implementó la prueba de Johansen (función `johansen`) para los casos 2 y 3, validada contra `coint_johansen` y contra `VECM("ci")`. Los valores críticos del caso 2 se obtienen por simulación (reproducen los de Osterwald-Lenum, 1992) y dan p-valores. Resultado: **r = 1 sin ambigüedad con 0 a 3 rezagos**. Se muestra por simulación que, sin deriva, el percentil 95 % del caso 3 es ≈ 8.0 y no 3.84. |
| 3 | Módulo 6 (detectado en esta revisión) | En statsmodels 0.14, `coint_johansen` con `k_ar_diff=0` empareja $\Delta y_t$ con $y_t$ en lugar de $y_{t-1}$ (verificado en el código fuente; con 1-3 rezagos coincide exactamente con la implementación propia). La v1 usaba `select_coint_rank`, que llama a esa función con `k_ar_diff=0`. | La decisión de rango usa la función propia. La discrepancia (traza 36.71 frente a 36.40) se documenta en el notebook; no cambia ninguna decisión. |
| 4 | Módulo 7 | La semivida se presentaba con la fórmula $\ln 0.5/\ln(1+\beta'\alpha)$ sin delimitar su validez. | Se explica que solo es válida con $r=1$ y sin $\Gamma$. Se añade un método general (simulación del sistema estimado sin choques, `trayectoria_desequilibrio`) y se compara con el modelo de dos rezagos, donde la trayectoria no es geométrica. |
| 5 | Módulo 7 | No se distinguía la contribución del ECT de la variación total pronosticada. | Nueva sección 7.4: descomposición del pronóstico de enero de 2025 en $\alpha\cdot ECT$ y en los términos $\Gamma_i\Delta y$, verificada contra `predict()`. En el modelo de dos rezagos, los $\Gamma$ casi anulan el aporte del ECT en la ecuación del crudo. |
| 6 | Módulo 9 | Las IRF se presentaban sin intervalos. | *Bootstrap* de residuos de diseño recursivo (B = 999) con bandas de percentiles del 90 %, con sus limitaciones explícitas (Kilian, 1998; heterocedasticidad; especificación fija). |
| 7 | Módulo 10 | Diebold-Mariano solo a un paso y sin tratamiento de la autocorrelación de los errores solapados. | DM con varianza de largo plazo (autocovarianzas hasta $h-1$) y corrección de Harvey-Leybourne-Newbold, para $h$ = 1, 3 y 6. Tablas separadas de un paso y de varios pasos; explicación de MAE frente a RMSE. |
| 8 | Módulo 8 | El cambio estructural solo se exploraba con estimaciones recursivas. | Se añade una prueba formal de razón de verosimilitudes para un cambio de nivel en la relación de equilibrio (`exog_coint`), con fechas fijadas de antemano (2020-03 y 2022-03). Se separan explícitamente las pruebas formales de las comprobaciones exploratorias. |
| 9 | Módulos 6-7 | La elección de los términos deterministas no se contrastaba. | Prueba LR de "constante solo dentro de la relación" (`ci` frente a `co`): LR = 0.08, p = 0.77. Se muestra que las constantes de `co` son prácticamente $\hat\alpha\hat\mu_0$ y que la deriva implícita es ≈ 0. |
| 10 | Módulos 6 y 8 | Correspondencia de casos de Johansen con códigos de `statsmodels` incompleta. | Tabla de los cinco casos con sus equivalencias en `VECM(deterministic=)` y `coint_johansen(det_order=)`. |
| 11 | Gráficos | En Windows (fuente Arial) aparecían avisos por el carácter "₂" en etiquetas de matplotlib. | Todas las etiquetas matemáticas de los gráficos usan la notación `$...$` de matplotlib. |

## 2. Cambios por módulo

- **Portada y Módulo 0.** Requisitos previos, versión 2, nota de versiones (0.14.5 y 0.14.6). Se elimina `select_coint_rank` de las importaciones (ya no se usa).
- **Módulo 1.** Se elimina el diagrama de dispersión (redundante con el nuevo gráfico de la relación de largo plazo del Módulo 7). Actividad 1.1.
- **Módulo 2 (ampliado).** Ejemplo numérico de una serie I(1) frente a una estacionaria; ejemplo numérico de combinación estacionaria y desequilibrio; nueva sección 2.3 sobre **regresión espuria**, con el caso simulado y un Monte Carlo de 2 000 réplicas (86 % de rechazos con |t| > 1.96 en niveles frente a ≈ 6 % en diferencias). Actividades 2.1 y 2.2.
- **Módulo 3.** Tabla de símbolos conectada con los atributos de `statsmodels`; relación explícita entre $p$ y `k_ar_diff`; exogeneidad débil; nueva sección 3.5 sobre constante dentro y fuera de la relación; la derivación general pasa al Apéndice A. Actividad 3.1.
- **Módulo 4.** Se añade la prueba de media cero de las diferencias (ausencia de deriva) como evidencia para los términos deterministas.
- **Módulo 5.** Encabezado con las cuatro preguntas; contenido conservado.
- **Módulo 6 (reestructurado).** Selección de rezagos con `"ci"` y prueba Portmanteau por candidato; hipótesis nulas y alternativas de traza y máximo autovalor; cinco casos deterministas; función `johansen` con dos validaciones; valores críticos simulados; tabla de sensibilidad caso 2 frente a caso 3; sección sobre rango estadístico frente a interpretación económica. Actividades 6.1 (antes de Johansen) y 6.2.
- **Módulo 7 (reestructurado).** Especificación única `"ci"`; comparación `ci`/`co` sin mezclar parámetros y prueba LR; ejemplo numérico del ECT con los precios de diciembre de 2024; gráfico de la relación de largo plazo junto al ECT; lectura de β, α, exogeneidad débil y homogeneidad; descomposición del pronóstico; semivida general; Γ y Granger; efecto de corto frente a largo plazo. Actividades 7.1-7.3.
- **Módulo 8.** Pruebas formales separadas de comprobaciones exploratorias; importancia y límites de la normalidad; prueba LR de cambio estructural; tabla de coherencia económica. Actividad 8.1.
- **Módulo 9.** IRF con bandas *bootstrap*; ejemplo numérico de corto frente a largo plazo; sensibilidad al orden de Cholesky; FEVD verificada. Actividad 9.1.
- **Módulo 10.** Explicación de MAE y RMSE; tablas de un paso y de varios pasos; Diebold-Mariano con corrección HLN; resultados desfavorables al VECM conservados. Actividad 10.1.
- **Módulos 11 y 12.** Conclusiones actualizadas con los resultados de v2; banco de actividades integradoras y proyecto final (incluye el cuaderno 16 de gasolina como opción).
- **Nuevo:** sección de **Respuestas sugeridas**, separada de las actividades; **Apéndice A** (derivación VAR(2) → VECM) y **Apéndice B** (procedimiento de Johansen); referencias añadidas: Granger y Newbold (1974), Phillips (1986), Nielsen y Rahbek (2000), Harvey, Leybourne y Newbold (1997), Newey y West (1987), Kilian (1998).

## 3. Resultados principales (con los datos congelados)

| Resultado | v1 | v2 |
|---|---|---|
| Especificación | `co` (con μ₀ tomado de `ci`) | `ci` en todo el análisis |
| Rango de cointegración | r = 1 "con incertidumbre" (r = 2 al 5 % en varias especificaciones) | r = 1 con 0-3 rezagos (traza r ≤ 1 = 4.38, p simulado = 0.34) |
| Relación de largo plazo | ln CL = 3.51 + 0.845 ln HO | Igual (ahora con una sola especificación) |
| α crudo / α gasóleo | −0.175 (p 0.16) / +0.248 (p 0.02) | Iguales |
| Semivida | 1.4 meses | 1.4 meses (válida en este modelo; método general añadido) |
| IRF | Sin intervalos | Bandas del 90 %: el choque al crudo tiene efecto permanente significativo sobre ambos precios |
| Pronóstico (prueba) | VECM no supera al ingenuo | Igual; además, ninguna diferencia es significativa en DM (h = 1, 3, 6) |

## 4. Aspectos que requieren validación adicional

1. **`coint_johansen` con `k_ar_diff=0`.** La discrepancia se identificó leyendo el código fuente de la serie 0.14 y comparando numéricamente. Conviene verificarla en la versión instalada antes de usar esa función con cero rezagos en otros cuadernos, y podría reportarse a los mantenedores de `statsmodels`.
2. **Valores críticos simulados.** Se obtienen con 5 000 réplicas y T = 500 (aproximación asintótica); reproducen los tabulados con diferencias de hasta ≈ 3 %. Para trabajos de investigación convendría usar más réplicas o valores de muestra finita.
3. **Prueba LR de `ci` frente a `co` y de cambio estructural.** Usan distribuciones χ² asintóticas con $T = 119$; las conclusiones (p = 0.77, 0.16 y 0.96) están lejos de los umbrales, pero son aproximadas.
4. **Bandas *bootstrap* de las IRF.** Percentiles sin corrección de sesgo, con remuestreo i.i.d. de residuos que presentan ARCH; la cobertura real puede diferir del 90 % nominal. La función está implementada solo para la especificación principal (`k_ar_diff = 0`, `ci`).
5. **Robustez de α.** Quién ajusta depende de los rezagos y del período; el notebook lo presenta como hallazgo tentativo, y así debe enseñarse.
6. **Evaluación de pronósticos.** 13-18 pronósticos por horizonte: potencia muy baja para Diebold-Mariano.
7. **Prueba en el entorno del autor.** La v2 se ejecutó con statsmodels 0.14.5 en Linux. Las funciones usadas existen en 0.14.6; se recomienda ejecutar el notebook completo una vez en Windows y comparar con las cifras de la sección 3.
