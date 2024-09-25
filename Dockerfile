FROM python:3.12-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock /app/

RUN poetry install --only main

COPY . /app

RUN poetry run pytest

EXPOSE 8077

CMD ["poetry", "run", "uvicorn", "src.python.main:app", "--host", "0.0.0.0", "--port", "8077"]