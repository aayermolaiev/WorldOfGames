FROM python:3.11-slim

WORKDIR /app

COPY *.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8777

ENV FLASK_APP=MainScoresFlaskApp

CMD ["python", "MainScores.py"]
