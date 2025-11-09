# Proyecto Final Machine Learning — Predicción de precios de vehículos

## 🎯 Caso de negocio
La empresa busca predecir el precio de venta de vehículos usados para optimizar sus estrategias de compra y venta.

## 📁 Estructura del proyecto
mlops_pipeline/
│
├── __pycache__/                  # Archivos temporales generados por Python
│
├── models/                       # Carpeta para almacenar modelos serializados
│   └── best_model.pkl            # Modelo entrenado y guardado con joblib
│
├── scr/                          # Carpeta principal del código fuente
│   ├── data/
│   │   └── historico.csv         # Datos históricos para monitoreo de drift
│   │
│   ├── models/
│   │   └── best_model.pkl        # Copia del modelo para despliegue
│   │
│   ├── reports/                  # Notebooks con cada etapa del pipeline
│   │   ├── Cargar_datos.ipynb           # Carga y exploración inicial del dataset
│   │   ├── component_eda.ipynb          # Análisis exploratorio con gráficas
│   │   ├── ft_engineering.ipynb         # Ingeniería de características
│   │   ├── heuristic_model.ipynb        # Modelo heurístico base
│   │   ├── model_evaluation.ipynb       # Evaluación de modelos
│   │   ├── model_monitoring.ipynb       # Monitoreo de drift y métricas
│   │   └── model_training.ipynb         # Entrenamiento de modelos supervisados
│
├── .gitignore                    # Archivos y carpetas ignoradas por Git
├── app.py                        # Script alternativo para ejecutar la API
├── Base_de_datos.csv            # Dataset original de precios de vehículos
├── config.json                  # Archivo de configuración del proyecto
├── Dockerfile                   # Instrucciones para construir la imagen Docker
├── model_deploy.py              # Script principal para desplegar el modelo como API
├── readme.md                    # Documentación del proyecto (versión final)
├── requirements.txt             # Lista de dependencias del entorno
├── set_up.bat                   # Script para automatizar construcción y ejecución
└── README.md                    # Documento explicativo del proyecto (duplicado)

## 📊 Principales hallazgos
- Alta correlación entre `Present_Price` y `Selling_Price`
- `Fuel_Type` y `Transmission` influyen en el precio
- El modelo seleccionado fue `GradientBoostingRegressor` con R² de 0.91

## 🔍 Monitoreo
Se implementaron métricas de drift como KS test, PSI, JS divergence y Chi-cuadrado. La app en Streamlit permite visualizar alertas y evolución temporal.

