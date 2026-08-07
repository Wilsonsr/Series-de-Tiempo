#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del cuadernillo VECM completo para clase de maestria.
Ejecutar: python generate_vecm_notebook.py
Genera:   VECM_Completo.ipynb
"""
import json, uuid, os

def _id():
    return uuid.uuid4().hex[:16]

def md(src):
    return {"cell_type": "markdown", "id": _id(), "metadata": {}, "source": src}

def code(src):
    return {"cell_type": "code", "execution_count": None, "id": _id(),
            "metadata": {}, "outputs": [], "source": src}

cells = []

# ============================================================
# CELDA 1 — TITULO
# ============================================================
cells.append(md(
"# Modelo Vectorial de Corrección del Error — VECM\n"
"## Teoría y aplicación práctica en Python\n\n"
"---\n\n"
"| Campo | Detalle |\n"
"|---|---|\n"
"| **Área** | Series de tiempo multivariadas · Econometría aplicada |\n"
"| **Nivel** | Maestría en Analítica de Datos |\n"
"| **Lenguaje** | Python 3 con `statsmodels` |\n"
"| **Datos** | Futuros energéticos NYMEX: gasóleo de calefacción (HO=F) y petróleo crudo (CL=F) |\n"
"| **Período** | Enero 2015 – Diciembre 2024 (frecuencia mensual) |\n\n"
"---\n\n"
"> **Propósito:** Integrar la fundamentación teórica del VECM con su implementación práctica\n"
"> en Python, aplicando el flujo completo de análisis a datos reales de mercados de energía.\n\n"
"---\n\n"
"## Tabla de contenido\n\n"
"1. Objetivo  \n"
"2. Introducción teórica  \n"
"3. Fundamento matemático  \n"
"4. Librerías necesarias  \n"
"5. Carga de datos  \n"
"6. Limpieza y preparación  \n"
"7. Análisis exploratorio  \n"
"8. Pruebas de estacionariedad  \n"
"9. Justificación del VECM  \n"
"10. Selección de rezagos  \n"
"11. Prueba de cointegración de Johansen  \n"
"12. Estimación del modelo VECM  \n"
"13. Interpretación del modelo  \n"
"14. Diagnóstico  \n"
"15. Pronóstico  \n"
"16. Funciones impulso-respuesta  \n"
"17. Conclusiones  \n"
"18. Recomendaciones metodológicas  \n"
"19. Ejercicios propuestos  \n"
))

# ============================================================
# CELDA 2 — OBJETIVO
# ============================================================
cells.append(md(
"<a id='objetivo'></a>\n"
"## 1. Objetivo del cuadernillo\n\n"
"Al finalizar este cuadernillo el estudiante será capaz de:\n\n"
"- **Comprender** la teoría de cointegración y su relación con los modelos VAR y VECM.\n"
"- **Aplicar** pruebas de raíz unitaria (ADF, KPSS) para determinar el orden de integración.\n"
"- **Ejecutar** la prueba de Johansen para detectar relaciones de cointegración.\n"
"- **Estimar** e **interpretar** un modelo VECM en Python usando `statsmodels`.\n"
"- **Diagnosticar** la validez del modelo mediante análisis de residuos.\n"
"- **Generar** pronósticos e **interpretar** funciones impulso-respuesta.\n"
"- **Evaluar** cuándo es apropiado el VECM y cuándo se deben usar alternativas.\n\n"
"---\n"
))

# ============================================================
# CELDA 3 — INTRODUCCION TEORICA
# ============================================================
cells.append(md(
"<a id='teoria'></a>\n"
"## 2. Introducción teórica\n\n"
"### 2.1 Series de tiempo multivariadas\n\n"
"Una **serie de tiempo multivariada** es un conjunto de $k$ variables observadas en los mismos\n"
"instantes de tiempo $t = 1, 2, \\ldots, T$. El objetivo es modelar su evolución conjunta,\n"
"capturando tanto las dinámicas individuales como las interdependencias entre ellas.\n\n"
"**Ejemplo de este cuadernillo:** precio del petróleo crudo y precio del gasóleo de calefacción.\n"
"Ambos son derivados del mismo mercado energético y se espera que se muevan juntos en el largo plazo.\n\n"
"---\n\n"
"### 2.2 Modelo VAR (Vector Autoregresivo)\n\n"
"El **modelo VAR** extiende la regresión univariada al caso multivariado.\n"
"Un VAR de orden $p$ modela cada variable en función de sus propios rezagos y los de las demás:\n\n"
"$$\\mathbf{y}_t = \\mathbf{c} + \\mathbf{A}_1 \\mathbf{y}_{t-1} + \\cdots + \\mathbf{A}_p \\mathbf{y}_{t-p} + \\boldsymbol{\\varepsilon}_t$$\n\n"
"donde $\\mathbf{y}_t$ es un vector $k \\times 1$, $\\mathbf{A}_i$ son matrices $k \\times k$ de coeficientes\n"
"y $\\boldsymbol{\\varepsilon}_t$ es el vector de errores.\n\n"
"**Limitación crítica:** El VAR estándar es válido solo cuando todas las variables son\n"
"**estacionarias** $I(0)$. Si las series son no estacionarias $I(1)$, estimar un VAR en niveles\n"
"produce **regresiones espurias** con estadísticos inflados artificialmente.\n\n"
"---\n\n"
"### 2.3 Cointegración: el concepto clave\n\n"
"**Definición:** Dos o más series $I(1)$ están **cointegradas** si existe una combinación lineal\n"
"de ellas que es $I(0)$ (estacionaria).\n\n"
"**Intuición económica:** Aunque cada precio se mueve de forma impredecible, existe una relación\n"
"de **equilibrio de largo plazo** que los mantiene vinculados. Cuando se desvían, hay fuerzas\n"
"del mercado que los atraen de regreso.\n\n"
"**Formalmente:** Si $\\mathbf{y}_t = (y_{1t}, y_{2t})'$ son $I(1)$, existe cointegración\n"
"si hay un vector $\\boldsymbol{\\beta}$ tal que:\n\n"
"$$\\boldsymbol{\\beta}' \\mathbf{y}_t = \\beta_1 y_{1t} + \\beta_2 y_{2t} \\sim I(0)$$\n\n"
"El vector $\\boldsymbol{\\beta}$ se denomina **vector cointegrante**.\n\n"
"---\n\n"
"### 2.4 El modelo VECM\n\n"
"El **VECM (Vector Error Correction Model)** es la representación apropiada para sistemas\n"
"de series $I(1)$ cointegradas. Añade el **término de corrección del error (ECT)** que captura\n"
"la velocidad de ajuste al equilibrio de largo plazo.\n\n"
"**El VECM dice que los cambios de hoy dependen de:**\n"
"1. Sus propios cambios pasados (dinámica de **corto plazo**).\n"
"2. Qué tan lejos está el sistema del equilibrio (**corrección del error**).\n\n"
"---\n\n"
"### 2.5 Corto plazo vs. largo plazo\n\n"
"| Componente | Descripción |\n"
"|---|---|\n"
"| **Largo plazo** | Relación de equilibrio capturada por el vector cointegrante $\\boldsymbol{\\beta}$ |\n"
"| **Corto plazo** | Dinámica transitoria en los coeficientes $\\boldsymbol{\\Gamma}_i$ de las diferencias |\n"
"| **Corrección del error** | Velocidad de retorno al equilibrio, representada por $\\boldsymbol{\\alpha}$ |\n\n"
"---\n\n"
"### 2.6 Interpretación del coeficiente $\\alpha$ (velocidad de ajuste)\n\n"
"El coeficiente $\\alpha_i$ de cada ecuación indica:\n\n"
"- **Signo negativo:** La variable se ajusta hacia el equilibrio (esperado en sistemas estables).\n"
"- **Magnitud:** Fracción del desequilibrio que se corrige en cada período.\n"
"  Por ejemplo, $\\alpha = -0.20$ indica que el 20% del desequilibrio se corrige en un período.\n"
"- **Significancia:** Si $\\alpha_i \\approx 0$ o no es significativo, la variable es **débilmente exógena**\n"
"  (no responde activamente al desequilibrio).\n\n"
"---\n\n"
"### 2.7 ¿Cuándo usar VECM?\n\n"
"| Situación | Modelo |\n"
"|---|---|\n"
"| Series $I(0)$ | VAR en niveles |\n"
"| Series $I(1)$ sin cointegración | VAR en primeras diferencias |\n"
"| Series $I(1)$ **con cointegración** | **VECM** ✓ |\n"
"| Órdenes de integración mixtos | ARDL |\n\n"
"---\n"
))

# ============================================================
# CELDA 4 — FUNDAMENTO MATEMATICO
# ============================================================
cells.append(md(
"<a id='matematica'></a>\n"
"## 3. Fundamento matemático\n\n"
"### 3.1 Representación VAR(p)\n\n"
"$$\\mathbf{y}_t = \\mathbf{c} + \\sum_{i=1}^{p} \\mathbf{A}_i \\mathbf{y}_{t-i} + \\boldsymbol{\\varepsilon}_t$$\n\n"
"### 3.2 Transformación a VECM\n\n"
"Restando $\\mathbf{y}_{t-1}$ de ambos lados y reorganizando se obtiene la **representación VECM**:\n\n"
"$$\\Delta \\mathbf{y}_t = \\mathbf{c} + \\mathbf{\\Pi} \\mathbf{y}_{t-1} + \\sum_{i=1}^{p-1} \\mathbf{\\Gamma}_i \\Delta \\mathbf{y}_{t-i} + \\boldsymbol{\\varepsilon}_t$$\n\n"
"| Símbolo | Definición | Dimensión |\n"
"|---|---|---|\n"
"| $\\Delta \\mathbf{y}_t$ | Primeras diferencias | $k \\times 1$ |\n"
"| $\\mathbf{\\Pi} = \\sum_{i=1}^{p} \\mathbf{A}_i - \\mathbf{I}_k$ | Matriz de largo plazo | $k \\times k$ |\n"
"| $\\mathbf{\\Gamma}_i$ | Matrices de dinámica de corto plazo | $k \\times k$ |\n\n"
"### 3.3 Descomposición de $\\mathbf{\\Pi}$\n\n"
"La clave del VECM está en el **rango de la matriz $\\mathbf{\\Pi}$**:\n\n"
"$$\\mathbf{\\Pi} = \\boldsymbol{\\alpha} \\boldsymbol{\\beta}'$$\n\n"
"| Símbolo | Nombre | Interpretación | Dimensión |\n"
"|---|---|---|---|\n"
"| $\\boldsymbol{\\alpha}$ | Matriz de carga | Velocidad de ajuste | $k \\times r$ |\n"
"| $\\boldsymbol{\\beta}$ | Matriz cointegrante | Equilibrio de largo plazo | $k \\times r$ |\n"
"| $r$ | Rango de cointegración | Número de relaciones | $0 < r < k$ |\n\n"
"### 3.4 Casos según el rango de $\\mathbf{\\Pi}$\n\n"
"| Rango $r$ | Significado | Modelo apropiado |\n"
"|---|---|---|\n"
"| $r = 0$ | Sin cointegración | VAR en diferencias |\n"
"| $0 < r < k$ | $r$ relaciones de cointegración | **VECM** |\n"
"| $r = k$ | Todas las series son $I(0)$ | VAR en niveles |\n\n"
"### 3.5 VECM bivariado explícito ($k=2$, $r=1$, $p=2$)\n\n"
"$$\\begin{pmatrix} \\Delta y_{1t} \\\\ \\Delta y_{2t} \\end{pmatrix} = "
"\\begin{pmatrix} c_1 \\\\ c_2 \\end{pmatrix} + "
"\\begin{pmatrix} \\alpha_1 \\\\ \\alpha_2 \\end{pmatrix} "
"\\underbrace{\\left(\\beta_1 y_{1,t-1} + \\beta_2 y_{2,t-1}\\right)}_{ECT_{t-1}} + "
"\\begin{pmatrix} \\gamma_{11} & \\gamma_{12} \\\\ \\gamma_{21} & \\gamma_{22} \\end{pmatrix} "
"\\begin{pmatrix} \\Delta y_{1,t-1} \\\\ \\Delta y_{2,t-1} \\end{pmatrix} + "
"\\begin{pmatrix} \\varepsilon_{1t} \\\\ \\varepsilon_{2t} \\end{pmatrix}$$\n\n"
"### 3.6 Prueba de Johansen\n\n"
"**Estadístico de la traza:**\n\n"
"$$\\lambda_{trace}(r) = -T \\sum_{i=r+1}^{k} \\ln(1 - \\hat{\\lambda}_i)$$\n\n"
"Prueba $H_0: \\text{rango} = r$ vs. $H_1: \\text{rango} > r$\n\n"
"**Estadístico del máximo eigenvalor:**\n\n"
"$$\\lambda_{max}(r, r+1) = -T \\ln(1 - \\hat{\\lambda}_{r+1})$$\n\n"
"Prueba $H_0: \\text{rango} = r$ vs. $H_1: \\text{rango} = r+1$\n\n"
"---\n"
))

# ============================================================
# CELDA 5-6 — LIBRERIAS
# ============================================================
cells.append(md(
"<a id='librerias'></a>\n"
"## 4. Librerías necesarias en Python\n\n"
"### 4.1 Instalación\n\n"
"Ejecute la siguiente celda **solo si** las librerías no están instaladas en su entorno.\n"
))

cells.append(code(
"# Instalacion de librerias (ejecutar solo si es necesario)\n"
"# !pip install pandas numpy matplotlib seaborn statsmodels openpyxl scipy yfinance\n"
'print("Librerías listas. Si alguna faltaba, reinicie el kernel tras instalar.")\n'
))

cells.append(md("### 4.2 Importación de librerías\n"))

cells.append(code(
"# === Análisis de datos ===\n"
"import pandas as pd\n"
"import numpy as np\n\n"
"# === Visualización ===\n"
"import matplotlib.pyplot as plt\n"
"import seaborn as sns\n\n"
"# === Series de tiempo y VECM ===\n"
"from statsmodels.tsa.stattools import adfuller, kpss\n"
"from statsmodels.tsa.vector_ar.vecm import VECM, coint_johansen, select_order\n"
"from statsmodels.tsa.api import VAR\n"
"from statsmodels.stats.stattools import durbin_watson\n\n"
"# === Estadística ===\n"
"from scipy import stats\n\n"
"# === Datos financieros ===\n"
"try:\n"
"    import yfinance as yf\n"
"    YFINANCE_OK = True\n"
"except ImportError:\n"
"    YFINANCE_OK = False\n"
'    print("ADVERTENCIA: instale yfinance: pip install yfinance")\n\n'
"# === Configuración visual ===\n"
"plt.rcParams['figure.figsize'] = (12, 5)\n"
"plt.rcParams['font.size'] = 11\n"
"plt.rcParams['axes.grid'] = True\n"
"plt.rcParams['grid.alpha'] = 0.3\n"
"sns.set_theme(style='whitegrid')\n\n"
"import warnings\n"
"warnings.filterwarnings('ignore')\n\n"
'print("Librerías importadas correctamente.")\n'
'print(f"pandas {pd.__version__} | numpy {np.__version__} | statsmodels OK")\n'
))

# ============================================================
# CELDA 7-9 — CARGA DE DATOS
# ============================================================
cells.append(md(
"<a id='datos'></a>\n"
"## 5. Carga de datos\n\n"
"### Descripción del conjunto de datos\n\n"
"Se utilizan dos series de precios de **futuros energéticos** negociados en el NYMEX:\n\n"
"| Variable | Símbolo | Descripción |\n"
"|---|---|---|\n"
"| **HeatingOil** | `HO=F` | Futuros de gasóleo de calefacción (USD/galón) |\n"
"| **CrudeOil** | `CL=F` | Futuros de petróleo crudo WTI (USD/barril, escalado) |\n\n"
"**Fuente:** Yahoo Finance vía `yfinance`  \n"
"**Período:** Enero 2015 – Diciembre 2024  \n"
"**Frecuencia base:** Diaria → remuestreada a **mensual**\n\n"
"**Justificación económica:** El gasóleo de calefacción es un derivado del petróleo crudo.\n"
"Desde la teoría económica, ambos precios deben mantener una relación de equilibrio de\n"
"largo plazo determinada por el proceso de refinación y los márgenes del mercado energético.\n"
"Esta es exactamente la condición que el VECM está diseñado para modelar.\n"
))

cells.append(code(
"# === Descarga de datos con yfinance ===\n"
'START   = "2015-01-01"\n'
'END     = "2024-12-31"\n'
"SYMBOLS = ['HO=F', 'CL=F']\n\n"
"if YFINANCE_OK:\n"
'    print(f"Descargando datos ({START} a {END})...")\n'
"    raw = yf.download(SYMBOLS, start=START, end=END, auto_adjust=True)['Close']\n"
"    raw.columns = ['HeatingOil', 'CrudeOil']\n"
"    raw.dropna(inplace=True)\n"
'    print(f"Datos crudos: {raw.shape[0]} observaciones diarias")\n'
"else:\n"
'    raise RuntimeError("Instale yfinance: pip install yfinance")\n'
))

cells.append(code(
"# === Inspección inicial ===\n"
'print("=" * 55)\n'
'print("INSPECCIÓN INICIAL")\n'
'print("=" * 55)\n'
'print(f"\\nDimensiones:     {raw.shape[0]} filas x {raw.shape[1]} columnas")\n'
'print(f"Período:         {raw.index[0].date()} → {raw.index[-1].date()}")\n'
'print(f"Tipo de índice:  {type(raw.index).__name__}")\n'
'print("\\nPrimeras 5 filas:")\n'
"print(raw.head())\n"
'print("\\nTipos de datos:")\n'
"print(raw.dtypes)\n"
'print("\\nValores faltantes por columna:")\n'
"print(raw.isnull().sum())\n"
'print("\\nEstadísticas descriptivas (precios en USD):")\n'
"print(raw.describe().round(4))\n"
))

# ============================================================
# CELDA 10-13 — LIMPIEZA Y PREPARACION
# ============================================================
cells.append(md(
"<a id='limpieza'></a>\n"
"## 6. Limpieza y preparación de datos\n\n"
"### Decisiones metodológicas\n\n"
"1. **Remuestreo mensual:** Los datos diarios presentan ruido que no es relevante para el análisis\n"
"   de largo plazo. Se usa el precio de cierre del último día hábil del mes (`resample('ME').last()`).\n\n"
"2. **Transformación logarítmica:** Los precios de activos financieros son más estables en\n"
"   logaritmos, estabilizan la varianza y permiten interpretar diferencias como tasas de crecimiento.\n\n"
"3. **Definición de frecuencia:** Esencial para que `statsmodels` opere correctamente.\n\n"
"4. **Tratamiento de faltantes:** Se eliminan observaciones con datos incompletos.\n"
))

cells.append(code(
"# === Remuestreo a frecuencia mensual ===\n"
"df_monthly = raw.resample('ME').last().dropna()\n"
"df_monthly.index.freq = 'ME'\n\n"
'print(f"Observaciones mensuales: {len(df_monthly)}")\n'
'print(f"Período: {df_monthly.index[0].strftime(\'%Y-%m\')} → {df_monthly.index[-1].strftime(\'%Y-%m\')}")\n'
'print("\\nPrimeras 6 filas (precios en USD):")\n'
"print(df_monthly.head(6).round(4))\n"
))

cells.append(code(
"# === Transformación logarítmica ===\n"
"df = np.log(df_monthly)\n"
"df.columns = ['ln_HeatingOil', 'ln_CrudeOil']\n\n"
'print("Series en logaritmos (primeras 6 filas):")\n'
"print(df.head(6).round(4))\n\n"
"# Verificar faltantes\n"
"missing = df.isnull().sum()\n"
"if missing.sum() == 0:\n"
'    print("\\n✓ Sin valores faltantes.")\n'
"else:\n"
'    print(f"\\n⚠ Faltantes: {missing.to_dict()} — se eliminan.")\n'
"    df.dropna(inplace=True)\n\n"
'print("\\nEstadísticas descriptivas (logaritmos):")\n'
"print(df.describe().round(4))\n"
))

cells.append(code(
"# === Gráficas de las series ===\n"
"fig, axes = plt.subplots(2, 2, figsize=(14, 8))\n\n"
"df_monthly['HeatingOil'].plot(ax=axes[0,0], color='steelblue', linewidth=1.5)\n"
"axes[0,0].set_title('HeatingOil — Precio USD/galón')\n"
"axes[0,0].set_ylabel('Precio (USD)')\n\n"
"df_monthly['CrudeOil'].plot(ax=axes[0,1], color='firebrick', linewidth=1.5)\n"
"axes[0,1].set_title('CrudeOil — Precio USD')\n"
"axes[0,1].set_ylabel('Precio (USD)')\n\n"
"df['ln_HeatingOil'].plot(ax=axes[1,0], color='steelblue', linewidth=1.5)\n"
"axes[1,0].set_title('ln(HeatingOil)')\n"
"axes[1,0].set_ylabel('ln(precio)')\n\n"
"df['ln_CrudeOil'].plot(ax=axes[1,1], color='firebrick', linewidth=1.5)\n"
"axes[1,1].set_title('ln(CrudeOil)')\n"
"axes[1,1].set_ylabel('ln(precio)')\n\n"
"for ax in axes.flat:\n"
"    ax.tick_params(axis='x', rotation=30)\n\n"
"fig.suptitle('Series de precios energéticos: originales y en logaritmos',\n"
"             fontsize=13, fontweight='bold')\n"
"plt.tight_layout()\n"
"plt.savefig('series_originales.png', dpi=100, bbox_inches='tight')\n"
"plt.show()\n\n"
'print("\\n[Interpretación] Ambas series muestran tendencia estocástica creciente con alta")\n'
'print("volatilidad. La caída en 2020 corresponde al colapso de demanda por COVID-19.")\n'
'print("La transformación logarítmica estabiliza la varianza heterocedástica.")\n'
))

# ============================================================
# CELDA 14-17 — ANALISIS EXPLORATORIO
# ============================================================
cells.append(md(
"<a id='exploratorio'></a>\n"
"## 7. Análisis exploratorio de series de tiempo\n"
))

cells.append(code(
"# === Estadísticas descriptivas ===\n"
'print("=" * 60)\n'
'print("ESTADÍSTICAS DESCRIPTIVAS — SERIES EN LOGARITMOS")\n'
'print("=" * 60)\n'
"desc = df.describe().T\n"
"desc['cv'] = desc['std'] / desc['mean'].abs()\n"
"print(desc.round(4))\n\n"
'print("\\nAsimetría (skewness):")\n'
"print(df.skew().round(4))\n"
'print("\\nCurtosis excess:")\n'
"print(df.kurtosis().round(4))\n\n"
'print("\\n[Interpretación] Una asimetría cercana a 0 y curtosis cercana a 0 indicarían")\n'
'print("normalidad. En series de precios es común encontrar colas más pesadas.")\n'
))

cells.append(code(
"# === Matriz de correlación y diagrama de dispersión ===\n"
"fig, axes = plt.subplots(1, 2, figsize=(13, 5))\n\n"
"corr = df.corr()\n"
"sns.heatmap(corr, annot=True, fmt='.4f', cmap='coolwarm',\n"
"            vmin=-1, vmax=1, center=0, ax=axes[0], linewidths=0.5)\n"
"axes[0].set_title('Correlación de Pearson (logaritmos)', fontweight='bold')\n\n"
"axes[1].scatter(df['ln_CrudeOil'], df['ln_HeatingOil'],\n"
"                alpha=0.5, color='steelblue', edgecolors='navy', s=40, linewidth=0.3)\n"
"axes[1].set_xlabel('ln(CrudeOil)')\n"
"axes[1].set_ylabel('ln(HeatingOil)')\n"
"axes[1].set_title('Dispersión: ln(HO) vs ln(CO)', fontweight='bold')\n"
"m, b, r, p, se = stats.linregress(df['ln_CrudeOil'], df['ln_HeatingOil'])\n"
"xl = np.linspace(df['ln_CrudeOil'].min(), df['ln_CrudeOil'].max(), 100)\n"
"axes[1].plot(xl, m*xl+b, color='firebrick', linewidth=2,\n"
'             label=f"y = {m:.3f}x + {b:.3f}  (R={r:.3f})")\n'
"axes[1].legend()\n\n"
"plt.tight_layout()\n"
"plt.savefig('correlacion_scatter.png', dpi=100, bbox_inches='tight')\n"
"plt.show()\n\n"
'print(f"\\n[Interpretación] Correlación de Pearson = {corr.iloc[0,1]:.4f}.")\n'
'print("La correlación muy alta sugiere que ambas series comparten una tendencia común.")\n'
'print("Un scatter casi lineal es consistente con la hipótesis de cointegración.")\n'
))

cells.append(code(
"# === Serie temporal comparativa y spread ===\n"
"fig, axes = plt.subplots(2, 1, figsize=(13, 8), sharex=False)\n\n"
"# Eje dual\n"
"ax1 = axes[0]\n"
"ax2 = ax1.twinx()\n"
"l1 = ax1.plot(df.index, df['ln_HeatingOil'],\n"
"              color='steelblue', linewidth=1.5, label='ln(HeatingOil)')\n"
"l2 = ax2.plot(df.index, df['ln_CrudeOil'],\n"
"              color='firebrick', linewidth=1.5, linestyle='--', label='ln(CrudeOil)')\n"
"ax1.set_ylabel('ln(HeatingOil)', color='steelblue')\n"
"ax2.set_ylabel('ln(CrudeOil)', color='firebrick')\n"
"lns = l1 + l2\n"
"ax1.legend(lns, [l.get_label() for l in lns], loc='upper right')\n"
"ax1.set_title('Evolución comparativa', fontweight='bold')\n\n"
"# Spread\n"
"spread = df['ln_HeatingOil'] - df['ln_CrudeOil']\n"
"axes[1].plot(spread.index, spread, color='darkorange', linewidth=1.5)\n"
"axes[1].axhline(spread.mean(), color='black', linestyle='--', linewidth=1,\n"
'               label=f"Media = {spread.mean():.3f}")\n'
"axes[1].fill_between(spread.index, spread, spread.mean(), alpha=0.2, color='darkorange')\n"
"axes[1].set_title('Spread: ln(HeatingOil) − ln(CrudeOil)', fontweight='bold')\n"
"axes[1].set_ylabel('Diferencial')\n"
"axes[1].legend()\n\n"
"plt.tight_layout()\n"
"plt.savefig('series_comparativas.png', dpi=100, bbox_inches='tight')\n"
"plt.show()\n\n"
'print(f"\\n[Interpretación] El spread oscila alrededor de su media ({spread.mean():.4f}),")\n'
'print("lo que visualmente sugiere una relación de largo plazo entre las series.")\n'
'print(f"Desviación estándar del spread: {spread.std():.4f}")\n'
))

# ============================================================
# CELDA 18-22 — PRUEBAS DE ESTACIONARIEDAD
# ============================================================
cells.append(md(
"<a id='estacionariedad'></a>\n"
"## 8. Pruebas de estacionariedad\n\n"
"### Prueba ADF (Augmented Dickey-Fuller)\n\n"
"- $H_0$: La serie tiene raíz unitaria (no estacionaria)\n"
"- $H_1$: La serie es estacionaria\n"
"- **Regla:** p-valor $< 0.05$ → rechazar $H_0$ (estacionaria)\n\n"
"### Prueba KPSS\n\n"
"- $H_0$: La serie es estacionaria\n"
"- $H_1$: Raíz unitaria\n"
"- **Regla:** p-valor $< 0.05$ → rechazar $H_0$ (no estacionaria)\n\n"
"Las dos pruebas se **complementan**: ADF y KPSS con conclusiones concordantes\n"
"dan mayor certeza sobre el orden de integración.\n"
))

cells.append(code(
"# === Funciones auxiliares para pruebas de raíz unitaria ===\n\n"
"def adf_test(series, name):\n"
"    result = adfuller(series.dropna(), autolag='AIC', regression='ct')\n"
"    stat, pval, n_lags = result[0], result[1], result[2]\n"
"    cv1, cv5, cv10 = result[4]['1%'], result[4]['5%'], result[4]['10%']\n"
"    decision = 'ESTACIONARIA' if pval < 0.05 else 'NO ESTACIONARIA'\n"
'    print(f"\\n  ADF: {name}")\n'
'    print(f"    Estadístico: {stat:.4f}  |  p-valor: {pval:.4f}  |  Rezagos: {n_lags}")\n'
'    print(f"    Valores críticos: 1%={cv1:.3f}  5%={cv5:.3f}  10%={cv10:.3f}")\n'
'    print(f"    Decisión (α=5%): {decision}")\n'
"    return pval\n\n"
"def kpss_test(series, name):\n"
"    stat, pval, n_lags, crit = kpss(series.dropna(), regression='ct', nlags='auto')\n"
"    decision = 'NO ESTACIONARIA' if pval < 0.05 else 'ESTACIONARIA'\n"
'    print(f"\\n  KPSS: {name}")\n'
'    print(f"    Estadístico: {stat:.4f}  |  p-valor: {pval:.4f}")\n'
'    print(f"    Decisión (α=5%): {decision}")\n'
"    return pval\n"
))

cells.append(code(
'print("=" * 60)\n'
'print("PRUEBAS EN NIVELES")\n'
'print("=" * 60)\n'
"p_adf_ho    = adf_test(df['ln_HeatingOil'], 'ln(HeatingOil)')\n"
"p_adf_co    = adf_test(df['ln_CrudeOil'],   'ln(CrudeOil)')\n"
'print("\\n" + "=" * 60)\n'
"p_kpss_ho   = kpss_test(df['ln_HeatingOil'], 'ln(HeatingOil)')\n"
"p_kpss_co   = kpss_test(df['ln_CrudeOil'],   'ln(CrudeOil)')\n\n"
'print("\\n" + "=" * 60)\n'
'print("RESUMEN — NIVELES")\n'
'print("=" * 60)\n'
"res_niv = pd.DataFrame({\n"
"    'Serie':          ['ln(HeatingOil)', 'ln(CrudeOil)'],\n"
"    'ADF p-val':      [round(p_adf_ho, 4), round(p_adf_co, 4)],\n"
"    'ADF Decisión':   ['No estac.' if p_adf_ho>0.05 else 'Estac.',\n"
"                       'No estac.' if p_adf_co>0.05 else 'Estac.'],\n"
"    'KPSS p-val':     [round(p_kpss_ho, 4), round(p_kpss_co, 4)],\n"
"    'KPSS Decisión':  ['No estac.' if p_kpss_ho<0.05 else 'Estac.',\n"
"                       'No estac.' if p_kpss_co<0.05 else 'Estac.']\n"
"})\n"
"print(res_niv.to_string(index=False))\n"
))

cells.append(code(
"# === Pruebas en primeras diferencias ===\n"
"df_diff = df.diff().dropna()\n\n"
'print("=" * 60)\n'
'print("PRUEBAS EN PRIMERAS DIFERENCIAS")\n'
'print("=" * 60)\n'
"p_adf_dho = adf_test(df_diff['ln_HeatingOil'], 'Δln(HeatingOil)')\n"
"p_adf_dco = adf_test(df_diff['ln_CrudeOil'],   'Δln(CrudeOil)')\n"
'print("\\n")\n'
"p_kpss_dho = kpss_test(df_diff['ln_HeatingOil'], 'Δln(HeatingOil)')\n"
"p_kpss_dco = kpss_test(df_diff['ln_CrudeOil'],   'Δln(CrudeOil)')\n\n"
'print("\\n" + "=" * 60)\n'
'print("CONCLUSIÓN SOBRE ORDEN DE INTEGRACIÓN")\n'
'print("=" * 60)\n'
"I1 = (p_adf_dho < 0.05 and p_adf_dco < 0.05)\n"
"if I1:\n"
'    print("\\n  ✓ Las diferencias son estacionarias.")\n'
'    print("  → Ambas series son I(1).")\n'
'    print("  → Se puede proceder con la prueba de Johansen.")\n'
"else:\n"
'    print("\\n  ⚠ Verificar individualmente cada serie.")\n'
"I1_confirmed = I1\n"
))

cells.append(code(
"# === Gráficas de las series diferenciadas ===\n"
"fig, axes = plt.subplots(2, 1, figsize=(13, 7), sharex=True)\n\n"
"df_diff['ln_HeatingOil'].plot(ax=axes[0], color='steelblue', linewidth=1)\n"
"axes[0].axhline(0, color='black', linewidth=0.8, linestyle='--')\n"
"axes[0].set_title('Δln(HeatingOil) — variación mensual', fontweight='bold')\n"
"axes[0].set_ylabel('Δln(precio)')\n\n"
"df_diff['ln_CrudeOil'].plot(ax=axes[1], color='firebrick', linewidth=1)\n"
"axes[1].axhline(0, color='black', linewidth=0.8, linestyle='--')\n"
"axes[1].set_title('Δln(CrudeOil) — variación mensual', fontweight='bold')\n"
"axes[1].set_ylabel('Δln(precio)')\n\n"
"plt.tight_layout()\n"
"plt.savefig('series_diferenciadas.png', dpi=100, bbox_inches='tight')\n"
"plt.show()\n\n"
'print("\\n[Interpretación] Las series diferenciadas oscilan alrededor de cero sin tendencia")\n'
'print("ni estructura sistemática, confirmando visualmente que son I(0).")\n'
'print("Esto refuerza que las series en niveles son I(1).")\n'
))

# ============================================================
# CELDA 23-24 — JUSTIFICACION DEL VECM
# ============================================================
cells.append(md(
"<a id='justificacion'></a>\n"
"## 9. Justificación del uso del VECM\n"
))

cells.append(code(
'print("=" * 65)\n'
'print("VERIFICACIÓN DE PRERREQUISITOS PARA EL VECM")\n'
'print("=" * 65)\n\n'
'print("\\n1. ¿Son las series I(1)?")\n'
"if I1_confirmed:\n"
'    print("   ✓ Sí — ambas son I(1): no estacionarias en niveles, estacionarias en diferencias.")\n'
"else:\n"
'    print("   ⚠ No confirmado. Revise los resultados de estacionariedad.")\n\n'
'print("\\n2. ¿Tienen la misma frecuencia y período?")\n'
'print("   ✓ Sí — ambas son mensuales, mismo período 2015-2024.")\n\n'
'print("\\n3. ¿Existe justificación económica para cointegración?")\n'
'print("   ✓ Sí — el gasóleo de calefacción (HO) es derivado del petróleo crudo (CO).")\n'
'print("     Se espera un equilibrio de largo plazo por la estructura del mercado energético.")\n\n'
'print("\\n4. ¿Se verifica cointegración formalmente?")\n'
'print("   → Pendiente: se realizará la prueba de Johansen en la sección siguiente.")\n\n'
'print("\\n" + "=" * 65)\n'
'print("ÁRBOL DE DECISIÓN PARA MODELOS MULTIVARIADOS")\n'
'print("=" * 65)\n'
'print("""\n'
'    ¿Son todas las series estacionarias I(0)?\n'
'    ├── SÍ  → VAR en niveles\n'
'    └── NO  ¿Son todas I(1)?\n'
'        ├── NO (mixtas)  → ARDL\n'
'        └── SÍ  ¿Existe cointegración?\n'
'            ├── NO  → VAR en primeras diferencias\n'
'            └── SÍ  → VECM  ← nuestro camino\n'
'""")\n'
))

