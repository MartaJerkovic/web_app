FROM python:3.11-slim as build

WORKDIR /crypto_app
COPY requirements.txt /crypto_app

RUN pip3 install --no-cache-dir -r /crypto_app/requirements.txt
COPY . .

EXPOSE 5000

CMD ["python3", "run.py"]