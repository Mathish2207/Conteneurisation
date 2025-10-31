# syntax=docker/dockerfile:1

# ---------- STAGE BASE ----------
FROM python:3.12-slim AS base
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ---------- STAGE DEPS ----------
FROM base AS deps
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---------- STAGE RUNTIME ----------
FROM base AS runtime

# Copier dépendances depuis le stage deps
COPY --from=deps /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=deps /usr/local/bin/uvicorn /usr/local/bin/uvicorn

# Copier l’application
COPY app.py .
COPY entrypoint.sh .
COPY log.ini .

# Créer utilisateur non-root et assigner les droits
RUN adduser --disabled-password --gecos "" todo \
    && chown -R todo:todo /app

USER todo

# Exposer le port et définir variables d’environnement
EXPOSE 8000
ENV PORT=8000 \
    TODO_DB_PATH=/app/data/todo.db

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
    CMD curl -fsS http://127.0.0.1:${PORT}/health || exit 1

# Entrypoint et CMD
ENTRYPOINT ["./entrypoint.sh"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "log.ini"]
