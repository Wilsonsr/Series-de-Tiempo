# Series de Tiempo y Forecasting con Python

Curso universitario aplicado para formular, explorar, modelar, validar y comunicar problemas de pronóstico. La ruta principal utiliza **Python**. Los materiales en **R son opcionales** y se presentan como apoyo, ejemplos alternativos o profundización.

## Ruta rápida

| Recurso | Contenido |
|---|---|
| [Programa](01_programa/programa_curso.md) | Propósito, resultados de aprendizaje y organización académica |
| [Cronograma](01_programa/cronograma.md) | Ruta de 16 semanas |
| [Evaluación](01_programa/evaluacion.md) | Actividades, porcentajes y entregables |
| [Clases](02_clases/) | Módulos semanales y notebooks Python |
| [Datos](03_datos/) | Datasets organizados por tema |
| [Talleres](04_talleres/) | Actividades prácticas y entregables |
| [Proyecto final](05_proyecto_final/) | Instrucciones, avances, entrega y rúbrica |
| [Recursos](06_recursos/) | Material R renderizado, scripts y complementos |
| [Revisión manual](99_revision_manual/) | Duplicados, versiones y archivos no eliminados |

## Resultados de aprendizaje

Al finalizar el curso, el estudiante podrá:

- formular un problema temporal y justificar frecuencia y horizonte;
- explorar, preparar y visualizar series de tiempo;
- establecer baselines antes de construir modelos complejos;
- aplicar train/test temporal y backtesting con ventanas móviles;
- construir y comparar ETS, ARIMA, SARIMA, SARIMAX, Prophet y modelos de machine learning;
- diagnosticar residuales y cuantificar incertidumbre;
- trabajar de forma introductoria con múltiples series, jerarquías y modelos VAR/VECM;
- comunicar pronósticos, limitaciones y recomendaciones de manera reproducible.

## Flujo de trabajo

```mermaid
flowchart LR
    A["Problema y horizonte"] --> B["Exploración"]
    B --> C["Preparación"]
    C --> D["Baseline"]
    D --> E["Validación temporal"]
    E --> F["Modelos candidatos"]
    F --> G["Diagnóstico y comparación"]
    G --> H["Incertidumbre"]
    H --> I["Pronóstico"]
    I --> J["Comunicación"]
```

## Cronograma de 16 semanas

| Semana | Tema | Notebook Python principal | R opcional |
|:---:|---|---|:---:|
| 1 | Fundamentos y planteamiento del problema | [Abrir](02_clases/01_fundamentos_series_tiempo/python/01_fundamentos_series_tiempo.ipynb) | Sí |
| 2 | Exploración y visualización temporal | [Módulo](02_clases/02_exploracion_temporal/README.md) | No requerido |
| 3 | Preparación, resampling e imputación | [Abrir](02_clases/03_preparacion_datos/python/03_preparacion_datos_temporales.ipynb) | Sí |
| 4 | Validación, backtesting, métricas y baselines | [Abrir](02_clases/04_validacion_baselines/python/04_validacion_backtesting_metricas.ipynb) | No requerido |
| 5 | Suavizamiento exponencial y ETS | [Abrir](02_clases/05_suavizamiento_exponencial/python/05_suavizamiento_exponencial.ipynb) | Sí |
| 6 | Estacionariedad, ACF, PACF y ARMA | [Abrir](02_clases/06_estacionariedad_acf_pacf/python/06_estacionariedad_acf_pacf_arma.ipynb) | Sí |
| 7 | ARIMA y metodología Box-Jenkins | [Abrir](02_clases/07_arima/python/07_arima_box_jenkins.ipynb) | Sí |
| 8 | SARIMA | [Abrir](02_clases/08_sarima/python/08_sarima.ipynb) | Sí |
| 9 | Regresión dinámica y SARIMAX | [Abrir](02_clases/09_sarimax_regresion_dinamica/python/09_sarimax_variables_exogenas.ipynb) | Sí |
| 10 | Prophet | [Abrir](02_clases/10_prophet/python/10_prophet_multiples_series.ipynb) | No requerido |
| 11 | Machine learning y feature engineering | [Abrir](02_clases/11_machine_learning/python/11_machine_learning_bicicletas.ipynb) | No requerido |
| 12 | Forecasting probabilístico e incertidumbre | [Módulo](02_clases/12_forecasting_probabilistico/README.md) | No requerido |
| 13 | Múltiples series y forecasting jerárquico | [Módulo](02_clases/13_multiples_series_jerarquico/README.md) | No requerido |
| 14 | Modelos VAR | [Abrir](02_clases/14_var/python/14_introduccion_var.ipynb) | Sí |
| 15 | Clínica avanzada: VECM, deep learning y modelos fundacionales | [Abrir](02_clases/15_clinica_avanzada/python/15_cointegracion_vecm.ipynb) | Sí |
| 16 | Presentación y defensa del proyecto final | [Proyecto](05_proyecto_final/README.md) | — |

