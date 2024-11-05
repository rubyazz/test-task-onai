# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY requirements/ requirements/

RUN pip install --no-cache-dir -r requirements/base.txt

COPY . .

RUN python webhook/manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "webhook.wsgi:application"]
