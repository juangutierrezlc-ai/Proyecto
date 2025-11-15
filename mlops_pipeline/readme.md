# Proyecto Final Machine Learning — Predicción de precios de vehículos

Este proyecto implementa un pipeline completo de MLOps para el análisis, entrenamiento, despliegue y monitoreo de un modelo de machine learning. Está diseñado con modularidad, automatización y buenas prácticas de desarrollo, incluyendo control de versiones, contenedores, calidad de código y documentación. El objetivo principal es construir un sistema reproducible y escalable que permita entender los datos, generar predicciones confiables y monitorear el rendimiento del modelo en producción.

# Estrutura del proyecto 

mlops_pipeline/
├── comprension_eda.ipynb
├── ft_engineering.py
├── model_training.py
├── model_monitoring.py
├── model_deploy.py
├── requirements.txt
├── Dockerfile
├── sonar-project.properties
├── set_up.bat
├── config.json
├── Base_de_datos.csv
├── src/
│   └── (módulos auxiliares)

 # 📊 Exploración de Datos (comprension_eda.ipynb)

El notebook comprension_eda.ipynb realiza un análisis exploratorio detallado sobre la base de datos Base_de_datos.csv. Este análisis incluye la clasificación automática de variables en numéricas y categóricas, la visualización de distribuciones, y la detección de valores atípicos. Se generan histogramas, boxplots y gráficos de barras para entender la frecuencia y comportamiento de cada variable. También se incluye un mapa de calor para visualizar correlaciones entre variables numéricas. Todas las funciones de graficación están modularizadas, validadas para evitar errores, y automatizadas para guardar las imágenes generadas en carpetas específicas para su uso en reportes.

# Ingeniería de Características (ft_engineering.py)

El módulo ft_engineering.py transforma los datos crudos en variables útiles para el modelo. Se encarga de imputar valores faltantes, codificar variables categóricas, escalar variables numéricas y generar nuevas características derivadas. Además, valida la consistencia de los datos y exporta un dataset limpio listo para el entrenamiento. Este paso es clave para mejorar el rendimiento del modelo y garantizar que los datos estén en un formato adecuado para el aprendizaje automático.

# 🤖 Entrenamiento del Modelo (model_training.py)

El script model_training.py entrena un modelo supervisado utilizando técnicas de validación cruzada y selección de hiperparámetros. Se divide el dataset en conjuntos de entrenamiento y prueba, se elige el algoritmo más adecuado (como RandomForest o XGBoost), y se evalúa el rendimiento mediante métricas como accuracy, F1-score o RMSE, según el tipo de problema. El modelo final se guarda en formato .pkl para su posterior despliegue.

# 🚀 Despliegue como API (model_deploy.py)

El archivo model_deploy.py expone el modelo entrenado como un servicio web utilizando FastAPI. Se define un endpoint /predict que permite enviar datos en formato JSON y recibir predicciones en tiempo real. El sistema soporta predicciones por lotes y está preparado para ser contenedorizado mediante Docker. El Dockerfile y el archivo .dockerignore están incluidos para facilitar la construcción de la imagen, y el archivo requirements.txt asegura la reproducibilidad del entorno.

# Monitoreo del Modelo (model_monitoring.py)

El módulo model_monitoring.py permite evaluar el rendimiento del modelo en producción. Compara las predicciones con los valores reales, detecta cambios en la distribución de las variables (drift), y genera alertas si el rendimiento cae por debajo de ciertos umbrales. También incluye visualizaciones que permiten entender cómo está funcionando el modelo en tiempo real, lo cual es esencial para mantener la calidad del sistema en entornos dinámicos.

# 🗃️ Base de Datos (Base_de_datos.csv)

La base de datos utilizada en este proyecto contiene registros de clientes, productos y transacciones. Incluye variables numéricas como edad, ingresos, número de compras y tiempo de permanencia, así como variables categóricas como género, tipo de producto, región y canal de compra. Esta información permite construir modelos que predicen comportamientos, segmentan usuarios o detectan patrones relevantes para la toma de decisiones


# 🧪 Calidad de Código y Automatización

El proyecto incluye análisis de calidad de código mediante SonarCloud, configurado a través del archivo sonar-project.properties. Se evalúan métricas como duplicación, cobertura de pruebas, complejidad y seguridad. Además, se incluye un script set_up.bat que automatiza la instalación de dependencias y la ejecución del análisis. El proyecto está preparado para integrarse con pipelines de CI/CD y se puede extender fácilmente para incluir pruebas unitarias y badges de calidad en el README.md.


# Contenedores y Entorno

El entorno de ejecución está definido mediante Docker, lo que permite desplegar el sistema en cualquier máquina sin preocuparse por incompatibilidades. El archivo config.json gestiona las variables de configuración, y el requirements.txt asegura que todas las dependencias estén correctamente instaladas. Esto facilita la colaboración entre desarrolladores y garantiza la reproducibilidad del proyecto.


# 📈 Descripción de las gráficas en comprension_eda.ipynb

El notebook genera una serie de visualizaciones que permiten comprender la estructura y comportamiento de los datos. Para las variables numéricas, se incluyen histogramas que muestran la distribución de cada variable, permitiendo identificar sesgos, concentraciones y posibles outliers. También se generan boxplots que resaltan valores extremos y la dispersión de los datos. Para las variables categóricas, se presentan gráficos de barras que muestran la frecuencia de cada categoría, facilitando el análisis de dominancia o balance entre clases. Además, se incluye un mapa de calor de correlaciones entre variables numéricas, útil para detectar relaciones lineales que podrían influir en el modelado. Algunas gráficas combinadas permiten comparar variables categóricas con métricas numéricas, como el ingreso promedio por tipo de producto o el número de compras por región. Todas las gráficas se generan mediante funciones modulares que validan los datos antes de graficar y guardan automáticamente los resultados en carpetas organizadas para su uso en reportes.


# Conclusión

Este proyecto representa una implementación completa de un pipeline MLOps, desde la exploración inicial de datos hasta el despliegue y monitoreo de un modelo en producción. Cada componente ha sido diseñado con modularidad, automatización y buenas prácticas de desarrollo, lo que permite escalar el sistema, colaborar con otros desarrolladores y mantener la calidad del código. La base de datos utilizada ofrece un contexto realista para aplicar técnicas de análisis, ingeniería de características y aprendizaje automático. El uso de FastAPI y Docker garantiza que el modelo pueda ser desplegado de forma eficiente, mientras que el monitoreo permite mantener su rendimiento en entornos dinámicos. Además, el análisis de calidad con SonarCloud refuerza el compromiso con la mantenibilidad y la seguridad del código. En conjunto, este proyecto no solo demuestra habilidades técnicas avanzadas, sino también una visión integral de cómo construir soluciones de machine learning robustas y listas para producción.