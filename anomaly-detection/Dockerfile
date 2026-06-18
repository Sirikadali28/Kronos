FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY detect_anomalies.py .
COPY sample-output.txt .

CMD ["python", "detect_anomalies.py"]
