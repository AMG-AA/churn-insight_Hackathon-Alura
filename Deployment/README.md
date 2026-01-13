# 🚀 Churn Prediction Model - Deployment Ready

Este directorio contiene el modelo **Champion** final para la predicción de fuga de clientes, optimizado (Optuna + Optimizacion Bayesiana) mediante ensamble (XGBoost + Random Forest).

## 📦 Componentes
1. `modelo_champion_churn_ensemble.pkl`: Objeto serializado con el modelo y preprocesadores.
2. `model_definition.py`: Clase Wrapper necesaria para reconstruir el modelo.
3. `requirements.txt`: Versiones de software requeridas.

## 🛠️ Instrucciones de Carga
Para integrar este modelo en la API:

```python
import joblib
import pandas as pd
from model_definition import ChurnEnsembleChampion

# Cargar el artefacto
model = joblib.load('modelo_champion_churn_ensemble.pkl')

# Estas son las variables que el modelo espera, junto con su tipo y descripción 6 columnas (contrato):

| Campo                   | Tipo   | Descripción                         | Rango / Valores Permitidos |
|-------------------------|--------|-------------------------------------|----------------------------|
| ingresos_mensuales      | float  | Ingresos mensuales del hogar.       | -6.17 a 1223.38*           |
| cargo_recurrente        | float  | Costo fijo del plan mensual.        | -11.0 a 400.0*             |
| calificacion_crediticia | string | Score de crédito categorizado.      | ['1-Highest', '2-High', '3-Good', '4-Medium', '5-Low', '6-Verylow', '7-Lowest'] |
| llamadas_caidas         | int    | Promedio de llamadas fallidas.      | 0 a 221                    |
| meses_en_servicio       | int    | Antigüedad del contrato.            | 6 a 61 meses               |
| dias_equipo_actual      | int    | Días desde el último equipo.        | -5 a 1812*                 |

```

*Valores atípicos presentes en el conjunto de datos de entrenamiento.
>Para no perder información valiosa, el modelo fue entrenado para procesar estos valores como parte del comportamiento financiero real del cliente

### Especificaciones del Modelo
- Tipo: Ensamble (XGBoost + Random Forest)

**F1-Score**: 0.48

**Recall (Clase 1):** 0.72

**Variables:** 6 variables de contrato.

---