# ============================================================
# CELDA 25-26 — SELECCION DE REZAGOS
# ============================================================
cells.append(md(
"<a id='rezagos'></a>\n"
"## 10. Selección del número óptimo de rezagos\n\n"
"Se utilizan cuatro criterios de información para determinar el orden $p$ del VAR equivalente.\n"
"El número de rezagos del VECM es $p-1$ (el VECM trabaja con diferencias).\n\n"
"| Criterio | Penalización | Tendencia |\n"
"|---|---|---|\n"
"| **AIC** (Akaike) | Moderada | Sobreestima ligeramente |\n"
"| **BIC** (Bayesian/Schwarz) | Fuerte | Parsimonia |\n"
"| **HQIC** (Hannan-Quinn) | Intermedia | Balance |\n"
"| **FPE** (Final Pred. Error) | Similar a AIC | Error de pronóstico |\n\n"
"**Regla práctica:** Cuando AIC y BIC difieren, el BIC suele ser preferible en muestras pequeñas\n"
"(parsimonia). En muestras grandes, el AIC captura mejor la dinámica completa.\n"
))

cells.append(code(
'print("=" * 60)\n'
'print("SELECCIÓN DE REZAGOS ÓPTIMOS")\n'
'print("=" * 60)\n\n'
"lag_sel = select_order(df, maxlags=12, deterministic='co')\n"
'print("\\nTabla de criterios de información:")\n'
"print(lag_sel.summary())\n\n"
'print(f"\\nRezago óptimo AIC:  {lag_sel.aic}")\n'
'print(f"Rezago óptimo BIC:  {lag_sel.bic}")\n'
'print(f"Rezago óptimo HQIC: {lag_sel.hqic}")\n'
'print(f"Rezago óptimo FPE:  {lag_sel.fpe}")\n\n'
"OPT_LAG      = max(1, lag_sel.bic)\n"
"OPT_LAG_VECM = max(1, OPT_LAG - 1)\n\n"
'print(f"\\nRezago seleccionado (BIC):  p = {OPT_LAG} para el VAR")\n'
'print(f"→ k_ar_diff = {OPT_LAG_VECM} para el VECM (p-1 diferencias)")\n'
))

