<div align='center'>    
    
# **Series de Tiempo**

### Wilson Sandoval Rodriguez
</div>    


El curso tiene como objetivo principal introducir a los estudiantes a los métodos fundamentales y avanzados de análisis de series de tiempo, junto con sus aplicaciones en una amplia variedad de disciplinas, tales como: estudios actuariales, climatología, economía, finanzas, geografía, meteorología, ciencias políticas, gestión de riesgos y sociología.

Se abordarán las técnicas de modelado de series de tiempo desde un enfoque práctico, haciendo énfasis en su uso en la predicción y en la interpretación de resultados cuando sea pertinente. Aunque los modelos lineales recibirán una atención detallada, se incluirán extensiones hacia modelos no lineales, con un enfoque en su aplicabilidad a problemas complejos del mundo real.

El curso se centra en: 
- Los conceptos fundamentales de las series de tiempo, incluyendo componentes como tendencia, estacionalidad y ruido.
- La aplicación práctica de los métodos mediante ejemplos contextualizados y el uso de software estadístico como R y Python.
- La comparación y selección de técnicas de modelado en función de sus ventajas, limitaciones y la naturaleza de los datos.
  
Al final del curso, los estudiantes estarán preparados para implementar y evaluar modelos de series de tiempo en contextos diversos, utilizando herramientas computacionales y un enfoque analítico crítico.


|Semana|Tema|Lectura|
|---|---|---|
|1|**Fundamentos del análisis de series de tiempo:** Forecasting, nowcasting y detección de anomalías. Componentes, frecuencia y horizonte de pronóstico.|Hyndman & Athanasopoulos, *Forecasting: Principles and Practice* (Cap. 1) ; Introducción general (docs)|
|2|**Preparación de datos temporales:** Resampling, manejo de valores faltantes y atípicos, transformaciones y calendarios.|Hyndman & Athanasopoulos (Cap. 2) ; pandas time series docs|
|3|**Evaluación en series de tiempo:** Entrenamiento y prueba temporal, backtesting y métricas de desempeño.|Hyndman & Athanasopoulos (Cap. 5)|
|4|**Modelos de suavizamiento exponencial y ETS:** Modelos basados en estado para series univariadas.|Hyndman & Athanasopoulos (Cap. 7–8) ; statsmodels ETS docs|
|5|**Modelos ARIMA y SARIMA:** Identificación, estimación y diagnóstico.|Hyndman & Athanasopoulos (Cap. 9–10) ; statsmodels ARIMA/SARIMAX docs|
|6|**Modelos con variables exógenas:** Regresión dinámica y SARIMAX.|statsmodels SARIMAX documentation|
|7|**Modelos aditivos modernos:** Prophet y detección de changepoints.|Prophet official documentation|
|8|**Machine Learning para series de tiempo:** Series temporales como problema supervisado e ingeniería de características.|sktime user guide (Supervised Forecasting)|
|9|**Pronóstico probabilístico:** Intervalos de predicción, cuantiles y evaluación de incertidumbre.|Hyndman & Athanasopoulos (Cap. 6)|
|10|**Series múltiples y datos tipo panel:** Modelos globales y pronóstico por grupos.|sktime or darts documentation (Global Models)|
|11|**Pronóstico jerárquico:** Reconciliación y coherencia entre series.|Hyndman et al. (2011), *Optimal forecast reconciliation*|
|12|**Modelos multivariados clásicos:** VAR para análisis dinámico multivariable.|Lütkepohl, *New Introduction to Multiple Time Series Analysis* (Cap. VAR)|
|13|**Modelos de corrección del error:** Cointegración y modelos VEC.|Lütkepohl (Cap. VEC) ; statsmodels VECM docs|
|14|**Deep Learning para series de tiempo:** Modelos secuenciales y convolucionales para forecasting.|darts documentation (N-BEATS, TCN)|
|15|**Detección de anomalías y monitoreo:** Identificación de comportamientos atípicos y drift temporal.|Chandola et al. (2009), *Anomaly Detection: A Survey*|
|16|**Presentación de proyectos finales:** Integración de modelos y análisis comparativo de resultados.|—|




