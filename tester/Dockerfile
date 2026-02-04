FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir requests

COPY test_script.py .

CMD ["python", "test_script.py"]