# Webhook Project

This project is a Django-based application that processes incoming webhook requests using a large language model (LLM). It includes support for message history to maintain conversation context and is integrated with Redis for asynchronous task processing.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Running with Docker](#running-with-docker)
- [License](#license)

## Features

- Process incoming webhook requests.
- Generate responses using an LLM.
- Maintain conversation context with message history.
- Asynchronous task processing with Celery and Redis.
- PostgreSQL as the database.

## Requirements

- Python 3.9 or higher
- Django 4.x
- Redis
- PostgreSQL
- Docker (optional, for containerized setup)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd webhook-project
