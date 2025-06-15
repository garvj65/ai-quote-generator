FROM python:3.11-slim-bullseye

# Update packages and install security fixes
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app ./app
CMD ["python", "app/main.py"]
