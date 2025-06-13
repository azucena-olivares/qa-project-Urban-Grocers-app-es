Proyecto de Automatización de API Urban Grocers - Creación de Usuarios y Kits
Este proyecto contiene un conjunto de scripts de prueba automatizados diseñados para interactuar con la API de Urben Grocers. El objetivo principal es garantizar que la API se comporte como se espera, tanto en escenarios de éxito (creación correcta de recursos) como en escenarios de error (manejo adecuado de entradas inválidas o situaciones inesperadas).

El proyecto utiliza Python para realizar solicitudes HTTP a los endpoints de la API y verifica las respuestas para asegurar la integridad de los datos y la funcionalidad.

Cómo Ejecutar las Pruebas
Para ejecutar las pruebas de este proyecto, sigue estos sencillos pasos:

Clona el repositorio:
Bash

git clone <URL_DE_TU_REPOSITORIO>
Navega al directorio del proyecto:
Bash

cd <nombre_del_directorio_del_proyecto>
Instala las dependencias: Asegúrate de tener requests instalado. Si no lo tienes, puedes instalarlo con pip:
Bash

pip install requests
(Asegúrate de que sender_stand_request y get_user_body/get_kit_body estén correctamente configurados y accesibles en tu entorno.)
Ejecuta los scripts de prueba: Para ejecutar todas las pruebas, puedes usar un runner de pruebas si lo tienes configurado (por ejemplo, pytest). Si no, puedes ejecutar los scripts individualmente (asumiendo que tus funciones de prueba están en un archivo como test_api.py):
Bash

python test_api.py
O si usas pytest:
Bash

pytest