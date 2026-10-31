# Informe de mejoras — Cuaderno de cointegración y VECM

**Archivos revisados:** `15_cointegracion_vecm.ipynb` (principal, 50 celdas) y `15_vecm_preliminar.ipynb` (complementario, 11 celdas).
**Archivos entregados:** `15_Cointegracion_VECM_Mejorado.ipynb` (67 celdas, 12 módulos + configuración), `datos_vecm.csv`, `requirements.txt` y este informe.
**Los originales no se modificaron.**

---

## 1. Auditoría inicial

Clasificación: **EE** error econométrico · **EP** error de programación · **PI** problema de interpretación · **DP** debilidad pedagógica · **MO** mejora opcional.

| # | Dónde (original) | Hallazgo | Tipo |
|---|---|---|---|
| 1 | Celda 21 | ADF y KPSS solo con `'ct'`: en niveles ADF dice "no estacionaria" y KPSS dice "estacionaria"; la contradicción se ignora y se concluye "I(1)" solo con el ADF de las diferencias. No se justifica la tendencia determinista. | EE |
| 2 | Celda 27 | `select_order` ya devuelve `k_ar_diff`; el código le resta 1 (`OPT_LAG - 1`) y además impone `max(1, …)` dos veces. BIC = 0 terminó en `k_ar_diff = 1` por coincidencia de ambos errores. | EE / EP |
| 3 | Celda 28 | Afirma que `det_order=0` es "constante dentro de la relación cointegrante"; en realidad es constante sin restringir (equivale a `deterministic="co"`). La celda 31 dice lo contrario (constante fuera). | PI |
| 4 | Celda 30 | `COINT_RANK = max(1, min(coint_rank, k-1))` fuerza r ≥ 1 aunque Johansen indique r = 0. | EE |
| 5 | Celda 29 | Se reporta un único Johansen; no se examina la sensibilidad a rezagos ni a términos deterministas (el resultado r = 1 vs. r = 2 cambia con ellos). | EE |
| 6 | Celda 34-35 | Interpretación de β incoherente con el orden de columnas (el texto dice β₁ para HO, el código normaliza sobre CO). | PI |
| 7 | Celda 35 | Un α positivo en la ecuación del gasóleo se marca "revisar especificación"; con la normalización usada, α > 0 es justamente el signo que corrige. | PI |
| 8 | Celda 35 | Se presenta α como "% del desequilibrio corregido por período" y se calcula una semivida con un α aislado y `abs(1+α)`, ignorando β'α y Γ. | PI |
| 9 | Celda 18 | El *spread* `ln CO − ln HO` supone β₂ = −1 sin contrastarlo (con la muestra completa se rechaza). | PI |
| 10 | Celda 38 | Índice de residuos construido como `k_ar_diff + coint_rank` (el rango no tiene que ver con las observaciones perdidas); se "ajusta" la longitud recortando si no coincide. | EP |
| 11 | Celda 39 | Durbin-Watson por ecuación y ADF sobre residuos como diagnóstico principal; sin prueba multivariada de autocorrelación, sin ARCH, sin estabilidad. | EE |
| 12 | Celda 40 | ADF ordinario sobre el ECT para "confirmar cointegración" (valores críticos no válidos para un residuo estimado). | EE |
| 13 | Celdas 45-46 | IRF y FEVD calculadas con un VAR en diferencias y presentadas como IRF del VECM; se describen bandas "bootstrap" que no corresponden al modelo. | EE / PI |
| 14 | Celdas 42-43 | Pronóstico sin ninguna evaluación fuera de muestra; las conclusiones afirman superioridad del VECM sin respaldo. | EE / PI |
| 15 | Celda 47 | Conclusiones contradicen las salidas: "α de HeatingOil negativo y significativo" (la salida era +0.10 y no significativo), "correctamente especificado" (normalidad rechazada). | PI |
| 16 | Celda 9 | Descarga obligatoria desde Yahoo en cada ejecución: resultados no reproducibles; precio negativo diario (−37.63) no se trata explícitamente. | EP |
| 17 | Preliminar, celda 0 | `df.columns = ['HeatingOil','CrudeOil']` sobre columnas en orden alfabético (`CL=F`, `HO=F`): **las etiquetas quedan intercambiadas**; todo el cuaderno preliminar interpreta el crudo como gasóleo. | EP |
| 18 | Preliminar | Datos diarios en niveles sin logaritmos, índice sin frecuencia (aviso de `statsmodels`), `freq='MS'` en un pronóstico con fechas de fin de mes. | EP |
| 19 | Celdas 14, 18; preliminar 3 | Gráficos de doble eje, sin unidades homogéneas; interpretaciones impresas con `print` en lugar de texto. | DP |
| 20 | Todo | Secuencia teoría → código sin intuición previa, sin ejemplos simulados, sin "errores frecuentes" ni preguntas de comprensión; ejercicios sin actividad integradora. | DP |
| 21 | Celda 7 | `warnings.filterwarnings('ignore')` global oculta avisos relevantes. | EP |

