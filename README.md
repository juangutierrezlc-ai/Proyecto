#  📈proyecto_final
Este proyecto correspo de al proyecto final de la materia de ML, el cual tiene como finalidad realizar un modelo de Machine Learning bajo un esquema de MLOps, siguiendo lineamintos de colaboracion y despliegue productivo.

# 🧾Estructura del proyecto
Proyecto/

├── mlops_pipeline/

│   └── src/

│       ├── Cargar_datos.ipynb 

│       ├── comprension_eda.ipynb           # Análisis exploratorio de datos (EDA)

│       ├── ft_engineering.py               # Generación de features y creación de datasets

│       ├── heuristic_model.py              # Modelo heurístico base

│       ├── model_training.ipynb            # Entrenamiento y comparación de modelos

│       ├── model_deploy.ipynb              # Despliegue del modelo en un endpoint

│       ├── model_evaluation.ipynb          # Evaluación de métricas del modelo desplegado

│       └── model_monitoring.ipynb          # Monitoreo y detección de datadrift

│

├── config.json                             # Archivo de configuración del pipeline

├── Base_de_datos.csv                       # Dataset de ejemplo

├── requirements.txt                        # Librerías y dependencias

├── .gitignore                              # Exclusiones de Git

├── readme.md                               # Documentación del proyecto

└── set_up.bat     
