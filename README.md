# FlasK Project by Ruben Castillo

## DOCKER COMMANDS TO USE:

## To build image:

docker-compose build

## To run docker and start the Flask REST API :

- docker-compose up
- Go to http://localhost:5000/

## To run one container :

docker-compose up -d <container_name> (use -d flag for daemonized version)

## To stop all containers:

docker-compose down

## To stop all containers and delete the volumes:

docker-compose down -v

## To list containers

docker ps

## To stop a container

docker stop <container hash>

"See docker-compose for more details"

## Swagger URL:

http://localhost:5000/docs

## TO run the tests with Pytest:

pytest


# homework_1
## Numero 01
Escribe en el lenguaje de programación que desees, un programa que muestre en
pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por la palabra “VIN” y,
a su vez, los múltiplos de 5 por “CLE”. Para los casos que, al tiempo, son múltiplos de 3
y 5, utiliza el combinado “VINCLE”.

## Numero 02
Diseña, documenta e implementa una PC (entregable y ejecutable en Docker) de un
sistema para poder visualizar en tiempo real la evolución de creación, modificación,
parada y destrucción de Ítems.
Los Ítems podrán ser de tipo bebida, comida, salsas, especies.
Cualquiera de los ítems podrá tener de manera aleatoria las siguientescaracterísticas:
- Precisa nevera
- No precisa nevera
Cualquiera de los ítems podrá tener una capacidad de:
- 100 gr
- 1000 gr
Cualquiera de los ítems podrá tener un envase de:
- botella
- caja
Cualquiera de los ítems tendrá:
- Nombre
- Identificador numérico único
Se deberá guardar:
- El nombre del cliente que ha lanzado el comando de creación
- Se deberá guardar el ID del ítem
- Se deberá guardar la hora + timestamp de la operación
- Se deberá guardar el estado
o WAITING: Está procesando una petición (creación, eliminación,
cambio, etc.)
o CREATED: creado ok
o DELETED: Está eliminado
Finalmente, se deberá implementar un sistema de simulación que lanzando
peticiones aleatorias a la API cree, elimine, modifique ítems, para que estos
cambios se puedan monitorizar en tiempo real en el dashboard.
### En resumen, el sistema deberá proveer:
- Una API restful para gestionar el recurso “ítem” sobre una base de
datos. (Diseño Openapi 3)
- Una App para gestionar desde el backend el recurso ítem
implementando la API.
- Una interficie gráfica para visualizar y analizar (drill down) en tiempo real
los cambios en la colección de ítems desde el origen de datos.
- Una aplicación de test para lanzar la creación automática y aleatoria de ítems
(CRUD completo) contra la API de N elementos en tiempo real.
###### Silence is golden
