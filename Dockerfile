FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Azure uses PORT env variable
ENV PORT=8000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.app:app"]