**Elementos valiosos conservados:** el caso económico (crudo y gasóleo), la frecuencia mensual con último cierre, la transformación logarítmica, la tabla de prerrequisitos y el árbol de decisión (integrados en los Módulos 3 y 6), las tablas de Johansen, el bloque de recomendaciones y los ejercicios propuestos (reescritos y ampliados en el Módulo 12). Del preliminar se recuperó la idea de una función de pronóstico reutilizable.

---

## 2. Correcciones econométricas realizadas

1. **Integración:** ADF y KPSS con constante (especificación principal, justificada económicamente) y con tendencia (sensibilidad), más diferencias; tabla con estadístico, valor crítico, p-valor (KPSS truncado indicado como "< 0.01"/"> 0.10"), decisión y lectura conjunta. Resultado: evidencia coherente de I(1) con constante; no concluyente con tendencia. La conclusión se formula como "razonable, no demostrada".
2. **Rezagos:** se usa directamente `k_ar_diff` de `select_order`, sin restar ni imponer mínimos. BIC/HQIC eligen 0 y AIC/FPE eligen 2; se adopta BIC (0) y se valida que los residuos no tienen autocorrelación. `k_ar_diff = 0` se presenta como especificación válida (VAR(1) en niveles).
3. **Johansen:** traza y máximo autovalor, `select_coint_rank` al 5 % y al 1 %, y una malla de sensibilidad (3 rezagos × 3 especificaciones deterministas). Hallazgo central: r ≥ 1 es robusto; r = 1 vs. r = 2 es dudoso al 5 %. Se adopta r = 1 con tres argumentos explícitos y se compensa la incertidumbre comparando, en el pronóstico, con modelos coherentes con r = 0 y r = 2. Se documenta la correspondencia `det_order` ↔ `deterministic` y que `"ci"` no tiene equivalente directo en `coint_johansen`.
4. **α y β:** tablas con errores estándar, intervalos y p-valores; constante de la relación obtenida con la variante `"ci"` (idéntica β); prueba informal de homogeneidad (IC de β₂ excluye −1 con la muestra completa, pero no antes de 2022); interpretación del signo de α según la normalización; ejemplo numérico de corrección con β'α; semivida derivada de la dinámica completa (válida porque `k_ar_diff = 0`) y contrastada con un AR(1) directo del ECT; distinción entre normalización e identificación.
5. **IRF/FEVD:** IRF calculadas con `vecm_res.irf()`; verificación de que β'·IRF(∞) ≈ 0; comparación de los dos órdenes de Cholesky; sin bandas (statsmodels no las calcula para VECM, y así se declara). FEVD implementada a partir de `orth_irfs` del VECM, con verificación numérica contra `VARResults.fevd` (coincidencia exacta).
6. **Diagnóstico:** Portmanteau multivariada, Ljung-Box, Jarque-Bera multivariada, ARCH-LM, residuos estandarizados y observaciones > 3σ, raíces de la matriz compañera, estimaciones recursivas de β y α, y tabla de sensibilidad (rezagos × `co`/`ci` × ficticias de 2020). Se eliminan DW como prueba de sistema y el ADF sobre residuos y sobre el ECT.
7. **Pronóstico:** partición entrenamiento (2015-2021) / validación (2022-01 a 2023-06) / prueba (2023-07 a 2024-12); origen móvil con ventana expansiva y horizontes 1-6; selección de rezagos solo en validación; comparación de VECM, VAR en diferencias, VAR en niveles e ingenuo; MAE, RMSE, error por horizonte, gráfico de pronósticos vs. observados y Diebold-Mariano a un mes.

