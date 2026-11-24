# Docker prácticas
## web-estatica

Página HTML servida con nginx dentro de un contenedor Docker.

### Cómo ejecutarla
```bash
cd web-estatica
docker build -t mi-web-estatica .
docker run -d -p 8080:80 --name web1 mi-web-estatica
```
Abrir http://localhost:8080

### Qué hace el Dockerfile
- `FROM nginx:alpine`: usa una imagen ligera de nginx como base.
- `COPY index.html ...`: copia la página dentro de la imagen.
- `EXPOSE 80`: indica el puerto que usa el contenedor.

### Conceptos que practico
- Imágenes y contenedores
- `docker build` y `docker run`
- Mapeo de puertos (`-p 8080:80`)

