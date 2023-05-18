FROM python:alpine

WORKDIR /app

COPY requirements/backend.in requirements.in

RUN pip install -r requirements.in

COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]