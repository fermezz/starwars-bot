FROM python:3.8.1-alpine3.11

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python3", "-m", "starwars_bot.main"]
