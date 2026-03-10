hen you have multiple services (for example a Python app and a database), Docker creates separate images and containers for each service. Usually this is managed using Docker Compose.

Concept

Each service has:

Its own image

Its own container

Its own configuration

Example services:

Python application

Database (MySQL / PostgreSQL)

Docker will create two containers from two images.

Example Project Structure
project/
 ├── app.py
 ├── requirements.txt
 ├── Dockerfile
 └── docker-compose.yml
Step 1 — Create Dockerfile for Python App

This builds the Python image.

FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
Step 2 — Create docker-compose.yml

Here we define multiple services.

version: "3"

services:

  web:
    build: .
    ports:
      - "5000:5000"

  db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: password
Step 3 — Run Docker Compose
docker-compose up

What happens internally:

1️⃣ Docker builds Python image from Dockerfile
2️⃣ Docker pulls MySQL image from Docker Hub
3️⃣ Docker creates two containers

Container 1 → Python App
Container 2 → MySQL Database

Both containers run in the same Docker network, so the Python app can connect to the database using:

host = db

(db is the service name)

Visual Flow
Dockerfile → Python Image → Python Container
Docker Hub → MySQL Image → MySQL Container

Docker Compose connects them automatically.

Important Interview Point ⭐

Docker does NOT create one image for multiple services.
Instead:

Each service = separate image

Each image = separate container

✅ Best Interview Answer

When an application has multiple services like a Python API and a database, Docker creates separate images and containers for each service. Tools like Docker Compose define these services in a YAML file and start all containers together.