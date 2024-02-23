# DashBoard CryptoBTC
 
Este proyecto consiste en un Dashboard de seguimiento para la criptomoneda Bitcoin (BTC). Utiliza técnicas de web scraping para recopilar datos en tiempo real, almacenando la información en una base de datos SQL Server. El objetivo principal es proporcionar una interfaz visual a través de Power BI que permita a los usuarios monitorizar y analizar fácilmente la evolución de Bitcoin.

## Estructura del Proyecto
- **`/Scripts`:** Contiene los scripts de web scraping para obtener datos en tiempo real de fuentes relevantes sobre Bitcoin.

- **`/database`:** Aquí se encuentran los archivos relacionados con la configuración de la base de datos SQL Server, incluyendo scripts de creación de tablas.
- -**`DashBoard`:** Archivo PowerBI para visualizacion de datos.

## Configuración

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes herramientas:

- **SQL Server:** Configura una instancia de SQL Server y ajusta la cadena de conexión en los scripts de base de datos según sea necesario.

- **Power BI:** Importa los archivos de Power BI para visualizar el Dashboard.

## Requisitos.
-Python 3.11.
- Librerias: requests, pyodbc.

## Ejecucion.
-Simplemente ejecutar el archivo main.py. (Dentro del archivo de código hay variables que igual interesan cambiar en funcion de las necesidades de cada uno)

## Future work.

Se planea implementar las siguientes caracteristicas:
- **Modelo de Inteligencia Artificial:** Desarrollar un modelo de IA para predecir futuros precios de Bitcoin basándose en datos históricos y parámetros relevantes.

- **Comparativas:** Añadir funcionalidades de comparación al archivo PowerBI para permitir a los usuarios analizar la evolución de Bitcoin en relación con otros activos o indicadores.


