FROM python:3.11.4-slim-bullseye

# Environment Variables
ENV LANG=C.UTF-8

# Install packages and dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    ca-certificates \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libsqlite3-dev \
    libbz2-dev


# Set working directory
WORKDIR /opt/app

# Copy files
COPY create_env.sh \
    requirements.in \
    /opt/app/

# Install dependencies
RUN bash create_env.sh && \
    python -m pip install --upgrade pip && \
    python -m pip install --upgrade -r requirements.in
