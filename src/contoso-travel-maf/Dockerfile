FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and data
COPY . .

# Expose the agent server port
EXPOSE 8088

# Run the agent
CMD ["python", "agent.py"]
