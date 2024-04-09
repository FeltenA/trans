FROM python:3.10.13

RUN apt update -y && apt upgrade -y

COPY ./tools/requirements.txt /
COPY --chmod=777 ./tools/script.sh /
COPY ./files/transcendence /transcendence

RUN pip install -r /requirements.txt \
    && pip install Django \
    && pip install -U djangorestframework \
    && pip install djangorestframework_simplejwt \
    && apt install python3

ENTRYPOINT ["/script.sh"]