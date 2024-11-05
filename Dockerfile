# Use a specific base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements/base.txt requirements/
RUN pip install --no-cache-dir -r requirements/base.txt

# Copy the entire project into the container
COPY . .

# Run collectstatic if you're using Django (uncomment if needed)
RUN python webhook/manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Start the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "webhook.wsgi:application"]