|Semana|Tema|Lectura|
|---|---|---|
|1|**Introducción a las Series de Tiempo:** Conceptos básicos: Tipos de datos de series de tiempo, componentes (tendencia, estacionalidad, ciclos, ruido).|<a href="https://docs.google.com/document/d/1X-KnJP9FAvmkS89UIjmv8KBc6qyfCVsj/edit?usp=sharing&ouid=111401641962812428858&rtpof=true&sd=true"> PDA <a/> ; <a href="https://github.com/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/1_Introduccion.ipynb">  Introducción </a> |
|2| **Suavizamiento Exponencial:** Suavizamiento simple, doble (Holt) y triple (Holt-Winters).Análisis de tendencia y estacionalidad. Ventajas y limitaciones del método.|<a  href="https://github.com/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/2_Suavizado%20Exponencial.ipynb"> Suavizamiento Exp.</a>|
|3|**Procesos Estacionarios:** Introducción a los procesos ARMA | <a href="https://github.com/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/3_procesos_estacionarioa%20ARMA.ipynb">  Procesos Estacionarios </a>|
|4|**Modelos ARIMA para series de tiempo no estacionarias:** Técnicas de identificación y raíces unitarias en modelos de series de tiempo.Primer avance. Problema, justificación y objetivos. 
|5|**Modelos SARIMA:** y Análisis Estacional Avanzado| <a href="https://github.com/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/5_SARIMA.ipynb"> Sarima <a/>  ;  <a href="https://github.com/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/6_sarima_gas_box_cox.ipynb" > Box-Cox </a>  |
|6|**Introducción a Prophet:** Construcción y ajuste de modelos Prophet.||
|7|**Criterios de evaluación (RMSE, MAE, MAPE, AIC/BIC) y validación cruzada temporal**.Análisis Comparativo de Metodologías: ARIMA, SARIMA, Holt-Winters, ETS, Prophet.||
|8|**Introducción a Machine Learning para Series de Tiempo**  modelos basados en regresores como Random Forest, XGBoost, y su adaptación para series temporales ||
|9|**Introducción a Series Multivariadas** Modelos SARIMAX 
|10|**Segundo avance**. Marco teórico – Previa metodología-modelo univariado||
|11|**Modelos VAR:** para Series Multivariadas||
|12|**Modelos de corrección del Error VEC**||
|13|**Machine Learning para Series Multivariadas**||
|14|**Deep Learning para Series Multivariadas**||
|15|**Datos Tipo Panel**||
|16|**Presentación Proyectos Finales**||



|Semana|Tema|Lectura|
|---|---|---|
|1|**Fundamentos del análisis de series de tiempo:** Diferencia entre forecasting, nowcasting y detección de anomalías. Componentes de una serie temporal, frecuencia y horizonte de pronóstico.| |
|2|**Preparación de datos temporales:** Resampling, manejo de valores faltantes y atípicos, transformaciones y calendarios.| |
|3|**Evaluación en series de tiempo:** Esquemas de entrenamiento y prueba temporal, backtesting y métricas de desempeño.| |
|4|**Modelos de suavizamiento exponencial y ETS:** Modelos basados en estado para series de tiempo univariadas.| |
|5|**Modelos ARIMA y SARIMA:** Identificación, estimación y diagnóstico de modelos autorregresivos integrados.| |
|6|**Modelos con variables exógenas:** Regresión dinámica y modelos SARIMAX.| |
|7|**Modelos aditivos modernos:** Prophet y detección de changepoints.| |
|8|**Machine Learning para series de tiempo:** Series temporales como problema supervisado e ingeniería de características temporales.| |
|9|**Pronóstico probabilístico:** Intervalos de predicción, cuantiles y evaluación de la incertidumbre.| |
|10|**Series múltiples y datos tipo panel:** Modelos globales y pronóstico por grupos.| |
|11|**Pronóstico jerárquico:** Reconciliación y coherencia entre series agregadas y desagregadas.| |
|12|**Modelos multivariados clásicos:** Modelos VAR para análisis dinámico multivariable.| |
|13|**Modelos de corrección del error:** Cointegración y modelos VEC.| |
|14|**Deep Learning para series de tiempo:** Modelos secuenciales y convolucionales para forecasting.| |
|15|**Detección de anomalías y monitoreo:** Identificación de comportamientos atípicos y drift temporal.| |
|16|**Presentación de proyectos finales:** Integración de modelos y análisis comparativo de resultados.| |





<!--


1.  <a href="https://github.com/Wilsonsr/Series-de-Tiempo/blob/main/CUADERNOS/presentacion.Rmd"> Introducción </a>





-->

## Evaluación
Las notas se distribuirán de la siguiente manera

|ACTIVIDAD|PORCENTAJE|
|---|---|
|Quices-Talleres| 50%|
|Proyecto|50% (10- 20- 20)|
|Total|100%|


+ Primer avance. Problema, justificación y objetivos.
+ Segundo avance. Marco teórico –previa metodología-
+ Metodología y primeros resultados.
+ Exposiciones Entrega Final


 <a href="https://www.superfinanciera.gov.co/publicaciones/10082252/informes-y-cifrascifrasestablecimientos-de-creditoinformacion-periodicamensualcalidad-de-cartera-establecimientos-de-credito-10082252/"> Superfinanciera </a>

<a href="https://docs.google.com/document/d/1y3lnQ_wxnQS7QVg2KbOwjuRYibVn2Oaw/edit?usp=sharing&ouid=111401641962812428858&rtpof=true&sd=true"> Rubrica <a/>

  

