En este proyecto realizaremos un dashboard entre el lenguaje de programación Python y la tecnología de contenedores Docker para mostrar las ventas de videojuegos en las regiones mas importantes.

La primera parte del proyecto fue hacer un fork del repositorio, para ello desde github lo realizamos sencillamente para posteriormente utilizar el comando git clone para poder trabajar con el.

Tras entender lo que habia que hacer, procedemos a descargar un set de datos, en mi caso utilice video_games_scales.csv, el cual obtuve de la siguiente fuente: https://www.kaggle.com/datasets/thedevastator/global-video-game-sales-and-ratings

Ahora es cuando se puede decir que empieza el proyecto, y tambien donde surgieron los problemas, desde la terminal descargamos docker, para ello podemos usar el comando "pip install docker", y para ejecutarlo debemos usar el comando sudo, asi iniciandolo con "sudo docker-compose up".
Uno de los problemas mas grandes que me encontre en el proyecto fue la applicacion de streamlit, ya que aun no se como fui capaz de arreglarlo, intentando forzar la descarga, actualizando los requirments.txt y volvienod a instalar, forzando los permisos de docker para eliminar imagenes y contenedores y no dejaba, no voy a alargar mucho esta historia ya que ya hable contigo sobre los problemas que tuve y las posibles soluciones que estuvimos buscando.
Entonces,intente forzar el error:[el modulo "streamlit" no tiene ningun atributo], para ello como no me dejaba descargar ningun modulo ya que el proyecto se realizaba desde un enviroment externo. Entonces, hice una copia de seguridad para no volver a perder los datos por si algo fallaba, y me creé mi propio enviroment, llamado ".venv", desde ahi force la descarga del paquete con la terminacion "--break-system-packages" forzando la descarga, y... funcionó.

Una vez el Entorno funcionaba perfectamente ya podia editar el codigo para que mostrase el set de datos, asi que en el archivo "server.py" cargamos todos los datos, además de editar cada tipo de cada una de las variables.
Y para la edición del Dashboard, editamos el script "1_dashboard.py" para obtener los datos quenosotros deseamos.