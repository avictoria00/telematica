
# Trabajo de telemática
En master se encuentran los archivos main.py y dockerfile (no supe subirlo muy bien).

A pesar de tener la documentación en un archivo adjunto, por este medio se estructurará la explicación cómo desplegar el servicio de contendor,y además, subir aquí la evidencia de cómo se subieron los archivos al repositorio.

# Telemática - Servicio Web con Flask y Docker

Este proyecto es una aplicación pequeña construida con Python y Flask y desplegada en un contenedor docker, ideal como base para un servicio telemático simple.

# Requisitos para desplegar el servicio

Asegurate de tener instalado:

- Docker
- Python, también se realizará durante el desarrollo de la aplicación web pero se puede tener previamente instalado.
- Git (opcional, para clonar desde GitHub)

# ¿Cómo ejecutar el servicio?

  1. Clona este repositorio

git clone https://github.com/avictoria00/telematica.git
cd telematica

  2. Crea una imagen del dockerfile y ejecutarla.

sudo docker build -t app:01.

app = nombre de la imagen, puede ser el que se desee.
01= etiqueta de la imagen, puede ser el que se desee.

//comando para ekecutar el contenedor:
sudo docker run -d -p 80:80 app:01.

# Estructura del proyecto

appweb/
├── README.md         
├── master/            
│   ├── main.py        
│   └── Dockerfile      

Ahora, 
# ¿cómo se subió el trabajo a git?

Primero, se crea una carpeta en la cual voy a pasar la carpeta donde estén guardados los dos archivos anteriores, luego de esto, se inicializa el repositorio y se añade lo que esté en la carpeta.
![image](https://github.com/user-attachments/assets/2ee6e804-1596-4127-a271-a5911b47d990)
Luego de esto se accede a la cuenta en la cual se encuentra el repositorio por medio de "git remote add origin https://github.com/avictoria00/telematica.git" y se añade los archivos a github y ya :D.
![image](https://github.com/user-attachments/assets/ab579f65-784c-4b89-afc7-fa467e01ebb9)

