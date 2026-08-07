<div align="center">

# 📈 Series de Tiempo

### Análisis, modelado y pronóstico con Python y R

**Wilson Sandoval Rodríguez**

*Forecasting · Nowcasting · Anomalías · ARIMA · SARIMA · SARIMAX · Prophet · Machine Learning · VAR/VEC · Deep Learning*

</div>

---

## 🚀 Acceso rápido

| Recurso | Descripción |
|---|---|
| 📘 [Programa del curso](Programa.md) | Objetivos, contenidos y organización general |
| 🐍 [Cuadernos Python](Cuadernos%20Python/) | Notebooks, ejercicios y ejemplos aplicados |
| 📊 [Cuadernos R](Cuadernos%20R/) | Scripts, R Markdown y ejemplos reproducibles |
| 💾 [Datos](Data/) | Bases de datos utilizadas durante el curso |
| 🧪 [Evaluación de modelos](sesion3_evaluacion_series_tiempo_5.ipynb) | Ejemplo de evaluación y comparación temporal |

---

## 🎯 Sobre el curso

El curso de **Series de Tiempo** introduce los fundamentos y las principales metodologías para analizar, modelar y pronosticar fenómenos que evolucionan a través del tiempo.

El enfoque es principalmente **práctico y aplicado**. A lo largo del curso se combinan conceptos estadísticos, visualización, programación y evaluación predictiva mediante **Python y R**, utilizando datos provenientes de diferentes contextos como economía, finanzas, salud, climatología, meteorología, gestión de riesgos y otros campos de aplicación.

Más que aprender modelos de manera aislada, el curso busca desarrollar un **flujo completo de trabajo para problemas de forecasting**, desde la comprensión de los datos hasta la validación y comunicación de los resultados.

---

## 🧭 Flujo de trabajo del curso

```mermaid
flowchart LR
    A[Datos temporales] --> B[Exploración]
    B --> C[Preparación]
    C --> D[Partición temporal]
    D --> E[Backtesting]
    E --> F[Modelos candidatos]
    F --> G[Diagnóstico]
    G --> H[Comparación]
    H --> I[Pronóstico]
    I --> J[Incertidumbre]
    J --> K[Comunicación de resultados]
```

> **Idea central:** en series de tiempo no basta con obtener un buen ajuste histórico. El modelo debe evaluarse respetando el orden temporal y demostrando capacidad de generalización hacia datos futuros.

---

## 🎓 Resultados de aprendizaje

Al finalizar el curso, el estudiante estará en capacidad de:

- Identificar **tendencia, estacionalidad, ciclos, ruido y cambios estructurales** en una serie temporal.
- Preparar datos temporales mediante **resampling, imputación, transformaciones y tratamiento de valores atípicos**.
- Diseñar esquemas apropiados de **entrenamiento, validación y prueba temporal**.
- Implementar estrategias de **backtesting** y validación con ventana móvil.
- Comparar modelos mediante métricas como **MAE, RMSE, MAPE y MASE**.
- Construir e interpretar modelos **ETS, ARIMA, SARIMA y SARIMAX**.
- Incorporar variables externas mediante modelos de **regresión dinámica**.
- Aplicar modelos modernos como **Prophet** y algoritmos de **Machine Learning**.
- Analizar **series múltiples, datos tipo panel y sistemas multivariados**.
- Introducir modelos **VAR, cointegración y VEC**.
- Comprender los fundamentos del **pronóstico probabilístico** y la incertidumbre predictiva.
- Explorar aplicaciones de **Deep Learning** y detección de anomalías en series de tiempo.
- Seleccionar modelos de manera crítica según el problema, los datos y el horizonte de pronóstico.

---

## 🗺️ Ruta de aprendizaje