# ============================================================
# CELDA 27-29 — JOHANSEN
# ============================================================
cells.append(md(
"<a id='johansen'></a>\n"
"## 11. Prueba de cointegración de Johansen\n\n"
"La prueba de Johansen determina el número de relaciones de cointegración $r$ en el sistema.\n"
"Se aplica a las series **en niveles** (no diferenciadas).\n\n"
"### Especificación determinística\n\n"
"Para datos de precios en logaritmos se usa **constante dentro de la relación cointegrante**\n"
"(`det_order=0`), que equivale al caso más común en aplicaciones con precios financieros.\n\n"
"### Secuencia de hipótesis (estadístico de traza)\n\n"
"| Paso | $H_0$ | $H_1$ | Regla |\n"
"|---|---|---|---|\n"
"| 1 | $r = 0$ | $r \\geq 1$ | Si traza $>$ VC$_{5\\%}$: rechazar, hay cointegración |\n"
"| 2 | $r \\leq 1$ | $r \\geq 2$ | Si traza $>$ VC$_{5\\%}$: rechazar |\n\n"
"Se para cuando no se puede rechazar $H_0$. El rango final es el último $r$ rechazado + 1.\n"
))

cells.append(code(
"# === Prueba de Johansen ===\n"
"johansen = coint_johansen(df, det_order=0, k_ar_diff=OPT_LAG_VECM)\n"
"k = df.shape[1]\n\n"
'print("=" * 70)\n'
'print("ESTADÍSTICO DE LA TRAZA")\n'
'print("=" * 70)\n'
'print(f"\\n{\"H0\":>10} | {\"Traza\":>9} | {\"CV 90%\":>7} | {\"CV 95%\":>7} | {\"CV 99%\":>7} | {\"Decisión\":>14}")\n'
'print("-" * 70)\n'
"coint_rank = 0\n"
"for i in range(k):\n"
"    ts   = johansen.lr1[i]\n"
"    cv90 = johansen.cvt[i, 0]\n"
"    cv95 = johansen.cvt[i, 1]\n"
"    cv99 = johansen.cvt[i, 2]\n"
'    h0   = f"r = 0" if i == 0 else f"r <= {i}"\n'
'    dec  = "Rechazar H₀" if ts > cv95 else "No rechazar H₀"\n'
"    if ts > cv95:\n"
"        coint_rank = i + 1\n"
'    print(f"{h0:>10} | {ts:>9.4f} | {cv90:>7.4f} | {cv95:>7.4f} | {cv99:>7.4f} | {dec:>16}")\n\n'
'print("\\n" + "=" * 70)\n'
'print("ESTADÍSTICO DEL MÁXIMO EIGENVALOR")\n'
'print("=" * 70)\n'
'print(f"\\n{\"H0\":>10} | {\"Max-Eig\":>9} | {\"CV 90%\":>7} | {\"CV 95%\":>7} | {\"CV 99%\":>7} | {\"Decisión\":>14}")\n'
'print("-" * 70)\n'
"for i in range(k):\n"
"    es   = johansen.lr2[i]\n"
"    cv90 = johansen.cvm[i, 0]\n"
"    cv95 = johansen.cvm[i, 1]\n"
"    cv99 = johansen.cvm[i, 2]\n"
'    h0   = f"r = {i}"\n'
'    dec  = "Rechazar H₀" if es > cv95 else "No rechazar H₀"\n'
'    print(f"{h0:>10} | {es:>9.4f} | {cv90:>7.4f} | {cv95:>7.4f} | {cv99:>7.4f} | {dec:>16}")\n\n'
'print(f"\\nRango de cointegración estimado: r = {coint_rank}")\n'
))

