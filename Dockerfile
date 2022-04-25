FROM python:3.8

WORKDIR /usr/src/app/gods_unchained_card_analyzer

COPY app/ ./app/
COPY dev.env ./dev.env
COPY models/ ./models/.
COPY requirements.txt ./requirements.txt

EXPOSE 8000

RUN pip install --no-cache-dir  -r requirements.txt
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app"]
