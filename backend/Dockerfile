# backend/Dockerfile

# 1. Base image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all backend files
COPY . .

# 5. Expose port
EXPOSE 5000

# 6. Run the Flask app
CMD ["python", "app.py"]