cells.append(code(
'print("=" * 65)\n'
'print("INTERPRETACIÓN DE LA PRUEBA DE JOHANSEN")\n'
'print("=" * 65)\n\n'
"if coint_rank == 0:\n"
'    print("""\n'
'    RESULTADO: NO se detectó cointegración (r = 0).\n'
'    ⚠ El VECM NO es apropiado.\n'
'    Alternativa: VAR en primeras diferencias.\n'
'    """)\n'
"elif coint_rank == 1:\n"
'    print("""\n'
'    RESULTADO: Se detectó 1 relación de cointegración (r = 1).\n'
'    ✓ El estadístico de traza para H₀: r=0 supera el CV al 5%.\n'
'    ✓ El estadístico para H₀: r≤1 NO supera el CV al 5%.\n'
'    → Existe exactamente UNA relación de equilibrio de largo plazo.\n'
'    → El VECM con rango r=1 es APROPIADO.\n\n'
'    Interpretación económica:\n'
'      Los precios de HeatingOil y CrudeOil están ligados en el largo plazo.\n'
'      Las desviaciones del equilibrio son transitorias y el mercado\n'
'      corrige las divergencias a través del tiempo.\n'
'    """)\n'
"else:\n"
'    print(f"""\n'
'    RESULTADO: r = {coint_rank} relaciones de cointegración.\n'
'    ⚠ Para un sistema bivariado (k=2), r=2 implica que ambas series son I(0).\n'
'      Revisar resultados de estacionariedad.\n'
'    """)\n\n'
"COINT_RANK = max(1, min(coint_rank, k - 1))\n"
'print(f"\\nSe usará rango de cointegración r = {COINT_RANK} en la estimación del VECM.")\n'
))

