web: alembic upgrade head && uvicorn api.app:app --host 0.0.0.0 --port ${PORT:-8000}
worker: arq api.workers.scrape_worker.WorkerSettings
