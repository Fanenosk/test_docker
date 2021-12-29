FROM python:3.9.9-slim-buster

RUN pip install poetry

COPY pyproject.toml .
COPY poetry.lock .
COPY requirements.txt .

RUN pip install -r requirements.txt 

RUN poetry install

COPY auth.py .
COPY main.py .

EXPOSE 5000

CMD [ "python", "./main.py"]