# 🚀 Churn Prediction Model - Deployment Ready

Este directorio contiene el modelo **Champion** final para la predicción de fuga de clientes, optimizado (Optuna + Optimizacion Bayesiana) mediante ensamble (XGBoost + Random Forest).

## 📦 Componentes
1. `modelo_champion_churn_ensemble.pkl`: Objeto serializado que contiene los modelos entrenados, los pesos del ensamble y los preprocesadores.
2. `model_definition.py`: Clase Wrapper personalizada necesaria para reconstruir la lógica del ensamble al cargar el archivo .pkl
3. `requirements.txt`: Listado de dependencias y versiones de software mínimas para la ejecución.
4. `model_test.py`: Script de validación rápida para verificar la integridad del modelo y las predicciones.

## 🛠️ Instrucciones de Carga
Para integrar este modelo en una API o script de producción:

```python
import joblib
import pandas as pd
from model_definition import ChurnEnsembleChampion

# Cargar el artefacto
model = joblib.load('modelo_champion_churn_ensemble.pkl')
```
## ✅ Validación Rápida
Antes de desplegar, puedes validar que el entorno es correcto ejecutando el script de prueba incluido:

```bash
python model_test.py
```
> Este script cargará el modelo y ejecutará una predicción con datos sintéticos para asegurar que todo funciona correctamente.
---
## 📋 Contrato de Datos (Variables de Entrada)
El modelo espera un **DataFrame** con las siguientes 6 columnas de contrato:

| Campo | Tipo | Descripción | Rango / Valores Permitidos |
|-------|------|-------------|---------------------------|
| ingresos_mensuales | float | Ingresos mensuales del hogar. | -6.17 a 1223.38* |
| cargo_recurrente | float | Costo fijo del plan mensual. | -11.0 a 400.0* |
| calificacion_crediticia | string | Score de crédito categorizado. | ['1-Highest', '2-High', '3-Good', '4-Medium', '5-Low', '6-Verylow', '7-Lowest'] |
| llamadas_caidas | int | Promedio de llamadas fallidas. | 0 a 221 |
| meses_en_servicio | int | Antigüedad del contrato. | 6 a 61 meses |
| dias_equipo_actual | int | Días desde el último equipo. | -5 a 1812* |

>Nota: *Valores atípicos presentes en el conjunto de datos de entrenamiento.
>Para no perder información valiosa, el modelo fue entrenado para procesar estos valores como parte del comportamiento financiero real del cliente

## Especificaciones del Modelo
- **Tipo:** Ensamble Ponderado (XGBoost + Random Forest).
- **F1-Score:** 0.48
- **Recall (Clase 1):** 0.72
- **Variables:** 6 variables de contrato seleccionadas por su alto valor predictivo.

---
