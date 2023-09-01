FROM python:3.9

ENV VIRTUAL_ENV=/opt/venv
ENV PATH=$VIRTUAL_ENV/bin:$PATH

COPY ./dataeden_site /app

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]