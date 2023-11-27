FROM python:3.10.13-slim-bookworm

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# COPY ./main.py /code/main.py
COPY ./src /code/src

CMD [ "uvicorn", "--host", "0.0.0.0", "src.main:app" ]