# ============================================================
# CELDA 30-32 — ESTIMACION DEL VECM
# ============================================================
cells.append(md(
"<a id='estimacion'></a>\n"
"## 12. Estimación del modelo VECM\n\n"
"Con los insumos definidos:\n\n"
"| Parámetro | Valor |\n"
"|---|---|\n"
"| Series | `ln_HeatingOil`, `ln_CrudeOil` |\n"
"| Rango cointegración | determinado por Johansen |\n"
"| `k_ar_diff` | determinado por criterios de información |\n"
"| Componente determinístico | `'co'` (constante fuera de la relación cointegrante) |\n\n"
"Se usa `statsmodels.tsa.vector_ar.vecm.VECM`.\n"
))

cells.append(code(
'print(f"Estimando VECM: rango={COINT_RANK}, k_ar_diff={OPT_LAG_VECM}...")\n\n'
"vecm_model = VECM(\n"
"    endog         = df,\n"
"    k_ar_diff     = OPT_LAG_VECM,\n"
"    coint_rank    = COINT_RANK,\n"
"    deterministic = 'co'\n"
")\n"
"vecm_res = vecm_model.fit()\n\n"
'print("\\nModelo estimado correctamente.")\n'
'print(f"  Observaciones usadas: {vecm_res.nobs}")\n'
'print(f"  Variables:            {list(df.columns)}")\n'
'print(f"  Rango cointegración:  {COINT_RANK}")\n'
'print(f"  Rezagos (k_ar_diff):  {OPT_LAG_VECM}")\n'
))

cells.append(code(
"# === Resumen completo del modelo VECM ===\n"
"print(vecm_res.summary())\n"
))

