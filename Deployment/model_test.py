import joblib
import pandas as pd
import numpy as np
from model_definition import ChurnEnsembleChampion

def test_integration():
    print("Inicializando prueba de carga del Modelo Champion...")

    try: 
        # 1. Cargar el modelo 
        model = joblib.load('modelo_champion_churn_ensemble.pkl')
        
        print("Archivo .pkl cargado correctamente.")

        # 2. Crear un caso de prueba (Dummy Data) basado en las variables de contrato
        # Usar los nombres de las columnas exctas definidas en el contrato.
        test_data = pd.DataFrame([{
            'ingresos_mensuales': 50.58,            # Tipo float
            'cargo_recurrente': 60.0,               # Tipo float
            'calificacion_crediticia': '1-Highest', # Tipo string
            'llamadas_caidas': 15,                  # Tipo int
            'meses_en_servicio': 46,                # Tipo int
            'dias_equipo_actual': 149               # Tipo int
        }])

        # 3. Ejecutar predicciones
        prob = model.predict_proba(test_data)
        clase = model.predict(test_data)

        churn = "Cancelación" if clase[0] == 1 else "No Churn"

        print("\n--- RESULTADOS DE LA PRUEBA ---")
        print(f"Probabilidades de Churn: {prob[0]:.4f}")
        print(f"Predicción de Clase: {clase[0]} (0=No Churn, 1= Cancelación)")
        print(f"El cliente tiene una probabilidad del {prob[0]*100:.2f}% de cancelar el servicio y se predice como: \"{churn}\"")
        print("\n------------------------------")
        print("🚀 ¡El modelo está listo para producción!")
    
    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")

if __name__ == "__main__":
    test_integration()