| Semana | Tema | Material disponible |
|:---:|---|---|
| **1** | Fundamentos de series de tiempo: forecasting, nowcasting, anomalías, componentes, frecuencia y horizonte | [Python](Cuadernos%20Python/1_Introduccion.ipynb) · [R](Cuadernos%20R/1_introducci%C3%B3n.Rmd) |
| **2** | Preparación de datos temporales: resampling, faltantes, atípicos, transformaciones y calendarios | [Python](Cuadernos%20Python/2_resampling_transformaciones_imputacion.ipynb) · [R](Cuadernos%20R/imputacion.Rmd) |
| **3** | Evaluación temporal: train/test, backtesting y métricas de desempeño | [Python](Cuadernos%20Python/sesion3_evaluacion_series_tiempo_5.ipynb) |
| **4** | Suavizamiento exponencial: SES, Holt y Holt-Winters | [Python](Cuadernos%20Python/2_Suavizado%20Exponencial.ipynb) · [R](Cuadernos%20R/Alisamiento-expone.Rmd) |
| **5** | Estacionariedad, procesos ARMA y fundamentos de ARIMA | [ARMA](Cuadernos%20Python/3_procesos_estacionarioa%20ARMA.ipynb) · [ARIMA](Cuadernos%20Python/codigo_base_ARIMA.ipynb) |
| **6** | Modelos SARIMA: identificación, estimación y diagnóstico | [Python](Cuadernos%20Python/5_SARIMA.ipynb) · [R](Cuadernos%20R/SARIMA.Rmd) |
| **7** | Variables exógenas, regresión dinámica y SARIMAX | [Python](Cuadernos%20Python/sarimax_soi_rec.ipynb) · [R](Cuadernos%20R/SARIMAX-SOIREC.Rmd) |
| **8** | Modelos aditivos modernos: Prophet y changepoints | [Python](Cuadernos%20Python/11_Prophet_in_Python.ipynb) |
| **9** | Machine Learning para series de tiempo e ingeniería de características | [Random Forest](Cuadernos%20Python/9_Series%20Tiempo%20Random%20Forest.ipynb) |
| **10** | Pronóstico probabilístico: intervalos, cuantiles e incertidumbre | En desarrollo |
| **11** | Series múltiples y datos tipo panel | [Python](Cuadernos%20Python/datos%20panel.ipynb) · [R](Cuadernos%20R/Datos%20Panel%20teor%C3%ADa.Rmd) |
| **12** | Pronóstico jerárquico y reconciliación de series | En desarrollo |
| **13** | Modelos multivariados clásicos: VAR | [Python](Cuadernos%20Python/VAR%20Introduccion.ipynb) · [R](Cuadernos%20R/VAR.Rmd) |
| **14** | Cointegración y modelos de corrección del error VEC | [R](Cuadernos%20R/cointegracion.Rmd) |
| **15** | Deep Learning, modelos avanzados y detección de anomalías | [Redes neuronales](Cuadernos%20Python/series_tiempo_redes_neuronales.ipynb) · [Amazon Chronos](Cuadernos%20Python/Amazon_Chronos.ipynb) |
| **16** | Presentación de proyectos finales y comparación de resultados | 🎓 Proyecto final |

---

## 🐍 Cuadernos destacados en Python

Los notebooks pueden visualizarse directamente en GitHub o ejecutarse en Google Colab.

