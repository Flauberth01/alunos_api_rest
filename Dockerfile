FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["./run.sh"]