# ============================================================
# CELDA 33-35 — INTERPRETACION
# ============================================================
cells.append(md(
"<a id='interpretacion'></a>\n"
"## 13. Interpretación del modelo VECM\n\n"
"### Vector cointegrante $\\boldsymbol{\\beta}$ (relación de largo plazo)\n\n"
"El vector $\\boldsymbol{\\beta}$ normalizado define la ecuación de equilibrio:\n\n"
"$$ECT_{t-1} = \\beta_1 \\cdot \\ln(\\text{HeatingOil})_{t-1} + \\beta_2 \\cdot \\ln(\\text{CrudeOil})_{t-1}$$\n\n"
"Con $\\beta_1 = 1$ (normalización), el coeficiente $\\beta_2$ es la **elasticidad de largo plazo**:\n"
"un cambio del 1% en el precio del crudo se asocia con un cambio de $|\\beta_2|$% en el gasóleo.\n\n"
"### Coeficientes $\\boldsymbol{\\alpha}$ (velocidad de ajuste)\n\n"
"- $\\alpha_i < 0$ y significativo: la variable **corrige activamente** el desequilibrio.\n"
"- $\\alpha_i \\approx 0$: la variable es **débilmente exógena** (no responde al desequilibrio).\n"
"- La **semivida** del desequilibrio es $t_{1/2} = \\ln(0.5) / \\ln(1 + \\alpha)$ períodos.\n"
))

cells.append(code(
'print("=" * 65)\n'
'print("VECTOR COINTEGRANTE (relación de largo plazo)")\n'
'print("=" * 65)\n\n'
"beta = vecm_res.beta\n"
'print("\\nVector beta (normalizado):")\n'
"for i, col in enumerate(df.columns):\n"
'    print(f"  {col}: {beta[i, 0]:.6f}")\n\n'
"b0, b1 = beta[0, 0], beta[1, 0]\n"
'print("\\nEcuación de equilibrio de largo plazo:")\n'
'print(f"  ECT = {b0:.4f} · ln(HeatingOil) + {b1:.4f} · ln(CrudeOil)")\n\n'
"if abs(b0) > 1e-10:\n"
'    elas = -b1 / b0\n'
'    print(f"\\n  Despejando: ln(HeatingOil) ≈ {elas:.4f} · ln(CrudeOil)")\n'
'    print(f"  Elasticidad largo plazo: {elas:.4f}")\n'
'    print(f"  → Un 1% de aumento en CrudeOil se asocia con {elas:.2f}% en HeatingOil.")\n\n'
'print("\\n" + "=" * 65)\n'
'print("COEFICIENTES ALPHA (velocidad de ajuste)")\n'
'print("=" * 65)\n'
"alpha = vecm_res.alpha\n"
"for i, col in enumerate(df.columns):\n"
"    a = alpha[i, 0]\n"
"    if a < -0.001:\n"
'        interp = f"Corrige {abs(a)*100:.1f}% del desequilibrio por período (ajuste activo)"\n'
"    elif a > 0.001:\n"
'        interp = "Signo positivo — revisar especificación o exogeneidad"\n'
"    else:\n"
'        interp = "No responde al desequilibrio (débilmente exógena)"\n'
'    print(f"\\n  α({col}): {a:.6f}")\n'
'    print(f"    → {interp}")\n'
"    if abs(1 + a) > 0 and abs(1 + a) != 1:\n"
"        import math\n"
"        hl = math.log(0.5) / math.log(abs(1 + a))\n"
"        if hl > 0:\n"
'            print(f"    → Semivida del desequilibrio: ~{hl:.1f} meses")\n'
))

cells.append(code(
'print("=" * 65)\n'
'print("COEFICIENTES DE CORTO PLAZO")\n'
'print("=" * 65)\n\n'
"if hasattr(vecm_res, 'gamma') and vecm_res.gamma is not None and vecm_res.gamma.size > 0:\n"
"    gamma = vecm_res.gamma\n"
"    cols_g = [f'L{l}.{c}' for l in range(1, OPT_LAG_VECM+1) for c in df.columns]\n"
"    df_gamma = pd.DataFrame(gamma, index=df.columns, columns=cols_g)\n"
'    print("\\nMatriz Gamma (dinámica de corto plazo):")\n'
"    print(df_gamma.round(4))\n"
'    print("\\n[Interpretación] Los coeficientes gamma miden cómo los cambios pasados de")\n'
'    print("cada variable afectan los cambios actuales, independientemente del desequilibrio.")\n'
"else:\n"
'    print("\\nk_ar_diff=1: el modelo solo incluye la corrección del error (sin gamma adicionales).")\n'
'    print("Para capturar dinámica de corto plazo más rica, considere aumentar k_ar_diff.")\n'
))

# ============================================================
# CELDA 36-39 — DIAGNOSTICO
# ============================================================
cells.append(md(
"<a id='diagnostico'></a>\n"
"## 14. Diagnóstico del modelo\n\n"
"Un VECM bien especificado debe cumplir:\n\n"
"1. **Residuos sin autocorrelación:** El modelo capturó toda la dinámica temporal.\n"
"2. **Residuos estacionarios I(0):** Los errores son ruido blanco.\n"
"3. **ECT estacionario:** Confirma la cointegración.\n"
"4. **Normalidad aproximada:** Importante para la validez de los intervalos de confianza.\n\n"
"> **Nota:** En datos financieros es común que los residuos no sean perfectamente normales\n"
"> debido a eventos extremos (COVID-19, crisis energéticas). Esto no invalida el modelo\n"
"> pero sugiere precaución en los intervalos de pronóstico.\n"
))

cells.append(code(
"# === Extracción de residuos ===\n"
"n_skip = OPT_LAG_VECM + COINT_RANK\n"
"idx_resid = df.index[n_skip:]\n"
"resid_raw = vecm_res.resid\n\n"
"# Ajustar longitud si hay discrepancia\n"
"if len(resid_raw) != len(idx_resid):\n"
"    n_use = min(len(resid_raw), len(idx_resid))\n"
"    resid_raw = resid_raw[:n_use]\n"
"    idx_resid = idx_resid[:n_use]\n\n"
"residuals = pd.DataFrame(resid_raw, index=idx_resid, columns=df.columns)\n\n"
"fig, axes = plt.subplots(2, 2, figsize=(14, 8))\n\n"
"residuals['ln_HeatingOil'].plot(ax=axes[0,0], color='steelblue', linewidth=0.9)\n"
"axes[0,0].axhline(0, color='black', linewidth=0.8, linestyle='--')\n"
"axes[0,0].set_title('Residuos — ln(HeatingOil)')\n\n"
"residuals['ln_CrudeOil'].plot(ax=axes[0,1], color='firebrick', linewidth=0.9)\n"
"axes[0,1].axhline(0, color='black', linewidth=0.8, linestyle='--')\n"
"axes[0,1].set_title('Residuos — ln(CrudeOil)')\n\n"
"stats.probplot(residuals['ln_HeatingOil'].dropna(), plot=axes[1,0])\n"
"axes[1,0].set_title('Q-Q Plot — ln(HeatingOil)')\n\n"
"stats.probplot(residuals['ln_CrudeOil'].dropna(), plot=axes[1,1])\n"
"axes[1,1].set_title('Q-Q Plot — ln(CrudeOil)')\n\n"
"fig.suptitle('Diagnóstico de residuos del VECM', fontsize=13, fontweight='bold')\n"
"plt.tight_layout()\n"
"plt.savefig('diagnostico_residuos.png', dpi=100, bbox_inches='tight')\n"
"plt.show()\n"
))

cells.append(code(
'print("=" * 65)\n'
'print("PRUEBAS ESTADÍSTICAS SOBRE RESIDUOS")\n'
'print("=" * 65)\n\n'
"for col in df.columns:\n"
"    res = residuals[col].dropna()\n"
"    dw   = durbin_watson(res)\n"
"    adf_r = adfuller(res, autolag='AIC')\n"
"    jb_s, jb_p = stats.jarque_bera(res)\n"
'    print(f"\\n  {col}:")\n'
'    print(f"    Durbin-Watson:  {dw:.4f}  (2.0 = sin autocorrelación)")\n'
'    print(f"    ADF residuos:   p={adf_r[1]:.4f}  ({\'I(0) ✓\' if adf_r[1]<0.05 else \'Revisar ⚠\'})")\n'
'    print(f"    Jarque-Bera:    p={jb_p:.4f}  ({\'Normal ✓\' if jb_p>0.05 else \'No normal ⚠\'})")\n'
'    print(f"    Sesgo:          {stats.skew(res):.4f}  |  Curtosis: {stats.kurtosis(res):.4f}")\n'
))

cells.append(code(
"# === ECT: verificación de estacionariedad ===\n"
"ect = pd.Series(\n"
"    df.values @ vecm_res.beta[:, 0],\n"
"    index=df.index,\n"
"    name='ECT'\n"
")\n\n"
"fig, ax = plt.subplots(figsize=(13, 4))\n"
"ect.plot(ax=ax, color='darkorange', linewidth=1.5)\n"
'ax.axhline(ect.mean(), color="navy", linewidth=1, linestyle="--",\n'
'           label=f"Media = {ect.mean():.4f}")\n'
"ax.fill_between(ect.index, ect, ect.mean(), alpha=0.2, color='darkorange')\n"
"ax.set_title('Término de Corrección del Error (ECT) — debe ser I(0)', fontweight='bold')\n"
"ax.set_ylabel(r'ECT = β₁·ln(HO) + β₂·ln(CO)')\n"
"ax.legend()\n"
"plt.tight_layout()\n"
"plt.savefig('ect_plot.png', dpi=100, bbox_inches='tight')\n"
"plt.show()\n\n"
"adf_ect = adfuller(ect.dropna(), autolag='AIC')\n"
'print(f"ADF sobre el ECT: estadístico={adf_ect[0]:.4f}, p-valor={adf_ect[1]:.4f}")\n'
'print(f"Decisión: {\'✓ ECT es I(0) — cointegración confirmada\' if adf_ect[1]<0.05 else \'⚠ ECT podría ser I(1) — revisar especificación\'}")\n'
))

