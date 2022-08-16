# syntax=docker/dockerfile:1
FROM python:3.7-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "-m", "flask", "run", "--port=3000", "--host=0.0.0.0"]
# CMD ["python3", "-m", "gunicorn", "--bind", "0.0.0.0:3000", "wsgi:app"]