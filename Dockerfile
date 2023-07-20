FROM python:3.10-slim

ENV HOME /attestation
WORKDIR $HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements .
RUN pip install -r requirements

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