## 🚀 Ejecución
```bash
streamlit run app.py

Este proyecto de Machine Learning tiene como objetivo construir, desplegar y monitorear un modelo supervisado capaz de predecir el precio de vehículos en función de características como año de fabricación, precio actual, kilometraje, tipo de combustible, tipo de vendedor, transmisión y número de propietarios. La estructura del repositorio sigue una arquitectura modular que facilita la integración con pipelines automatizados, el despliegue en contenedores Docker y la exposición del modelo como API mediante FastAPI.

El flujo comienza con el archivo Cargar_datos.ipynb, que permite cargar el dataset original en formato .csv. Este archivo contiene registros de vehículos con múltiples atributos relevantes para la predicción. A continuación, el notebook comprension_eda.ipynb realiza un análisis exploratorio profundo. En esta etapa se generan varias gráficas clave. Los histogramas permiten visualizar la distribución de variables numéricas como Present_Price y Kms_Driven, revelando sesgos hacia valores bajos y la presencia de outliers. Los boxplots complementan esta visión al mostrar la dispersión y los valores extremos, facilitando decisiones sobre limpieza de datos. Los countplots se utilizan para variables categóricas como Fuel_Type, Seller_Type y Transmission, mostrando que la mayoría de los vehículos son de tipo gasolina, vendidos por concesionarios y con transmisión manual. También se genera una matriz de correlación que revela relaciones entre variables numéricas, destacando la fuerte correlación entre Present_Price y Selling_Price, lo cual valida su uso como variable predictora.

El script ft_engineering.py contiene el pipeline de ingeniería de características. Aquí se aplica un ColumnTransformer que combina imputación de valores nulos (SimpleImputer), escalamiento (StandardScaler), codificación one-hot (OneHotEncoder) y codificación ordinal (OrdinalEncoder) según el tipo de variable. Este pipeline transforma los datos en un formato adecuado para el entrenamiento de modelos. El script model_training_evaluation.py entrena múltiples modelos supervisados, incluyendo regresión lineal, árboles de decisión y XGBoost. Se evalúan mediante métricas como MAE, RMSE y R², y se selecciona el mejor modelo con base en su rendimiento. Las gráficas generadas en esta etapa incluyen comparaciones de métricas entre modelos, curvas de predicción vs. valores reales, y visualizaciones de importancia de variables, que permiten interpretar qué atributos influyen más en el precio final.

El archivo model_deploy.py expone el modelo como una API REST utilizando FastAPI. Este script carga el modelo y el preprocesador, define el esquema de entrada mediante Pydantic, y habilita el endpoint /predict, que acepta datos en formato JSON y devuelve predicciones por lotes. La API se ejecuta dentro de un contenedor Docker, construido a partir del Dockerfile, que incluye todas las dependencias necesarias especificadas en requirements.txt. El archivo .dockerignore optimiza el contexto de construcción excluyendo archivos innecesarios. Para facilitar la ejecución, se incluye un script setup.bat que automatiza los pasos de construcción y despliegue. La interfaz Swagger generada por FastAPI permite probar el endpoint de forma interactiva, visualizar los esquemas de entrada y salida, y validar el comportamiento del modelo en tiempo real.

Durante el desarrollo del proyecto se enfrentaron varias dificultades técnicas que enriquecieron el aprendizaje. Una de las principales fue la incompatibilidad entre versiones de scikit-learn al momento de cargar el modelo serializado. El error AttributeError: Can't get attribute '_RemainderColsList' surgió al intentar deserializar objetos entrenados con una versión distinta a la instalada en el contenedor. Esto obligó a revisar cuidadosamente la versión usada en el entrenamiento, ajustar el archivo requirements.txt, y reconstruir el modelo en un entorno limpio para garantizar compatibilidad. Otra dificultad fue la configuración inicial de Docker en Windows, donde el comando docker no era reconocido por el sistema. Esto se resolvió instalando Docker Desktop y asegurando que el daemon estuviera activo. También se presentaron errores al construir la imagen sin especificar correctamente el contexto (.), y al ejecutar el contenedor sin que el modelo estuviera correctamente referenciado en la ruta esperada.

La carpeta src/ contiene todo el código fuente y notebooks del proyecto. Dentro de ella, models/ almacena los objetos serializados del modelo y el preprocesador; data/ guarda el dataset original y los datos históricos para monitoreo; reports/ incluye métricas de drift y visualizaciones generadas; y la raíz del proyecto contiene archivos de configuración como readme.md, requirements.txt, setup.bat y .gitignore. Esta organización modular permite escalar el proyecto, facilitar la colaboración y asegurar reproducibilidad.

En conclusión, este proyecto representa una implementación completa de un flujo MLOps, desde la carga y exploración de datos hasta el despliegue y monitoreo del modelo en producción. Las gráficas generadas en cada etapa no solo enriquecen el análisis, sino que permiten tomar decisiones informadas sobre limpieza, transformación, selección de modelos y mantenimiento. La integración con Docker y FastAPI garantiza que el modelo esté listo para ser consumido por aplicaciones externas, mientras que el monitoreo continuo asegura que su rendimiento se mantenga estable a lo largo del tiempo. Las dificultades enfrentadas durante el desarrollo fortalecieron la comprensión de buenas prácticas en compatibilidad de entornos, gestión de dependencias y despliegue reproducible. Este enfoque metodológico, junto con una documentación clara y modularidad del código, permite que cualquier colaborador pueda entender, reproducir y extender el trabajo realizado.
