# Review_collector

A small project to collect product reviews via WhatsApp/SMS (Twilio) and view them on a React UI.

## Components
- FastAPI backend — receives Twilio webhooks and stores reviews in Postgres.
- PostgreSQL — persistence.
- Simple React frontend — display collected reviews.
- Docker Compose for easy orchestration.

## Quick start
1. Build and run:
   ```bash
   docker-compose up --build
