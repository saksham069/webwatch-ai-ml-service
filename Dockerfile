FROM python:3.12-slim

WORKDIR /app

# installing dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

EXPOSE 5000

# run server
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-5000}