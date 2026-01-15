# 📉 ChurnInsight – Data Science (Hackathon)

## 1. Descripción del desafío

El desafío **ChurnInsight** consiste en desarrollar una solución de *Data Science* capaz de **predecir si un cliente es propenso a cancelar un servicio (churn)**.

En el contexto del hackathon, el proyecto se divide en dos grandes componentes:
- **Equipo de Data Science**: desarrollo del modelo predictivo de churn.
- **Equipo de Back-end**: construcción de una API que expone la predicción del modelo a otros sistemas.

Este repositorio documenta **exclusivamente el trabajo del equipo de Data Science**, desde la preparación de los datos hasta la optimización y serialización del modelo.

---

## 2. Problema de negocio (visión no técnica)

Las empresas que operan bajo modelos de suscripción o contratos recurrentes enfrentan constantemente el problema de la cancelación de clientes. Retener clientes existentes es significativamente más económico que adquirir nuevos.

La empresa desea **anticiparse a la cancelación**, identificando clientes con alto riesgo de churn para:
- Priorizar acciones de retención.
- Ofrecer beneficios personalizados.
- Actuar de forma preventiva desde soporte o marketing.
- Medir el impacto de estas acciones a lo largo del tiempo.

---

## 3. Validación de mercado

La predicción de churn es una de las aplicaciones más comunes y valiosas de la ciencia de datos en negocios modernos.

Sectores como:
- Telecomunicaciones  
- Bancos digitales y fintech  
- Plataformas de streaming  
- Gimnasios  
- Software SaaS  

utilizan modelos de churn para:
- Reducir pérdidas financieras.
- Comprender patrones de comportamiento.
- Incrementar el *lifetime value* del cliente.

Incluso modelos simples generan valor al permitir enfocar esfuerzos donde el riesgo es mayor.

---

## 4. Objetivo del equipo de Data Science

Desarrollar un **modelo de clasificación binaria** capaz de predecir si un cliente:
- **Va a cancelar**
- **Va a continuar**

a partir de información histórica de uso, contrato y comportamiento, entregando además una **probabilidad asociada a la predicción**.

---

## 5. Dataset

El dataset utilizado contiene información de clientes, incluyendo variables como:
- Tiempo de contrato
- Uso del servicio
- Historial de pagos
- Tipo de plan
- Variables demográficas y de comportamiento

La variable objetivo es binaria e indica si el cliente abandonó el servicio (*churn*).

El volumen de datos fue controlado considerando las limitaciones del **Free Tier de OCI**.

---

## 6. Metodología y estructura del proyecto

El proyecto se desarrolló siguiendo un pipeline clásico de *Machine Learning*, dividido en tres fases principales, cada una documentada en un notebook independiente.

```
📁 notebooks/
 ├── 01_ETL_hackathon.ipynb
 ├── 02_Modelado_hackathon.ipynb
 └── 03_Optimizacion_modelo_hackathon.ipynb
```

---

## 7. Fase 1 – ETL y preparación de datos  
**Notebook:** `01_ETL_hackathon.ipynb`

En esta etapa se realizó el proceso de *Extract, Transform & Load (ETL)* para dejar los datos listos para el entrenamiento del modelo.

### Actividades principales:
- Exploración inicial del dataset (EDA).
- Análisis de tipos de datos y valores faltantes.
- Limpieza y depuración.
- Selección de variables relevantes.
- Preparación del dataset final para modelado.

**Resultado:**  
Un dataset limpio, consistente y adecuado para algoritmos de *Machine Learning*.

---

## 8. Fase 2 – Modelado predictivo  
**Notebook:** `02_Modelado_hackathon.ipynb`

En esta fase se entrenaron distintos modelos de clasificación para establecer una línea base de desempeño.

### Actividades principales:
- Separación de datos en entrenamiento y prueba.
- Entrenamiento de modelos supervisados.
- Comparación de desempeño entre modelos.
- Evaluación considerando el desbalance de clases.

### Métricas utilizadas:
- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC

###  Comparativa final de modelos 

<img width="1384" height="684" alt="image" src="https://github.com/user-attachments/assets/4391d82d-f96d-4ca6-ad29-da4db410d1b9" />

**Resultado:** 

Se identificaron modelos con mejor capacidad predictiva y potencial de mejora.

---

## 9. Fase 3 – Optimización del modelo  
**Notebook:** `03_Optimizacion_modelo_hackathon.ipynb`

En la fase final se buscó mejorar el desempeño del modelo seleccionado.

### Actividades principales:
- Ajuste de hiperparámetros.
- Comparación entre modelos optimizados y no optimizados.
- Análisis del impacto de la optimización en métricas clave.

<img width="980" height="583" alt="image" src="https://github.com/user-attachments/assets/62aab3ba-6522-4eff-ac56-f82d66e281bd" />

## Tabla de comparción de Modelos Final**

