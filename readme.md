# Challenge Backend developer by Hamilton Sánchez - CopyRight

# Al Revisar este código acepta que no podrá usarse para fines empresariales de desarrollo

# puesto que fue implementado para fines de un proceso de selección.

## Primeros Pasos:

1. Ambiente virtual

- recomiento la instalacion de un paquete como conda o miniconda o el de su preferencia
- una vez haya creado y activado el ambiente, `conda create -n challange python=3.10` por ejemplo, dirijase a la ubicación del archivo requeriments.txt
- ejecute `pip install -r requirements.txt`, con esto tendrá las dependencias necesarias para correr el proyecto.

2. Base de datos:

- El proyecto está por defecto configurado para usar una base de datos PostgreSQL, si ud prefiere, puede ir al archivo settings.py y cambiar esto para utilizar la db por defecto en django que es SQLite3 (no se recomienda por no tener el mismo performance).
- Cuando ya haya decidido que db usar, por favor dirijase a la ubicación del archivo manage.py en la terminal y realice : `python manage.py makemigrations`, después : `python manange.py migrate`, con esto su base de datos tendrá todas las tablas y esquemas necesarios para funcionar con la aplicación.

## Correr script y cargar data

- Al realizar los pasos 1 y 2 podrá entonces cargar la data. Estando en la ubicación del archivo manage.py en la terminal, ejecute:
  `python manage.py load_all_data`, esto cargará datos como paises, empresas, usuarios, entre otros modelos para hacer más rápido las cosas, en este punto ya se cumple por ejemplo el Item 3 del reto, relacionado con los datos.
- si un aviso de "Todos los datos han sido cargados exitosamente" aparece en su terminal, el proceso fue exitoso, puede dirigirse a las tablas en db corroborarlo.

## Pruebas en POSTMAN

- A continuación se detalla el cómo probar en postman, endpoints y demás, por favor levante el servidor.
  `python manange.py runserver`

1. Login:

- haga una solicitud POST a : `http://127.0.0.1:8000/api/1.0/login/` , con la siguiente carga útil (tal cual):
  {
  "email":"usuario1@example.com",
  "password":"password1"
  }
  el endpoint le retornará el token de acceso, por favor agreguelo a una variable de entorno en postman o simplemente copielo y tengálo en el clipboard ( el de tipo access ), los usuarios creados tienen esa estructura, para más info dirijase a users.json

2. Probando Item 2 del challenge:

- Anteriormente se cargaron datos con información de registros de encuestas para los diferentes cargos de forma aleatoria para al menos 8 diferentes países, usted podrá probar lo siguiente :
  ● Muestreo del NPS por país clasificándolos un top 3 de de los países con más encuestas con detractores
- path : `/api/1.0/report_detractor/` method: GET ( en Authorization seleccione Berear Token y pegue su token)
  este endpoint le retornará lo solicitado.

● Clasificar los tipos de personas con mayor calificación de promotor

- path : `/api/1.0/report_promoter/` method: GET ( en Authorization seleccione Berear Token y pegue su token)
  este endpoint le retornará lo solicitado.

● Clasificar las encuestas por mes dentro indicando cual es el detractor vs promotor mas alto de cada país

- path : `/api/1.0/report_monthly/` method: GET ( en Authorization seleccione Berear Token y pegue su token)
  este endpoint le retornará lo solicitado.

3. Item 3 Datos, esto ya ha sido ejecutado en Correr script y cargar data

4. Endpoints:
   ● Un usuario logueado puede ver los datos de todos los clientes que calificaron a la empresa por debajo de 4 puntos, y la posibilidad de enviar un registro de log de que fue contactado

- path : `/api/1.0/low_rating/` method: GET ( en Authorization seleccione Berear Token y pegue su token)
  este endpoint le retornará lo solicitado.

● Los NPS pueden ser diligenciados por usuarios logueados o no, si estoy logueado enviare mis datos básicos para el registro de la encuesta, de lo contrario entraré está registrado como usuario anónimo

- path : `/api/1.0/nps_rating/` method: POST payload :{ "score":10 } (Si envía el token, el backend reconocerá su usuario y la información suya quedará almacenada automáticamente, sino lo hace, el dato de usuario quedará Nulo equivalente a Anónimo)

● Un usuario logueado puede crear, eliminar, editar o leer empresas o cargos como a voluntad quiera
para esto por favor pegue el token para poder tener los permisos.

- path : `/api/1.0/company/` method: GET response: devuelve la lista de empresas
- path : `/api/1.0/company/<id_company>/` method: PUT,PATCH response: puede EDITAR parcialmente o totalmente el registro
- path : `/api/1.0/company/<id_company>/ ` method: DELETE response: puede ELIMINAR el registro
- path : `/api/1.0/company/ ` method: POST response: puede CREAR un registro de empresa, enviando la data requerida en el body

Esto mismo aplica para cargos, para esto cambie "company" por "rol", ejemplo : path : `/api/1.0/rol/` method GET devuelve lista de roles, tiene disponible POST,GET,DELETE,PUT,PATCH, para company u rol.

● El endpoint del registro de NPS debe enviar a través de un decorador un evento a base de datos registrando los datos generales del navegador y sistema operativo que se usó para el registro de los datos.

- Aquí implemnté un Logger que registra esta información, lo hace através de un decorador @LogEvent, por cuestión de tiempo no lo envie a base de datos.

5. Comunicación con un servicio externo

- Esto se realiza en el archivo load_country_api.py, que se ejecuta en el script de "load_all_data" automaticamente.

6. Calidad y cobertura de código:

- Use la librería coverage, puede ejecutarla haciendo `coverage run manage.py test `, llegué a un total de 84% de cobertura, omitiendo archivos como los "**init**.py" o de configuración, estos se encuentran en .coveragerc.

## Puede ver un reporte ejecutando `coverage html` , creará un folder en la ruta htmlcov/index.html

## La prueba la realicé en un total de 15 horas.

## Consideraciones:

- El proyecto tiene 2 apps:
  - nps_app : tiene una estructura limpia, donde cada archivo cumple con el principio de responsabilidad única, esto ayuda a la escalabilidad y colabaracion en el desarrollo.
  - user : este usa una estructura standar en django, por lo que no se necesita que fuera complejo.
  - en un entorno de productivo se recomienda la estructura de nps_app.
- los archivos que están al nivel del manage.py como : roles.json, users.json, etc, son para cargar la data.
- los diagramas de Modelado y arquitectura están en esta misma carpeta.
