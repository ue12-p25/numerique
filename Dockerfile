# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Avoid interactive prompts during package installs
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for scientific packages and Jupyter
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Create a working directory
WORKDIR /workspace

# Copy requirements and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose Jupyter port
EXPOSE 8888

# Set up a default command for Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
