# TODO: Install the backend dependency package into the app folder inside the container.

FROM python:3.11
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN useradd --create-home appuser
RUN chown -R appuser:appuser /app

COPY --chown=appuser:appuser ./src/ /app/src
COPY --chown=appuser:appuser ./tests/ /app/tests
COPY --chown=appuser:appuser ./python3.11/ /app/python3.11

USER appuser
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000",  "--reload"]