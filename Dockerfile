FROM python:3.9

ENV VIRTUAL_ENV=/opt/venv
ENV PATH=$VIRTUAL_ENV/bin:$PATH
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=dataeden
ENV POSTGRES_DB=postgres

COPY ./dataeden_site /app

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

# CMD ["bash", "migrate.sh"]
ADD migrate.sh /app
