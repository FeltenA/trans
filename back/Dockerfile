FROM python:3.10.13

RUN apt update -y && apt upgrade

WORKDIR .

COPY ./tools/requirements .
COPY ./files/transcendence .

RUN pip install -r requirements.txt \
    && python transcendence/manage.py migrate \
    && pip install Django \
    && pip install -U djangorestframework \
    && pip install djangorestframework_simplejwt \
    && apt install python3

ENTRYPOINT ["/script.sh"]