---

## 3. Cambios pedagógicos

- Nueva estructura en 12 módulos con la secuencia *pregunta → intuición → visualización → matemática → código → resultado → interpretación → ejercicio*; cada módulo tiene objetivo de aprendizaje, errores frecuentes y "Comprueba tu comprensión".
- **Módulo 2 nuevo:** simulación reproducible de series cointegradas y de paseos aleatorios independientes con correlación igual de alta (0.94 vs. 0.95), con Engle-Granger.
- **Módulo 3 nuevo:** derivación gradual VAR → VECM (bivariado y matricial), tabla de símbolos, aclaraciones sobre normalización y signo de α, ejemplo numérico, y simulación de un VECM verdadero que muestra que β se estima con mucha más precisión que α.
- Interpretaciones en Markdown escritas a partir de las salidas reales y verificadas una por una; las cifras que dependen de los datos se imprimen también desde el código.
- Gráficos sin doble eje (series indexadas o centradas en el mismo eje), colores fijos por variable y por modelo, ejes temporales anuales, anotaciones de eventos, partición sombreada.
- Módulo 11 de discusión que responde a las preguntas del Módulo 1 y separa asociación, cointegración y causalidad.
- Módulo 12 con 15 actividades en 8 bloques y una actividad integradora con opciones, entregable y rúbrica.
- Referencias bibliográficas completas (Engle-Granger 1987; Johansen 1988, 1991, 1995; Johansen-Juselius 1990; Hamilton 1994; Lütkepohl 2005; Juselius 2006; Dickey-Fuller 1979; KPSS 1992; Osterwald-Lenum 1992; Diebold-Mariano 1995; Hyndman-Athanasopoulos 2021; Seabold-Perktold 2010; documentación de statsmodels).

---

## 4. Datos

`datos_vecm.csv` contiene los cierres diarios sin modificar de `CL=F` (USD/barril) y `HO=F` (USD/galón) del 2015-01-02 al 2024-12-31 (2 517 filas, con 3 y 2 faltantes respectivamente y el cierre de −37.63 del 2020-04-20), obtenidos el 31-10-2026 del *endpoint* `v8/finance/chart` de Yahoo Finance. Los primeros valores coinciden con los del cuaderno original (52.69 y 1.7957 el 2015-01-02). Diferencia: el original terminaba el 2024-12-30 (fin exclusivo de `yfinance`); el archivo incluye el 2024-12-31, que pasa a ser el cierre de diciembre de 2024. El cuaderno documenta el posible efecto de empalme en febrero de 2015 (gasóleo +31 % y −29 % en meses consecutivos).

---

## 5. Resultados de las pruebas de ejecución

