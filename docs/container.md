# Containerfile Build & Run Guide

This guide provides detailed instructions for building, running, and managing the CSE API container.

## Prerequisites

- Docker or Podman installed
- `.env` file configured with `CSE_BASE_URL`

## Build Container

### Build with Docker

```bash
docker build -f containerfile -t cse-api:latest .
```

### Build with Podman

```bash
podman build -f containerfile -t cse-api:latest .
```

### Build with Specific Tag

```bash
docker build -f containerfile -t cse-api:v1.0 .
```

## Run Container

### Basic Run

```bash
docker run -p 8000:8000 --env-file .env cse-api:latest
```

### Run in Detached Mode (Background)

```bash
docker run -d -p 8000:8000 --env-file .env --name cse-api cse-api:latest
```

### Run with Custom Port

```bash
docker run -p 8001:8000 --env-file .env cse-api:latest
```

### Run with Environment Variables

```bash
docker run -p 8000:8000 \
  -e CSE_BASE_URL=https://www.cse.lk/api \
  cse-api:latest
```

## Container Management

### List Running Containers

```bash
docker ps
```

### Stop Container

```bash
docker stop cse-api
```

### Start Stopped Container

```bash
docker start cse-api
```

### Restart Container

```bash
docker restart cse-api
```

### Remove Container

```bash
docker rm cse-api
```

### Remove Container (Force)

```bash
docker rm -f cse-api
```

### View Container Logs

```bash
docker logs cse-api
```

### Follow Container Logs

```bash
docker logs -f cse-api
```

### Execute Command in Running Container

```bash
docker exec -it cse-api /bin/bash
```

## Image Management

### List Images

```bash
docker images
```

### Remove Image

```bash
docker rmi cse-api:latest
```

### Remove Image (Force)

```bash
docker rmi -f cse-api:latest
```

## Complete Workflow

### 1. Build the Container

```bash
docker build -f containerfile -t cse-api:latest .
```

### 2. Run the Container

```bash
docker run -d -p 8000:8000 --env-file .env --name cse-api cse-api:latest
```

### 3. Verify Container is Running

```bash
docker ps | grep cse-api
```

### 4. Check Logs

```bash
docker logs cse-api
```

### 5. Test the API

```bash
curl http://localhost:8000/health
```

### 6. Stop the Container

```bash
docker stop cse-api
```

### 7. Remove the Container

```bash
docker rm cse-api
```

## Troubleshooting

### Port Already in Use

If port 8000 is already in use, use a different port:

```bash
docker run -p 8001:8000 --env-file .env cse-api:latest
```

### Check Port Usage

```bash
lsof -i :8000
```

### View Container Status

```bash
docker ps -a
```

### Inspect Container

```bash
docker inspect cse-api
```

### View Container Resource Usage

```bash
docker stats cse-api
```

## Environment Variables

The container requires the following environment variables:

- `CSE_BASE_URL`: Base URL for the CSE API (default: `https://www.cse.lk/api`)

These can be provided via:
- `.env` file using `--env-file .env`
- Direct environment variables using `-e` flag
- Docker Compose file

## Container Details

- **Base Image**: `python:3.10-slim`
- **Working Directory**: `/app`
- **Exposed Port**: `8000`
- **Command**: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## Notes

- The container runs the FastAPI application using Uvicorn
- All application code is copied into the container during build
- Environment variables from `.env` file are loaded at runtime
- The container exposes port 8000 by default
- Use `-d` flag to run in detached mode (background)
- Use `--name` to assign a custom container name for easier management
