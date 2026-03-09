# 1. Use an official Python runtime as a base image
FROM python:3.12-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Install system dependencies for MySQL (important for flask-mysqldb)
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy the requirements file into the container
COPY requirements.txt .

# 5. Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application code
COPY . .

# 7. Expose the port Flask runs on
EXPOSE 5000

# 8. Command to run the app using Gunicorn (production server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]