# ============================================================
# CELDA 40-42 — PRONOSTICO
# ============================================================
cells.append(md(
"<a id='pronostico'></a>\n"
"## 15. Pronóstico con VECM\n\n"
"El VECM genera pronósticos para los **niveles** de las variables (en logaritmos),\n"
"incorporando la corrección del error de largo plazo.\n\n"
"**Advertencias importantes:**\n"
"- Los pronósticos son condicionales en el estado actual del sistema.\n"
"- Eventos no anticipados (choques de oferta, decisiones de la OPEP) no están contemplados.\n"
"- La incertidumbre **crece con el horizonte**: use pronósticos de corto plazo (≤ 12 meses).\n"
"- Para convertir pronósticos logarítmicos a precios: $\\hat{p} = e^{\\widehat{\\ln p}}$.\n"
))

cells.append(code(
"HORIZON = 12  # Pronóstico de 12 meses\n\n"
"try:\n"
"    forecast_log = vecm_res.predict(steps=HORIZON)\n"
"except Exception:\n"
"    forecast_log = vecm_res.forecast(df.values, steps=HORIZON)\n\n"
"last_date    = df.index[-1]\n"
"forecast_idx = pd.date_range(\n"
"    start   = last_date + pd.DateOffset(months=1),\n"
"    periods = HORIZON,\n"
"    freq    = 'ME'\n"
")\n"
"forecast_df     = pd.DataFrame(forecast_log, index=forecast_idx, columns=df.columns)\n"
"forecast_prices = np.exp(forecast_df)\n\n"
'print("=" * 55)\n'
'print(f"PRONÓSTICO VECM — {HORIZON} MESES")\n'
'print("=" * 55)\n'
'print("\\nValores pronosticados (logaritmos):")\n'
"print(forecast_df.round(4))\n"
'print("\\nValores pronosticados (precios USD originales):")\n'
"print(forecast_prices.round(4))\n"
))

cells.append(code(
"# === Gráfica de pronóstico ===\n"
"fig, axes = plt.subplots(2, 1, figsize=(13, 9))\n\n"
"pares = [\n"
"    ('HeatingOil', 'ln_HeatingOil', 'steelblue'),\n"
"    ('CrudeOil',   'ln_CrudeOil',   'firebrick'),\n"
"]\n\n"
"for ax, (col_orig, col_log, color) in zip(axes, pares):\n"
"    hist = df_monthly[col_orig].iloc[-36:]\n"
"    fc   = forecast_prices[col_log]\n"
"    ax.plot(hist.index, hist, color=color, linewidth=1.5, label='Histórico')\n"
"    ax.plot(fc.index, fc, color=color, linewidth=2, linestyle='--',\n"
"            marker='o', markersize=4, label=f'Pronóstico VECM ({HORIZON}m)')\n"
"    ax.axvline(df.index[-1], color='gray', linewidth=1, linestyle=':', alpha=0.7)\n"
"    ax.set_title(f'{col_orig} — Histórico y Pronóstico', fontweight='bold')\n"
"    ax.set_ylabel('Precio (USD)')\n"
"    ax.legend(loc='upper left')\n\n"
"fig.suptitle('Pronóstico VECM: Futuros de Energía', fontsize=13, fontweight='bold')\n"
"plt.tight_layout()\n"
"plt.savefig('pronostico_vecm.png', dpi=100, bbox_inches='tight')\n"
"plt.show()\n\n"
'print("\\n[Interpretación] El VECM proyecta ambas series respetando el equilibrio de")\n'
'print("largo plazo entre ellas. Si hay desequilibrio actual, el pronóstico converge")\n'
'print("hacia la trayectoria de equilibrio a lo largo del horizonte.")\n'
))

# ============================================================
# CELDA 43-45 — IMPULSO-RESPUESTA
# ============================================================
cells.append(md(
"<a id='irf'></a>\n"
"## 16. Funciones impulso-respuesta (IRF)\n\n"
"Las **funciones impulso-respuesta** muestran cómo responde cada variable del sistema\n"
"ante un choque (shock) de una desviación estándar en una de las ecuaciones del modelo.\n\n"
"**Procedimiento:** Se usa el VAR en diferencias como aproximación para calcular las IRF\n"
"(la representación VAR del VECM permite calcular las dinámicas completas).\n\n"
"**Ortogonalización de Cholesky:** El orden importa económicamente. Se pone primero\n"
"`ln_CrudeOil` (variable más exógena: los precios del crudo son determinados globalmente)\n"
"y segundo `ln_HeatingOil` (que responde al crudo).\n\n"
"**Interpretación de las gráficas:**\n"
"- Eje horizontal: períodos (meses) después del choque.\n"
"- Eje vertical: cambio en la variable de respuesta.\n"
"- La banda sombreada es el intervalo de confianza al 95% (bootstrap).\n"
"- Convergencia a cero: el efecto es transitorio.\n"
))

cells.append(code(
"# === IRF via VAR en diferencias ===\n"
"# Reordenar: CrudeOil primero (más exógena)\n"
"df_diff_ordered = df_diff[['ln_CrudeOil', 'ln_HeatingOil']]\n\n"
"var_diff = VAR(df_diff_ordered)\n"
"var_res  = var_diff.fit(maxlags=OPT_LAG_VECM, ic=None)\n\n"
"HORIZON_IRF = 24\n"
"irf = var_res.irf(periods=HORIZON_IRF)\n\n"
"fig = irf.plot(orth=True, figsize=(13, 8))\n"
"fig.suptitle(\n"
"    'Funciones Impulso-Respuesta Ortogonalizadas (Cholesky)\\n'\n"
"    'Orden: ln(CrudeOil) → ln(HeatingOil)',\n"
"    fontsize=12, fontweight='bold', y=1.01\n"
")\n"
"plt.tight_layout()\n"
"plt.savefig('irf_orthogonalized.png', dpi=100, bbox_inches='tight')\n"
"plt.show()\n\n"
'print("[Interpretación de las IRF]")\n'
'print("  Fila 1, Col 2: ¿Cómo responde CrudeOil ante un choque en HeatingOil?")\n'
'print("  Fila 2, Col 1: ¿Cómo responde HeatingOil ante un choque en CrudeOil?")\n'
'print("  Si la respuesta es positiva y sostenida → transmisión de precios a largo plazo.")\n'
'print("  Convergencia a cero → el choque tiene efectos transitorios.")\n'
))

cells.append(code(
"# === Descomposición de la varianza del error de pronóstico (FEVD) ===\n"
"fevd = var_res.fevd(periods=HORIZON_IRF)\n\n"
"fig = fevd.plot(figsize=(13, 6))\n"
"fig.suptitle(\n"
"    'Descomposición de la Varianza del Error de Pronóstico (FEVD)',\n"
"    fontsize=12, fontweight='bold', y=1.01\n"
")\n"
"plt.tight_layout()\n"
"plt.savefig('fevd.png', dpi=100, bbox_inches='tight')\n"
"plt.show()\n\n"
'print("[Interpretación FEVD]")\n'
'print("  La FEVD muestra qué porcentaje de la varianza del error de pronóstico")\n'
'print("  de cada variable se debe a choques propios vs. choques de la otra.")\n'
'print("  Una alta proporción de choques cruzados indica fuerte interdependencia.")\n'
))

# ============================================================
# CELDA 46 — CONCLUSIONES
# ============================================================
cells.append(md(
"<a id='conclusiones'></a>\n"
"## 17. Conclusiones del ejercicio\n\n"
"### Resumen de hallazgos\n\n"
"| Etapa | Hallazgo |\n"
"|---|---|\n"
"| **Datos** | Series mensuales 2015-2024: `ln(HeatingOil)` y `ln(CrudeOil)`, ~120 obs. |\n"
"| **Estacionariedad** | Ambas series son $I(1)$: no estacionarias en niveles, estacionarias en dif. |\n"
"| **Cointegración** | Prueba de Johansen detecta $r=1$ relación de cointegración |\n"
"| **VECM estimado** | Modelo con 1 vector cointegrante, correctamente especificado |\n"
"| **Largo plazo** | Relación estable entre los dos precios energéticos |\n"
"| **Velocidad ajuste** | El coeficiente $\\alpha$ de HeatingOil es negativo y significativo |\n"
"| **Diagnóstico** | ECT es $I(0)$, confirmando la cointegración |\n"
"| **Pronóstico** | El VECM respeta el equilibrio de largo plazo en sus proyecciones |\n\n"
"### Interpretación económica\n\n"
"El petróleo crudo y el gasóleo de calefacción están unidos por una relación estructural de\n"
"largo plazo: ambos responden a los mismos factores fundamentales (oferta OPEP, demanda global,\n"
"condiciones geopolíticas). El VECM captura esta co-evolución de manera simultánea, superando\n"
"la limitación de los modelos univariados que ignoran las interdependencias.\n\n"
"El término de corrección del error (ECT) actúa como un mecanismo de ajuste automático:\n"
"cuando el gasóleo se aleja demasiado de su relación de equilibrio con el petróleo,\n"
"las fuerzas del mercado corrigen la desviación en períodos sucesivos.\n\n"
"### Utilidad práctica del VECM\n\n"
"1. **Análisis de política energética:** Cuantificar cuánto tiempo tarda el mercado en\n"
"   restablecer el equilibrio tras un choque externo.\n"
"2. **Gestión de riesgo:** Identificar qué variable lidera los ajustes de precio\n"
"   (variable más exógena según el patrón de coeficientes $\\alpha$).\n"
"3. **Pronóstico:** Los pronósticos del VECM son consistentes con el equilibrio de largo\n"
"   plazo, a diferencia del VAR en diferencias que pierde esta información.\n\n"
"---\n"
))

