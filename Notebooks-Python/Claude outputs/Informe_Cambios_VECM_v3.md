# Revisión final — `15_Cointegracion_VECM_Mejorado.ipynb` (versión 3)

**Base:** la versión 2 que estaba en la carpeta (no se encontró un archivo con "(1)" en el nombre; la versión de la carpeta tenía el mismo tamaño que la entregada).
**Datos:** `datos_vecm.csv` sin cambios. **Ejecución:** 89 celdas (38 de código) ejecutadas en orden en un kernel nuevo, sin errores ni avisos, en ≈ 11 s (Python 3.13, statsmodels 0.14.5, pandas 2.3.3, numpy 2.5.3, scipy 1.18.1).

## 1. Johansen (Módulo 6)

| Antes (v2) | Ahora (v3) |
|---|---|
| La implementación propia del caso 2 (`ci`) se "validaba" solo comparando el vector β con `VECM`. | **Validación completa e independiente:** la traza y el máximo autovalor coinciden exactamente con $2(\ell_{r}-\ell_{r_0})$ calculados con las verosimilitudes de `VECM(deterministic="ci")` (r = 1, 2) y la verosimilitud de r = 0 calculada a mano, con 0, 1 y 2 rezagos. |
| Se afirmaba que los valores críticos tabulados del caso 3 "suponen deriva", sin comprobarlo. | Se explica que 3.84 es el percentil 95 % de una $\chi^2_1$, la distribución asintótica de la última prueba **cuando la tendencia común tiene deriva**, y se comprueba por simulación: el percentil 95 % es 8.04 sin deriva, 4.46 con deriva 0.2 y 3.99 con deriva 1. |
| La equivalencia `coint_johansen(det_order=1)` ↔ caso 5 figuraba como "aprox.". | Se declara **no verificada**: el código elimina una tendencia lineal de los niveles con toda la muestra, lo que no coincide literalmente con los casos 4 ni 5. La equivalencia `det_order=0` ↔ caso 3 se declara verificada solo con 1-3 rezagos. |
| p-valores únicamente asintóticos (T = 500). | Nuevo *bootstrap* de rango con T = 120 (en la línea de Cavaliere, Rahbek y Taylor, 2012): valores críticos 20.18 y 9.03, p = 0.001 y 0.341. La decisión r = 1 no cambia. |
| Se presentaba lo validado sin distinguir grados. | Una sección enumera qué quedó validado por completo (estadísticos del caso 2 y del caso 3 con 1-3 rezagos), qué solo de forma aproximada (valores críticos simulados, diferencias de hasta ≈ 3-5 % con la tabla en la cola de m = 1) y qué no se verificó (det_order = 1). |

## 2. Cambios estructurales (Módulo 8.3)

- **Corrección de una conclusión no respaldada.** La v2 decía que un cambio de nivel en 2020 "no es significativo". Al repetir el contraste con los tratamientos que recomiendan Johansen, Mosconi y Nielsen (2000), el resultado de 2020 **depende de cómo se traten los meses extremos**: p = 0.16 sin ficticias, **p = 0.019** con una ficticia de impulso en marzo de 2020 y p = 0.30 con ficticias en marzo-mayo. Para 2022, p entre 0.63 y 0.96 en los tres casos.
- Se explica qué contrasta la prueba (solo un cambio de **intercepto** con β y α fijos) y qué no (cambios de **pendiente** o de ajuste), la necesidad de fijar la fecha de antemano, la corrección de Bonferroni por probar dos fechas y la baja potencia con 34 meses posteriores a 2022.
- Nueva conclusión: no se detecta cambio de nivel en 2022; para 2020 la evidencia es frágil y no permite afirmar ni descartar; los cambios en β y α solo tienen evidencia exploratoria (estimación recursiva).

## 3. Pronósticos (Módulo 10)

- Nueva tabla de RMSE y MAE **por variable y horizonte**, con el mejor modelo en cada casilla: para el crudo gana el VECM en 4 de 6 horizontes; para el gasóleo, el ingenuo a 1-2 meses y el VAR en niveles a 3-6. El VECM nunca es el mejor para el gasóleo.
- Explicación de por qué el mejor modelo depende de la variable, el horizonte y la métrica.
- Diebold-Mariano: ahora también por variable (27 comparaciones). Se exponen sus condiciones de aplicación: muestras de 13-18, estacionariedad del diferencial, **modelos anidados con ventana expansiva** (la distribución no es estándar: Clark y McCracken, 2001; Clark y West, 2007; Giacomini y White, 2006) y comparaciones múltiples. Se usa como evidencia descriptiva. Una comparación tiene p < 0.05 (gasóleo, h = 6, VECM peor que VAR en niveles) y se informa como tal.

## 4. Funciones impulso-respuesta (Módulo 9)

- Verificación del *bootstrap*: con los residuos reales, la recursión reproduce exactamente la serie observada.
- Sesgo estimado por el *bootstrap* (≤ 0.23 puntos porcentuales, pequeño frente al ancho de las bandas).
- Alcance de las bandas: punto a punto, condicionales al rango, rezagos, términos deterministas y orden de Cholesky; limitaciones del remuestreo i.i.d. con ARCH (alternativa: *wild bootstrap*).
- Sensibilidad al orden ampliada: qué cambia (reparto del componente común entre los choques) y qué no (IRF no ortogonalizadas y covarianzas de pronóstico), con las cifras de ambos órdenes.

## 5. Pedagogía

- Tabla de **ruta esencial y profundización** en la portada y etiquetas *(ruta esencial)* / *(profundización)* en los apartados de los Módulos 6-10 y los apéndices.
- **Módulo 6 simplificado:** la ruta esencial (6.1-6.4) presenta rezagos, la idea de la prueba, la especificación y el resultado; la implementación, las validaciones, los valores críticos, el *bootstrap* y la comparación de casos pasan a 6.5-6.8. No se eliminó ningún procedimiento.

## 6. Interpretación

- La constante $\hat\mu_0$ ya no se interpreta como "unidades y margen"; se explica que depende de las unidades y de la pendiente.
- El reparto de la corrección se cuantifica (el gasóleo aporta ≈ 54 %) en lugar de "la mayor parte".
- La lectura del ECT como margen de refinación se marca como interpretación económica; se añade febrero de 2015 entre los valores extremos.
- Nueva tabla en 7.3: resultado / evidencia estadística / interpretación económica / limitación.
- Módulo 11 reescrito con esa misma estructura para cada pregunta; incorpora la fragilidad del contraste de 2020 y el resultado de Diebold-Mariano.
- Respuesta sugerida 7.2: separa lo que dice la prueba (no se rechaza) de la interpretación económica.

## 7. Reproducibilidad: qué no se pudo verificar

- **Entorno del autor.** No fue posible conectarse a su computador durante esta revisión, por lo que la v3 no se ejecutó en Windows con statsmodels 0.14.6. La v1 dio resultados idénticos en ambos entornos; se recomienda ejecutar la v3 una vez y comparar con este informe.
- **Descarga opcional desde Yahoo Finance** (`DESCARGAR = True`): no verificada, porque este entorno no tiene acceso a ese sitio. El caso base no la necesita.
- Todas las cifras citadas en el texto proceden de la ejecución descrita arriba; las simulaciones y *bootstrap* usan semillas fijas.

## Referencias añadidas

Cavaliere, Rahbek y Taylor (2012); Clark y McCracken (2001); Clark y West (2007); Giacomini y White (2006); Johansen, Mosconi y Nielsen (2000).
