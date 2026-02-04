# Python Test Container Dockerfile

# slim variant: smaller than full image, has what we need. Trade-off: no compiled libs
FROM python:3.9-slim

WORKDIR /app

# Copy requirements first - enables Docker layer caching for faster rebuilds
COPY requirements.txt .
# no-cache-dir = smaller image (don't store pip cache)
RUN pip install --no-cache-dir -r requirements.txt

COPY test_script.py .

# Container runs tests and exits. Exit code determines CI pass/fail
CMD ["python", "test_script.py"]
