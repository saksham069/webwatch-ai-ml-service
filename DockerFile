FROM python:3.10-slim

WORKDIR /app

# installing dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy the project
COPY . .

EXPOSE 5000

# run server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
