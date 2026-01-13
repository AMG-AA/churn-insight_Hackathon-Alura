# churn-insight_Hackathon-Alura
Sistema que recibe datos de un cliente y comprueba si es probable que cancele el servicio o no.


## Estructura del proyecto / churn-insight_Hackathon-Alura
``` R
📁 main/
├── 01_ETL_hackathon.ipynb
├── 02_Modelado_hackathon.ipynb
└── 03_Optimizacion_modelo_hackathon.ipynb
└── hackathon_model_ready.csv
└── README.md


📁 Deployment/ <=== Carpeta de despliegue con modelo champion y dependencias
├── README.md
├── model_definition.py
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
```
