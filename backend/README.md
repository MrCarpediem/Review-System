# Backend (FastAPI)

This folder contains the FastAPI backend that receives Twilio webhooks and stores reviews in PostgreSQL.

## Prerequisites
- Python 3.10+ (recommended)
- PostgreSQL (when running locally) or use the included Docker Compose setup

## Install (local development)
1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set environment variables (example):

```bash
export DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/reviews_db
```

## Database migrations (Alembic)
Alembic is configured in this repository. To apply migrations locally:

```bash
alembic upgrade head
```

To create a new migration after making model changes:

```bash
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

## Run development server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available on `http://localhost:8000`.

## Docker / Production (via docker-compose)
The repository includes a `docker-compose.yml` at the project root that brings up a Postgres DB, the backend, and the frontend. To run everything with Docker:

```bash
docker-compose up --build
```

This will build the backend image using the `backend/Dockerfile` and start the services.

## Configuration
- `DATABASE_URL`: SQLAlchemy database URL (used by the app and Alembic).

## Endpoints (quick)
- Twilio webhook endpoint: configured in `app/twilio_webhook.py` (see code for path)

If you want, I can show the exact URL paths and example curl commands for local testing.
