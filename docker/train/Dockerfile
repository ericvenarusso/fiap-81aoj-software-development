FROM python:3.8

WORKDIR /usr/src/app

COPY data/train.csv ./data/train.csv
COPY app/machine_learning/trainer.py ./trainer.py
COPY config/train/ ./config/train/
COPY requirements/train/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir  -r requirements.txt
CMD [ "python", "trainer.py" ]
