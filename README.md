# Docker prácticas

![Docker build](https://github.com/BenjaCC/docker-practicas/actions/workflows/docker-build.yml/badge.svg)
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


## app-flask-db

App web en Python (Flask) que cuenta visitas y las guarda en PostgreSQL. Los dos servicios se levantan juntos con Docker Compose.

### Cómo ejecutarla
```bash
cd app-flask-db
cp .env.example .env    # edita .env y pon tu propia contraseña
docker compose up --build
```
Abrir http://localhost:8000

### Cómo funciona
- `web`: la app Flask, construida con su propio `Dockerfile`.
- `db`: PostgreSQL, usando la imagen oficial.
- Un volumen (`datos-db`) guarda los datos, así el contador no se reinicia al apagar los contenedores.
- La contraseña va en `.env`, que no se sube al repositorio.

### Conceptos que practico
- Docker Compose con varios servicios
- Variables de entorno y manejo de secretos
- Volúmenes para persistir datos
- Redes entre contenedores (la app encuentra la base de datos por el nombre `db`)

## Pipeline de CI (GitHub Actions)

Cada vez que subo código a `main` (o abro un pull request), GitHub ejecuta automáticamente un pipeline que verifica que mis proyectos de Docker sigan funcionando. El archivo está en `.github/workflows/docker-build.yml`.

### Qué hace
1. Descarga el código del repositorio en una máquina Linux temporal (`actions/checkout`).
2. Construye la imagen de `web-estatica` con `docker build`.
3. Construye la imagen de `app-flask-db` con `docker build`.
4. Valida el `docker-compose.yml` con `docker compose config`, usando una contraseña de prueba porque el archivo `.env` real no se sube al repositorio.

Si alguno de los pasos falla, el pipeline se marca en rojo y el badge de arriba cambia, así detecto el problema antes de seguir.

### Cómo se ve el resultado
Se puede revisar en la pestaña **Actions** del repositorio, o desde la terminal con:
```bash
gh run list
gh run view --log-failed
```

### Conceptos que practico
- Integración continua (CI)
- Workflows en YAML con GitHub Actions
- Automatizar la construcción y validación de imágenes Docker
- Manejo de secretos: el `.env` no se sube, y el pipeline usa un valor de prueba
