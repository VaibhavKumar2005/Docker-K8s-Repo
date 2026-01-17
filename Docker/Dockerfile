# 1. Use official Python image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements & install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all code
COPY . .

# 5. Expose port
EXPOSE 80

# 6. Run FastAPI app using uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
