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

## 13. Notas finales

Este proyecto fue desarrollado dentro de un **hackathon**, priorizando:
- Claridad metodológica.
- Buenas prácticas de Data Science.
- Aplicabilidad real al negocio.
- Facilidad de integración con sistemas externos.

El trabajo del equipo de Back-end se documenta en un repositorio independiente.
