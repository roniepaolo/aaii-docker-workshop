# Variables before image base
ARG PYTHON_VERSION=3.8

# Image base
FROM python:${PYTHON_VERSION}

# Variables after image base
ARG PYTHON_APP_DIR=/app

# Complement files
COPY requirements.txt .
COPY src/ ${PYTHON_APP_DIR}/
COPY docker/docker-entrypoint.sh /usr/bin/

# Dependencies
RUN set -eux; \
    \
    apt-get update; \
    apt-get upgrade; \
    pip install -r requirements.txt;

# Entrypoint
ENTRYPOINT ["docker-entrypoint.sh"]

# Working directory
WORKDIR ${PYTHON_APP_DIR}/

# Command
CMD ["python3", "my_app.py"]
