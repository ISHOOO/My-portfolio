FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit (launch homepage.py instead of app.py)
CMD ["streamlit", "run", "homepage.py", "--server.port=8501", "--server.address=0.0.0.0"]
