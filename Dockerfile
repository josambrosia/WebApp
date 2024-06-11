FROM python:3.8-alpine

COPY . /app

# set working directory
WORKDIR /app

# set environment variables
ENV PYTHONUNBUFFERED 1

# alipne linux problem
#  Gagal bbrp kali, solved -> installing Pillow&PsycoPG require several dependencies. Bisa juga pakai virtual dependencies `--virtual nama`
RUN apk update --no-cache \
    && apk add postgresql-dev \
    && apk add gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install -r requirements.txt

# install dependencies
EXPOSE 8000
# RUN pip install -r requirements.txt

# RUN python manage.py migrate

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

