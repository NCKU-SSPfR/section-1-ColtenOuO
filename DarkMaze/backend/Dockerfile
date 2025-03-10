# TODO: Install the backend dependency package into the app folder inside the container.

FROM python:3.11
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . .
EXPOSE 8000

USER appuser
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000",  "--reload"]