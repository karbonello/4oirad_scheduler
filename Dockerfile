FROM python:3.9-alpine as intermediate
ARG SSH_PRIVATE_KEY
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="/root/.cargo/bin:/root/.poetry/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
    poetry install --no-dev -E prod

FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH="${PYTHONPATH}:/app"
ENV PATH="/app/.venv/bin:$PATH"
COPY --from=intermediate /app/.venv/ /app/.venv
COPY . /app
WORKDIR /app
VOLUME ["/var/logs"]
EXPOSE 8000
ENTRYPOINT [ "/entrypoint.sh" ]
