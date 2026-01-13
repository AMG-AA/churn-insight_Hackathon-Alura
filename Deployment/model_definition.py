import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin

class ChurnEnsembleChampion(BaseEstimator, ClassifierMixin):
    """
    Clase para el modelo Champion que integra XGBoost y Random Forest
    con pesos optimizados y manejo de umbral personalizado.
    """
    def __init__(self, xgb_model, rf_model, w_xgb, features_list, threshold=0.5):
        self.xgb_model = xgb_model
        self.rf_model = rf_model
        self.w_xgb = w_xgb
        self.w_rf = 1.0 - w_xgb
        self.features_list = features_list
        self.threshold = threshold

    def predict_proba(self, X):
        # Asegurar que X sea un DataFrame con las columnas correctas
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X, columns=self.features_list)
        
        X_subset = X[self.features_list]
        
        # Obtener probabilidades de ambos modelos
        prob_xgb = self.xgb_model.predict_proba(X_subset)[:, 1]
        prob_rf = self.rf_model.predict_proba(X_subset)[:, 1]
        
        # Combinación lineal ponderada
        avg_prob = (self.w_xgb * prob_xgb) + (self.w_rf * prob_rf)
        return avg_prob

    def predict(self, X):
        probabilities = self.predict_proba(X)
        return (probabilities >= self.threshold).astype(int)