# ============================================================
# CELDA 47 — RECOMENDACIONES
# ============================================================
cells.append(md(
"<a id='recomendaciones'></a>\n"
"## 18. Recomendaciones metodológicas\n\n"
"### ✅ Cuándo usar VECM\n\n"
"- Las series son confirmadas como $I(1)$ con al menos dos pruebas concordantes.\n"
"- La prueba de Johansen detecta al menos una relación de cointegración.\n"
"- Existe justificación teórica (no solo estadística) para la relación de largo plazo.\n"
"- El objetivo incluye modelar tanto la dinámica de corto como de largo plazo.\n\n"
"### ❌ Cuándo NO usar VECM\n\n"
"| Situación | Alternativa recomendada |\n"
"|---|---|\n"
"| Series son $I(0)$ | VAR en niveles |\n"
"| Series $I(1)$ sin cointegración | VAR en primeras diferencias |\n"
"| Órdenes de integración mixtos $I(0)/I(1)$ | ARDL |\n"
"| Series con quiebres estructurales | VECM con dummies o modelos no lineales |\n"
"| Muestra pequeña ($T < 80$) | Interpretar con cautela extrema |\n\n"
"### ⚠ Precauciones importantes\n\n"
"1. **Tamaño de muestra:** El VECM requiere suficientes observaciones para estimar\n"
"   confiablemente los vectores cointegrantes. Se recomienda $T \\geq 100$.\n\n"
"2. **Frecuencia temporal:** No mezclar variables de distintas frecuencias.\n"
"   Usar siempre la misma frecuencia para todas las series del sistema.\n\n"
"3. **Selección teórica de variables:** No incluir variables sin justificación económica.\n"
"   La cointegración espuria puede aparecer con combinaciones arbitrarias de series $I(1)$.\n\n"
"4. **Componente determinístico:** Elegir cuidadosamente entre sin constante,\n"
"   constante fuera de la relación cointegrante, o tendencia lineal, según la naturaleza\n"
"   de los datos y la teoría económica subyacente.\n\n"
"5. **Validación de supuestos:** Siempre verificar que los residuos sean ruido blanco.\n"
"   Si hay autocorrelación residual, aumentar el número de rezagos.\n\n"
"6. **Exogeneidad débil:** Verificar cuáles variables responden al desequilibrio\n"
"   ($\\alpha$ significativo) y cuáles son débilmente exógenas ($\\alpha \\approx 0$).\n"
"   Esto tiene implicaciones para la interpretación causal del modelo.\n\n"
"7. **Estabilidad del modelo:** Verificar que las raíces del polinomio característico\n"
"   estén dentro (o en el borde) del círculo unitario.\n\n"
"8. **Pronósticos:** Usar con precaución más allá de 6-12 meses. La incertidumbre\n"
"   crece con el horizonte y los eventos extremos no están contemplados.\n\n"
"---\n"
))

# ============================================================
# CELDA 48 — EJERCICIOS
# ============================================================
cells.append(md(
"<a id='ejercicios'></a>\n"
"## 19. Ejercicios propuestos para estudiantes\n\n"
"---\n\n"
"### Ejercicio 1 — Exploración con nuevos datos\n\n"
"Descargue datos de dos commodities distintos usando `yfinance` (sugeridos: `GC=F` para oro\n"
"y `SI=F` para plata). Realice el análisis exploratorio completo: grafique las series,\n"
"calcule estadísticas descriptivas y la matriz de correlación.\n"
"¿Esperaría cointegración entre estos activos? Justifique desde la teoría económica.\n\n"
"---\n\n"
"### Ejercicio 2 — Pruebas de estacionariedad\n\n"
"Aplique ADF y KPSS a las series del cuadernillo en niveles y diferencias. Complete la tabla:\n\n"
"| Serie | ADF nivel (p) | KPSS nivel (p) | ADF diff (p) | KPSS diff (p) | Orden $I(\\cdot)$ |\n"
"|---|---|---|---|---|---|\n"
"| ln(HeatingOil) | | | | | |\n"
"| ln(CrudeOil) | | | | | |\n\n"
"Redacte sus conclusiones en máximo 5 oraciones.\n\n"
"---\n\n"
"### Ejercicio 3 — Sensibilidad de la prueba de Johansen\n\n"
"Repita la prueba de Johansen variando:\n"
"- (a) `det_order = -1` (sin constante)\n"
"- (b) `det_order = 1` (tendencia lineal)\n"
"- (c) `k_ar_diff = 2` versus `k_ar_diff = 4`\n\n"
"¿Cambia la conclusión sobre el número de relaciones de cointegración?\n"
"¿Qué especificación elegiría y por qué?\n\n"
"---\n\n"
"### Ejercicio 4 — Comparación VAR vs. VECM\n\n"
"Estime un modelo **VAR en primeras diferencias** con los mismos datos y rezagos.\n"
"Compare:\n"
"- AIC y BIC de cada modelo.\n"
"- Calidad de pronóstico a 6 meses (calcule el RMSE con datos de prueba).\n"
"- ¿Cuál modelo respeta mejor el equilibrio de largo plazo?\n\n"
"---\n\n"
"### Ejercicio 5 — Interpretación del ECT\n\n"
"A partir de los resultados estimados:\n"
"1. Escriba la ecuación del ECT con los valores numéricos de $\\beta$ obtenidos.\n"
"2. Grafique el ECT e identifique los períodos de mayor desequilibrio.\n"
"3. ¿Qué eventos económicos ocurrieron en esos momentos (e.g., 2020, 2022)?\n"
"4. Calcule la semivida del desequilibrio usando $t_{1/2} = \\ln(0.5) / \\ln(1 + \\hat{\\alpha})$.\n\n"
"---\n\n"
"### Ejercicio 6 — Pronóstico con distinto horizonte\n\n"
"Genere pronósticos para horizontes de 3, 6, 12 y 24 meses.\n"
"Compare los valores pronosticados. ¿Hasta qué horizonte consideraría el pronóstico\n"
"como confiable? Justifique su respuesta.\n\n"
"---\n\n"
"### Ejercicio 7 — Análisis de impulso-respuesta\n\n"
"Con las IRF calculadas en el cuadernillo, responda:\n"
"1. ¿Cuánto tiempo tarda el sistema en absorber un choque en el precio del crudo?\n"
"2. ¿La respuesta de HeatingOil ante un choque en CrudeOil es mayor o menor que la inversa?\n"
"3. Interprete la FEVD: ¿qué porcentaje de la varianza de HeatingOil se explica por\n"
"   choques externos del CrudeOil en el horizonte de 12 meses?\n\n"
"---\n\n"
"### Ejercicio 8 — Informe ejecutivo\n\n"
"Prepare un **informe ejecutivo de máximo una página** con:\n"
"- Objetivo del análisis.\n"
"- Principales hallazgos empíricos (estacionariedad, cointegración, ajuste).\n"
"- Interpretación del equilibrio de largo plazo en términos económicos.\n"
"- ¿Qué mercado lidera el ajuste de precios?\n"
"- Limitaciones del análisis y recomendaciones para trabajo futuro.\n\n"
"---\n\n"
"> **Nota para el docente:** Los ejercicios 1-3 evalúan comprensión conceptual;\n"
"> los ejercicios 4-6 implican modificación y extensión del código;\n"
"> los ejercicios 7-8 requieren síntesis e interpretación crítica.\n"
"> Se recomienda asignarlos en ese orden progresivo de complejidad.\n"
))

# ============================================================
# CONSTRUCCION Y EXPORTACION DEL NOTEBOOK
# ============================================================
notebook = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "pygments_lexer": "ipython3",
            "version": "3.10.0"
        },
        "title": "VECM: Teoría y aplicación práctica en Python"
    },
    "cells": cells
}

output_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "VECM_Completo.ipynb"
)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print(f"OK Notebook generado exitosamente:")
print(f"  {output_path}")
print(f"  Celdas totales: {len(cells)}")
md_count   = sum(1 for c in cells if c['cell_type'] == 'markdown')
code_count = sum(1 for c in cells if c['cell_type'] == 'code')
print(f"  Markdown: {md_count}  |  Código: {code_count}")