- Ejecución completa con `jupyter nbconvert --execute` en un kernel limpio: **67 celdas, 0 errores, 0 avisos en las salidas** (tiempo ≈ 8 s).
- Entorno: Python 3.13, numpy 2.5.3, pandas 2.3.3, scipy 1.18.1, statsmodels 0.14.5, matplotlib 3.11.2, seaborn 0.13.2.
- Funciones verificadas en la versión instalada: `select_order`, `select_coint_rank`, `coint_johansen`, `VECM(..., exog=...)`, `fit`, `conf_int_beta`, `pvalues_alpha`, `det_coef_coint`, `test_whiteness`, `test_normality`, `test_granger_causality`, `irf`, `predict(alpha=...)`, `var_rep`.
- Comprobaciones internas que el cuaderno ejecuta: residuos con longitud = `nobs`; raíces de la matriz compañera = {1, 1+β'α}; semivida implícita = semivida del AR(1) directo; β'·IRF(24) ≈ 0; FEVD propia = FEVD de statsmodels en un VAR; ningún pronóstico usa datos posteriores a su origen.
- Se revisaron visualmente las 12 figuras (legibilidad, solapamientos, unidades).

**Resultados principales (con los datos congelados):** T = 120; elasticidad de largo plazo 0.845 (IC 95 % 0.75-0.93); α crudo −0.175 (p = 0.16), α gasóleo +0.248 (p = 0.02); semivida ≈ 1.4 meses; Johansen: r = 0 rechazado con holgura, r ≤ 1 rechazado al 5 % pero no al 1 %. Fuera de muestra (prueba), RMSE relativo al ingenuo: VAR en niveles 0.89, VAR en diferencias 1.10, VECM 1.11; Diebold-Mariano no distingue los modelos a un mes (n = 18).

---

## 6. Afirmaciones del original que se corrigieron por contradecir los resultados

| Afirmación original | Qué muestran los resultados |
|---|---|
| "Ambas series son I(1)" (con ADF y KPSS contradictorios en niveles) | Coherente con constante; no concluyente con tendencia |
| "El VECM con rango r = 1 es APROPIADO" (sin matices) | r ≥ 1 robusto; r = 1 vs. 2 depende de rezagos y del nivel de significancia |
| "α de HeatingOil negativo y significativo" | En la especificación principal es **positivo** y significativo; con `k_ar_diff = 1` (la del original) es positivo y no significativo |
| α positivo = "revisar especificación" | Con β normalizado sobre el crudo, α > 0 en el gasóleo corrige el desequilibrio |
| "Corrige 39 % del desequilibrio por período… semivida 1.4 meses" (con un α aislado) | La corrección total es −β'α; la semivida coincide por casualidad numérica, no por el método |
| IRF "del VECM" con bandas bootstrap | Eran de un VAR en diferencias; las del VECM se calculan ahora sin bandas |
| "Los pronósticos del VECM… a diferencia del VAR en diferencias" (superioridad implícita) | En la prueba fuera de muestra el VECM no supera al ingenuo ni al VAR en diferencias |
| "Modelo correctamente especificado" | Sin autocorrelación, pero con no normalidad y ARCH |

---

## 7. Limitaciones pendientes

1. **Muestra corta** (T = 120) y validación/prueba de 18 meses: las comparaciones de pronóstico tienen poca potencia y la clasificación cambió entre validación y prueba.
2. **Rango ambiguo** (1 vs. 2): no se aplicaron correcciones de muestra pequeña (Bartlett, Reinsel-Ahn) ni p-valores de Johansen por simulación, porque `statsmodels` no los ofrece; se dejan como extensión.
3. **Sin bandas de confianza para IRF/FEVD del VECM**; un *bootstrap* por residuos sería la extensión natural.
4. **No normalidad y ARCH**: los intervalos de pronóstico de `predict` son gaussianos; se advierte en el texto, pero no se implementaron intervalos alternativos.
5. **Posible inestabilidad tras 2022** (homogeneidad y ajuste dependen del período; desequilibrio persistente en 2024): no se aplicó una prueba formal de cambio estructural en cointegración (p. ej., Gregory-Hansen o Hansen-Johansen), que no está en `statsmodels`.
6. **Contrato continuo**: posibles saltos de empalme (febrero de 2015) no corregidos por falta de una serie alternativa verificable.
7. **Sistema bivariado**: omite otros refinados y determinantes comunes; la actividad integradora propone un sistema de tres variables.
8. El cuaderno se ejecutó en Python 3.13 con statsmodels 0.14.5; no se probó en el entorno Anaconda del usuario. Si su versión de statsmodels es distinta, conviene ejecutar el cuaderno completo una vez y comparar con las cifras de la sección 5.
