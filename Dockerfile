FROM python:3.12 as pre_auth

ARG CONTEXT=GCP
ENV CONTEXT ${CONTEXT}
WORKDIR /code
ENV PYTHONPATH=/code/python

RUN pip install poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock so dependencies only get rebuilt if they are changed
# Creds file as wildcard to not fail if not present
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --no-root

COPY ./python ./python
WORKDIR /code/python
CMD ["uvicorn", "app.adaptor.into.api.fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
