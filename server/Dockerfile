# Use Python 3.10 as base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy required files
COPY server.py requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the API port
EXPOSE 8000

# Run FastAPI server
CMD [ "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000" ]