FROM python:3.11.7-slim

# Set environment variable to ensure output is flushed directly to the terminal
ENV PYTHONUNBUFFERED=1

# Expose the application port
EXPOSE 8000

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file from host to the container
COPY ./requirements.txt .

# Copy everything from the ./src directory on the host to /app in the container
COPY ./src .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the application using uvicorn, specifying the host and port
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]
