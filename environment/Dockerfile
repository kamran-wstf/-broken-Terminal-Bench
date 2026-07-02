FROM python:3.11.6-slim@sha256:0d8e3c6d2f7a6d9a3b5a5e5f6c3b4a2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b

RUN pip install --no-cache-dir pytest==8.4.1

WORKDIR /app

# Copy only the input access log into the image; do not include reference solutions.
COPY access.log /app/access.log
