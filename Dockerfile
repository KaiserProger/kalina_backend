FROM python:3.11-slim-buster

ENV POETRY_VERSION=1.4.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt clean && \
    rm -rf /var/cache/apt/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"


COPY . /src
ENV PATH "$PATH:/src/scripts"

RUN useradd -m -d /src -s /bin/bash app \
    && chown -R app:app /src/* && chmod +x /src/scripts/*

WORKDIR /src

COPY poetry.lock pyproject.toml ./
RUN poetry install

RUN poetry exit

USER app

CMD ["./scripts/start-dev.sh"]