| Tema | GitHub | Google Colab |
|---|:---:|:---:|
| Introducción | [📓 Abrir](Cuadernos%20Python/1_Introduccion.ipynb) | [▶️ Colab](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/1_Introduccion.ipynb) |
| Preparación de datos | [📓 Abrir](Cuadernos%20Python/2_resampling_transformaciones_imputacion.ipynb) | [▶️ Colab](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/2_resampling_transformaciones_imputacion.ipynb) |
| Evaluación temporal | [📓 Abrir](Cuadernos%20Python/sesion3_evaluacion_series_tiempo_5.ipynb) | [▶️ Colab](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/sesion3_evaluacion_series_tiempo_5.ipynb) |
| Suavizamiento exponencial | [📓 Abrir](Cuadernos%20Python/2_Suavizado%20Exponencial.ipynb) | [▶️ Colab](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/2_Suavizado%20Exponencial.ipynb) |
| ARIMA | [📓 Abrir](Cuadernos%20Python/codigo_base_ARIMA.ipynb) | [▶️ Colab](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/codigo_base_ARIMA.ipynb) |
| SARIMA | [📓 Abrir](Cuadernos%20Python/5_SARIMA.ipynb) | [▶️ Colab](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/5_SARIMA.ipynb) |
| SARIMAX | [📓 Abrir](Cuadernos%20Python/sarimax_soi_rec.ipynb) | [▶️ Colab](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/sarimax_soi_rec.ipynb) |
| Prophet | [📓 Abrir](Cuadernos%20Python/11_Prophet_in_Python.ipynb) | [▶️ Colab](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/11_Prophet_in_Python.ipynb) |
| Random Forest | [📓 Abrir](Cuadernos%20Python/9_Series%20Tiempo%20Random%20Forest.ipynb) | [▶️ Colab](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/9_Series%20Tiempo%20Random%20Forest.ipynb) |
| VAR | [📓 Abrir](Cuadernos%20Python/VAR%20Introduccion.ipynb) | [▶️ Colab](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/VAR%20Introduccion.ipynb) |
| Redes neuronales | [📓 Abrir](Cuadernos%20Python/series_tiempo_redes_neuronales.ipynb) | [▶️ Colab](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/Cuadernos%20Python/series_tiempo_redes_neuronales.ipynb) |

> Si un notebook requiere archivos externos, revise primero la carpeta [`Data`](Data/) y las instrucciones incluidas dentro del propio cuaderno.

---

## 📊 Material en R

La carpeta [`Cuadernos R`](Cuadernos%20R/) contiene ejemplos desarrollados mediante **R, R Markdown y HTML**, incluyendo:

- Introducción a series de tiempo.
- Suavizamiento exponencial.
- Imputación de datos temporales.
- Transformaciones Box-Cox.
- SARIMA y SARIMAX.
- Series múltiples y datos panel.
- Modelos VAR.
- Cointegración y VEC.
- Aplicaciones y ejemplos reproducibles.

---

## 🧠 Modelos y enfoques estudiados

```text
Métodos clásicos
├── Suavizamiento exponencial
│   ├── SES
│   ├── Holt
│   └── Holt-Winters
├── AR / MA / ARMA
├── ARIMA
├── SARIMA
└── SARIMAX

Métodos modernos
├── Prophet
├── Machine Learning
│   └── Random Forest
├── Forecasting probabilístico
├── Modelos globales
├── Forecasting jerárquico
└── Deep Learning

Series multivariadas
├── VAR
├── Cointegración
└── VEC

Monitoreo
├── Detección de anomalías
├── Cambios estructurales
└── Drift temporal
```

---

## 📐 Evaluación de modelos

Durante el curso se hace especial énfasis en que la evaluación debe respetar la estructura temporal de los datos.

### Principios clave

1. **No mezclar aleatoriamente pasado y futuro.**
2. Definir claramente el **horizonte de pronóstico**.
3. Utilizar un conjunto de prueba temporal o esquemas de **rolling/expanding window**.
4. Comparar varios modelos bajo el **mismo esquema de evaluación**.
5. Revisar tanto las métricas como los **residuales y la estabilidad del modelo**.
6. Incorporar la **incertidumbre** en la interpretación del pronóstico.

### Métricas frecuentes

- **MAE** — Mean Absolute Error.
- **RMSE** — Root Mean Squared Error.
- **MAPE** — Mean Absolute Percentage Error.
- **MASE** — Mean Absolute Scaled Error.

---

## 📝 Evaluación del curso

| Actividad | Porcentaje |
|---|:---:|
| Quices y talleres | **50 %** |
| Proyecto aplicado | **50 %** |
| **Total** | **100 %** |

### 🎓 Proyecto aplicado

El proyecto busca integrar los conceptos desarrollados durante el curso mediante el análisis de un problema real que involucre datos temporales.

**Avance 1 — 10 %**  
Definición del problema, justificación, objetivos y descripción inicial de los datos.

**Avance 2 — 20 %**  
Marco conceptual, análisis exploratorio temporal, propuesta metodológica y modelos candidatos.

**Entrega final — 20 %**  
Modelado, backtesting, comparación de resultados, pronóstico, interpretación, conclusiones y presentación final.

