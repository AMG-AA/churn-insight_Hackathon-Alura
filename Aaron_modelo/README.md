# Churn Insight MVP: Predicción de Bajas en Telecomunicaciones

Este repositorio contiene el desarrollo de un motor de Machine Learning diseñado para identificar proactivamente a clientes con alta probabilidad de cancelar sus servicios. La solución destaca por su **baja latencia** y su capacidad de detección enfocada en el **Recall**.

---

## 🚀 Resumen del Modelo (Model Card)

### 📝 Descripción
El modelo es el resultado de un proceso de optimización que evolucionó desde un análisis exhaustivo de **42 variables** de comportamiento hasta una arquitectura **"Lite"** de alta velocidad. Basado en el algoritmo *Random Forest*, el sistema está optimizado para integrarse en tiempo real con APIs de atención al cliente.

### 🛠️ Contrato de Datos (Input API)
Para garantizar una respuesta inmediata, el modelo de producción utiliza las 6 variables con mayor impacto predictivo:

* `ingresos_mensuales` (float)
* `cargo_recurrente` (float)
* `calificacion_crediticia` (string - ej: '1-Highest')
* `llamadas_caidas` (int)
* `meses_en_servicio` (int)
* `dias_equipo_actual` (int)

### 📊 Rendimiento y Eficiencia
La fase de optimización técnica logró una reducción drástica en los tiempos de respuesta sin degradar la capacidad de detección:

* **Detección (Recall):** **66%** (Identifica 2 de cada 3 fugas reales).
* **Velocidad (Latencia):** **~13 - 16 ms** por petición.
* **Optimización:** Mejora de velocidad superior al **10%** respecto al modelo base mediante sintonización de hilos y profundidad.

---

## ⚙️ Arquitectura Técnica
El modelo se distribuye como un objeto `Pipeline` de Scikit-Learn que encapsula:
1.  **Imputación:** Manejo automático de valores nulos (Mediana / "Unknown").
2.  **Escalado:** Estandarización de rangos mediante `StandardScaler`.
3.  **Codificación:** Transformación de etiquetas de texto vía `OneHotEncoder`.



---

## 📈 Estrategia de Operación (Umbrales)
Se sugieren dos modos de acción según la probabilidad devuelta por la API:

1.  **Estrategia Reactiva (Umbral 0.50):** Máxima cobertura. Ideal para campañas automáticas masivas (SMS/Email) de bajo costo.
2.  **Estrategia Proactiva (Umbral 0.70):** Alta precisión. Recomendado para intervención humana (Agentes de Call Center) o asignación de bonos de retención de alto valor.

---

## 🔬 Estructura del Notebook
El desarrollo sigue una metodología de ingeniería de datos rigurosa:
* **Fase de Experimentación:** Entrenamiento de modelos *Full* (42 variables) y comparación de algoritmos (Regresión Logística vs. Random Forest).
* **Fase de Producción:** Creación de modelos *Lite* (6 y 8 variables) y pruebas de estrés para validación de latencia en milisegundos.

---
**Desarrollado para la Hackathon de Machine Learning - 2024**
