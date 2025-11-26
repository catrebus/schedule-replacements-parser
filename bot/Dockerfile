FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./bot

CMD ["python","-m", "bot.main"]