### Criterios esperados en el proyecto

- Problema claramente formulado.
- Variable temporal correctamente definida.
- Frecuencia y horizonte de pronóstico justificados.
- Análisis exploratorio coherente con la naturaleza temporal.
- Separación adecuada de entrenamiento y prueba.
- Comparación de al menos dos enfoques cuando sea pertinente.
- Uso de métricas de desempeño apropiadas.
- Diagnóstico de residuales y revisión de supuestos cuando aplique.
- Interpretación de resultados en el contexto del problema.
- Código reproducible y conclusiones sustentadas en la evidencia.

> Los enlaces institucionales de clase, rúbricas, grupos y sesiones sincrónicas se comparten mediante los canales oficiales del curso.

---

## 🗂️ Estructura del repositorio

```text
Series-de-Tiempo/
│
├── README.md
├── Programa.md
├── Cuadernos Python/
│   └── Notebooks y ejercicios en Python
├── Cuadernos R/
│   └── Scripts, R Markdown y HTML
├── Data/
│   └── Bases de datos utilizadas en clase
├── sesion3_evaluacion_series_tiempo_5.ipynb
└── mapa_captación_temprana_de_gestantes.html
```

---

## ⚙️ ¿Cómo utilizar este repositorio?

### Opción 1 — Visualizar los materiales

Puede navegar directamente por las carpetas y abrir los notebooks o documentos desde GitHub.

### Opción 2 — Ejecutar Python en Google Colab

Utilice los enlaces **▶️ Colab** disponibles en la sección de cuadernos destacados. Esta opción permite trabajar desde el navegador sin realizar una instalación local completa.

### Opción 3 — Clonar el repositorio

```bash
git clone https://github.com/Wilsonsr/Series-de-Tiempo.git
cd Series-de-Tiempo
```

Posteriormente puede abrir los notebooks desde **JupyterLab**, **Jupyter Notebook**, **VS Code** o el entorno de su preferencia.

---

## 🛠️ Herramientas utilizadas

| Área | Herramientas |
|---|---|
| Programación | Python · R |
| Notebooks | Jupyter Notebook · Google Colab |
| Análisis estadístico | statsmodels · scipy · R |
| Manipulación de datos | pandas · numpy · dplyr |
| Visualización | matplotlib · plotly · ggplot2 |
| Forecasting | ARIMA · SARIMA · SARIMAX · Prophet |
| Machine Learning | scikit-learn |
| Series multivariadas | VAR · VEC |

> Las librerías utilizadas pueden variar según el notebook y la metodología desarrollada en cada sesión.

---

## 📚 Recursos recomendados

Como material complementario se recomienda consultar documentación y textos de referencia sobre:

- Forecasting y análisis de series de tiempo.
- *Forecasting: Principles and Practice*.
- Documentación oficial de Prophet.
- Documentación de `statsmodels` para modelos de series de tiempo.
- Documentación de `scikit-learn` para evaluación y Machine Learning.
- Recursos de R para forecasting, modelos dinámicos y series multivariadas.

---

## 🤝 Recomendaciones para estudiantes

- Revise el material **antes de cada sesión**.
- Ejecute los notebooks y modifique parámetros para observar cómo cambian los resultados.
- No se limite a obtener una métrica: **interprete el comportamiento temporal del modelo**.
- Documente decisiones, supuestos y transformaciones realizadas sobre los datos.
- Mantenga separado el conjunto de datos destinado a la evaluación final.
- Utilice gráficos como herramienta permanente de diagnóstico.
- Compare modelos simples y complejos antes de elegir una solución final.

---

## 👨‍🏫 Autor

**Wilson Sandoval Rodríguez**  
Docente del curso **Series de Tiempo**

GitHub: [@Wilsonsr](https://github.com/Wilsonsr)

---

<div align="center">

### 📈 Del dato histórico a una decisión sobre el futuro

**Explorar · Modelar · Validar · Pronosticar · Comunicar**

⭐ Si este material le resulta útil, puede marcar el repositorio con una estrella.

</div>