| Modelo                                   | Recall (Churn) | Precision | F1-Score | Accuracy |
|------------------------------------------|----------------|-----------|----------|----------|
| Regresión Logística (Full)               | 0.0449         | 0.4632    | 0.0818   | 0.7098   |
| Random Forest (Full)                     | 0.0455         | 0.6091    | 0.0848   | 0.7166   |
| Random Forest (8 Vars - Sugerido)         | 0.6615         | 0.3679    | 0.4728   | 0.5750   |
| Random Forest (6 Vars - Contrato)         | 0.6676         | 0.3655    | 0.4723   | 0.5702   |
| Random Forest (Ranking - Data-Driven)    | 0.6948         | 0.3588    | 0.4733   | 0.5544   |
| XGBoost (6 Vars - Contrato)               | 0.7158         | 0.3584    | 0.4777   | 0.5489   |
| Ensamble (RF + XGBoost)                  | 0.6975         | 0.3584    | 0.4735   | 0.5530   |

**Conclusión:**

El análisis final confirma que XGBoost (6 Vars - Contrato) es el modelo con mejor desempeño en la métrica más crítica para el negocio, el Recall de Churn, maximizando la detección de clientes en riesgo.

El Ensamble (RF + XGBoost) ofrece un rendimiento muy cercano y robusto, con una leve mejora en Accuracy, lo que lo convierte en una alternativa válida si se prioriza estabilidad global.

Por su parte, el Random Forest (6 Vars) sigue siendo un modelo sólido, aunque ligeramente inferior en capacidad de detección de churn frente a las otras dos opciones.

**Resultado:**

Modelo final optimizado, con mejor equilibrio entre rendimiento y capacidad de generalización.

---

## 10. Serialización del modelo

El modelo final y su pipeline fueron **serializados** para permitir su uso fuera del notebook, facilitando la integración con el equipo de Back-end.

Herramientas utilizadas:
- `joblib`
- `pickle`

El modelo puede ser cargado por la API para realizar predicciones en tiempo real.

---

## 11. Alcance del MVP (Data Science)

- Clasificación binaria de churn.
- Predicción acompañada de probabilidad.
- Modelo reproducible y exportable.
- Dataset pequeño y controlado.
- Métricas claras y justificadas.

---

## 12. Stack tecnológico

- **Lenguaje:** Python  
- **Análisis y modelado:** Pandas, NumPy, scikit-learn  
- **Entorno:** Jupyter Notebook / Google Colab  
- **Serialización:** joblib / pickle  
- **Control de versiones:** Git / GitHub  

---

## 13. Estructura de proyecto

📁 main/
├── 01_ETL_hackathon.ipynb
├── 02_Modelado_hackathon.ipynb
└── 03_Optimizacion_modelo_hackathon.ipynb
└── hackathon_model_ready.csv
└── README.md


📁 Deployment/ <=== Carpeta de despliegue con modelo champion y dependencias
├── README.md
├── model_definition.py
├── model_test.py
├── modelo_champion_churn_ensemble.pkl
└── requirements_api.txt

└── 📁 Experimentos/  <=== Queda como evidencia de nuestro avance
    ├── 📁 Limpieza_datos/
    │   ├── 📁 Aaron/
    │   │   └── ETL_hackathon.ipynb
    │   ├── 📁 Cuaderno_analisis/
    │   │   └── Analisis de telecom proyecto hackaton.ipynb
    │   ├── 📁 Dataset_telecom_(cell2cell)/
    │   │   ├── cell2celltrain.csv
    │   │   └── cell2celltrain.csv.zip
    │   ├── 📁 Galia/
    │   │   ├── Base de datos inicial.csv
    │   │   ├── Churn_limpieza_Galia-vs0.ipynb
    │   │   ├── Limpieza_vs1.ipynb
    │   │   ├── Entrenamiento_V2.ipynb
    │   │   ├── dataset_churn_listo_para_entrenar.parquet
    │   │   └── readme.md
    │   ├── 📁 Jhovan/
    │   │   └── Analisis de telecom proyecto hackaton.ipynb
    │   └── 📁 Kevin/
    │       ├── Kevin Cancino 02.ipynb
    │       └── Kevin_Cancino_churn.ipynb
    │
    ├── 📁 Modelo/ 
    │   └── 📁 Aaron_modelo/
    │       ├── 📁 Entrenamiento/
    │       │   ├── Hackathon_modelo_2.1.ipynb
    │       │   ├── Hackathon_modelo_2_2.ipynb
    │       │   ├── hackathon_model_ready.csv
    │       │   └── modelo_churn_6vars_contrato.pkl
    │       └── 📁 Feature_engineering/
    │           └── Hackathon_modelo_2_0.ipynb
    │
    └── 📁 Optimizacion/
        ├── 📁 Aaron/
        │   └── Hackathon_modelo_2_3.ipynb
        ├── 📁 Galia/
        │   └── Hackathon_modelo_2_4.ipynb
        └── 📁 Jhovan/
            └── Hackathon_modelo_2_5.ipynb

---

## 14. Notas finales

Este proyecto fue desarrollado dentro de un **hackathon**, priorizando:

- Buenas prácticas de Data Science.
- Aplicabilidad real al negocio.
- Facilidad de integración con sistemas externos.

El trabajo del equipo de Back-end se documenta en carpeta independiente.

## link de backend: __ __
