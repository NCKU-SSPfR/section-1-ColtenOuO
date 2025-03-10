FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt
RUN useradd -m -u 1000 appuser
RUN chown -R appuser:appuser /app

COPY --chown=appuser:appuser ./src/ /app/src
COPY --chown=appuser:appuser ./src/ /app/tests

USER appuser
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]