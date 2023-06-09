FROM python:3.10-slim-buster
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "telegram_bot/bot.py"]