# LLM Deployment with FastAPI

## Model

Qwen2.5-1.5B-Instruct

## Features

- REST API
- Docker support
- Streaming endpoint
- Concurrent benchmark

## Endpoints

POST /generate

Returns a complete response.

POST /stream

Returns tokens progressively using StreamingResponse.

## Run

```bash
docker build -t llm-api .
docker run -p 8000:8000 llm-api
```

Open:

http://localhost:8000/docs

to test the API interactively.
