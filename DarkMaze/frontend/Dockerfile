FROM python:3.11
RUN useradd -m appuser

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt /app/requirements.txt
COPY src/ /app/src

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8088
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]