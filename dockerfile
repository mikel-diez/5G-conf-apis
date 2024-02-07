FROM python:3.8-slim

WORKDIR /app

COPY reqs.txt .

RUN pip install --no-cache-dir -r reqs.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]