## Abrir notebooks principales en Google Colab

| Semana | Colab |
|:---:|---|
| 1 | [Abrir fundamentos](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/01_fundamentos_series_tiempo/python/01_fundamentos_series_tiempo.ipynb) |
| 3 | [Abrir preparación](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/03_preparacion_datos/python/03_preparacion_datos_temporales.ipynb) |
| 4 | [Abrir validación](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/04_validacion_baselines/python/04_validacion_backtesting_metricas.ipynb) |
| 5 | [Abrir suavizamiento](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/05_suavizamiento_exponencial/python/05_suavizamiento_exponencial.ipynb) |
| 6 | [Abrir estacionariedad](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/06_estacionariedad_acf_pacf/python/06_estacionariedad_acf_pacf_arma.ipynb) |
| 7 | [Abrir ARIMA](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/07_arima/python/07_arima_box_jenkins.ipynb) |
| 8 | [Abrir SARIMA](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/08_sarima/python/08_sarima.ipynb) |
| 9 | [Abrir SARIMAX](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/09_sarimax_regresion_dinamica/python/09_sarimax_variables_exogenas.ipynb) |
| 10 | [Abrir Prophet](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/10_prophet/python/10_prophet_multiples_series.ipynb) |
| 11 | [Abrir machine learning](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/11_machine_learning/python/11_machine_learning_bicicletas.ipynb) |
| 14 | [Abrir VAR](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/14_var/python/14_introduccion_var.ipynb) |
| 15 | [Abrir VECM](https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/02_clases/15_clinica_avanzada/python/15_cointegracion_vecm.ipynb) |

## Python como ruta principal

Los notebooks obligatorios se encuentran dentro de `python/`. Cuando un módulo contiene `ejemplos/` o `complementarios/`, estos materiales amplían la sesión y no sustituyen el notebook principal.

Los materiales en `r_opcional/`:

- no son requisito para completar el curso;
- pueden utilizarse para contrastar implementaciones;
- conservan ejemplos académicos valiosos del repositorio original;
- no necesariamente cubren exactamente el mismo caso que Python.

## Cómo ejecutar los notebooks

### Google Colab

Cambie la ruta del enlace según el notebook que desee abrir:

```text
https://colab.research.google.com/github/Wilsonsr/Series-de-Tiempo/blob/main/<ruta-del-notebook>.ipynb
```

### Entorno local

```bash
git clone https://github.com/Wilsonsr/Series-de-Tiempo.git
cd Series-de-Tiempo
jupyter lab
```

Algunos notebooks avanzados requieren librerías pesadas o acceso a internet. Revise siempre el README del módulo antes de ejecutarlos.

## Estado de los contenidos

Los módulos 2, 12 y 13 necesitan un notebook principal nuevo o consolidado. La carpeta `99_revision_manual/` preserva materiales con errores, duplicados o datos faltantes; no forma parte de la ruta del estudiante.

## Autor

**Wilson Sandoval Rodríguez**  
Curso de Series de Tiempo y Forecasting
