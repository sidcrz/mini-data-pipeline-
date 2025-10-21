# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirement list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy ETL script
COPY etl_script.py .

# Default command
CMD ["python", "etl_script.py"]
