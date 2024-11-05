Webhook Project
===============

This project is a Django-based application that processes incoming webhook requests using a large language model (LLM). It includes support for message history to maintain conversation context and is integrated with Redis for asynchronous task processing.

Table of Contents
-----------------
- `Features <#features>`_
- `Requirements <#requirements>`_
- `Installation <#installation>`_
- `Environment Variables <#environment-variables>`_
- `Usage <#usage>`_
- `Running with Docker <#running-with-docker>`_
- `License <#license>`_

Features
--------
- Process incoming webhook requests.
- Generate responses using an LLM.
- Maintain conversation context with message history.
- Asynchronous task processing with Celery and Redis.
- PostgreSQL as the database.

Requirements
------------
- Python 3.9 or higher
- Django 4.x
- Redis
- PostgreSQL
- Docker (optional, for containerized setup)

Installation
------------
1. **Clone the repository:**

   .. code-block:: bash

      git clone <repository-url>
      cd webhook-project

2. **Create a virtual environment:**

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**

   .. code-block:: bash

      pip install -r requirements/base.txt

4. **Set up the database:**

   - Ensure you have PostgreSQL installed and running.
   - Create a new database and user for your project. You can use the following commands in the PostgreSQL shell:

     .. code-block:: sql

        CREATE DATABASE your_database_name;
        CREATE USER your_user_name WITH PASSWORD 'your_password';
        ALTER ROLE your_user_name SET client_encoding TO 'utf8';
        ALTER ROLE your_user_name SET default_transaction_isolation TO 'read committed';
        ALTER ROLE your_user_name SET timezone TO 'UTC';
        GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_user_name;

5. **Run migrations to set up your database schema:**

   .. code-block:: bash

      python manage.py migrate

6. **(Optional) Create a superuser to access the Django admin:**

   .. code-block:: bash

      python manage.py createsuperuser

7. **Run the development server to ensure everything is set up correctly:**

   .. code-block:: bash

      python manage.py runserver

Environment Variables
---------------------
The application requires several environment variables for configuration. You can create a `.env` file in the project root and populate it with the following variables:

.. code-block:: dotenv

   DEBUG=True
   OPENAI_API_KEY=your_openai_api_key
   CELERY_BROKER_URL=redis://localhost:6379/0
   CELERY_RESULT_BACKEND=redis://localhost:6379/0
   POSTGRES_DB=your_database_name
   POSTGRES_USER=your_user_name
   POSTGRES_PASSWORD=your_password

Make sure to replace the placeholder values with your actual credentials.

Usage
-----
To process incoming webhook requests, send a POST request to the `/webhook/` endpoint with a JSON payload. Here is an example of a request body:

.. code-block:: json

   {
       "message": "Hello, how can I assist you today?"
   }

The application will respond with a generated reply based on the message provided.

Running with Docker
--------------------
To run the application using Docker, follow these steps:

1. **Ensure Docker and Docker Compose are installed on your machine.**

2. **Build the Docker images:**

   .. code-block:: bash

      docker-compose build

3. **Start the application:**

   .. code-block:: bash

      docker-compose up

4. **The application will be available at `http://localhost:8000/`.**

5. **To stop the application, you can use:**

   .. code-block:: bash

      docker-compose down
