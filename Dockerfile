# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt (if you have one) and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire repo
COPY . .

# Expose the port (8501 for Streamlit, 5000/8000 for Flask/FastAPI)
EXPOSE 8501

# Default command (change this depending on your framework)
# For Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# If it's Flask, instead use:
# CMD ["python", "app.py"]

# If it's FastAPI with uvicorn:
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
