# Review_collector

A small project to collect product reviews via WhatsApp/SMS (Twilio) and view them on a React UI.

**Features:**
- Collect reviews submitted via Twilio (SMS/WhatsApp).
- Store reviews in PostgreSQL.
- Simple React UI to view collected reviews.
- Docker Compose for easy local orchestration.

**Architecture:**
- **Backend:** FastAPI app (in `backend/`) — receives Twilio webhooks and stores reviews.
- **Database:** PostgreSQL (Docker service `db`).
- **Frontend:** React + Vite (in `frontend/`) — shows collected reviews.

**Services (docker-compose):**
- `db` — PostgreSQL 15
- `backend` — FastAPI app (exposes port `8000`)
- `frontend` — React app (served in container, exposed on port `5173`)

## Quick start (recommended)
1. Build and run everything with Docker Compose:

```bash
docker-compose up --build
```

2. Access the services:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000

## Development

Backend development and details are in `backend/README.md`.
Frontend development and details are in `frontend/README.md`.

## Environment variables
- The Docker Compose setup injects `DATABASE_URL` into the backend. When running locally, set:

```bash
export DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/reviews_db
```

## Database migrations
The backend uses Alembic for migrations. See `backend/README.md` for commands to run migrations locally (or let Docker Compose handle DB creation when using the provided `docker-compose.yml`).

## Contributing
- Open an issue or submit a PR with small, focused changes.
- Keep changes to a single service per PR when possible.

---
If you'd like, I can also run the app locally (start Docker Compose) or show how to run backend and frontend individually. Which would you prefer next?
