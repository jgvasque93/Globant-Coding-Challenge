# Globant-Coding-Challenge
Goal: Create a Music artists data API.
- Support the following endpoint GET /artist?name=ArtistName
- The data must be human-readable.
- Use environment variables for configuration.
- The response must include the content-type header (application/json)
- Functions must be tested.
- Keep a cache of 2 minutes of the data. You can use a persistence layer for this.

For extra points:

- Create custom exceptions to contemplate possible errors when the endpoint is consumed.
- Upload and deploy the solution to a free cloud service like Heroku.


## Setup Project

Este challenge se puede probar de manera local con docker y tambien de manera online , ya que la app esta subida a heroku(se cambio a AWS elasticbeanstalk debido a que a la fecha se pide un metodo de pago en Heroku).

## Prueba local
Requisitos:
- Asegurarse de tener instalado Docker en su sistema operativo

Este proyecto esta configurado con docker-compose para que sea mas facil su prueba e instalacion. Las variables de configuracion tanto para el entorno de flask como para el setup de la aplicacion se encuentran en los files .env y .flaskenv los cuales estan incluidos en este proyecto. Para un proyecto que no sea de prueba se recomienda pasar estos files encriptados mediante algun metdo acordado por los contribuidores del proyecto

### Steps
- Clonar repositorio con el proyecto

```console
git clone https://github.com/jgvasque93/Globant-Coding-Challenge.git
```
- Entrar a la carpeta del proyecto

```console
cd Globant-Coding-Challenge
```
- Ejecutar docker-compose para contruir la imagen que contiene en el file Dockerfile y que tambien se lance la misma

```console
docker-compose up -d --build
```

- En cualquier navegador o por console visitar la ruta http://localhost/artist?name=coldplay para comprobar que esta corriendo la app.
En consola se puede correr:
```console
curl -i http://localhost/artist?name=coldplay
```

- Mientras se contruia la imagen se ejecuto en el Dockerfile el comando python3 -m flask test, el cual garantiza que la app solo puede ser contruida si los test configurados para la misma se ejecutaron de manera correcta. Si se desea ejecutar los test de manera manual se debe ejecutar en la consola:
```console
docker-compose exec app bash
```

- y dentro de la imagen ejecutar:
```console
flask test
```

## Prueba on Live
El endpoint esta deployado en AWS elasticbeanstalk debido a que Heroku al momento de crear un proyecto pide un metodo de pago,y el servicio de aws ya lo tengo autentificado y actualizado
```console
http://global-challange-jordyvasquez.us-east-1.elasticbeanstalk.com/artist?name=coldplay
```
