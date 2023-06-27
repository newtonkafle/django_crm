FROM python:3.9-alpine3.13

# set environment variables
ENV PYTHONUNBUFFERED 1

# copy the requirement file to the directory
COPY ./requirements.txt /tmp/requirements.txt

# copy the project code to the working directory 
COPY ./app /app/

# set the working directory on the container
WORKDIR /app

#Expose the port to the django development server
EXPOSE 8000

ARG DEV=false

# install project dependencies
RUN python -m venv /env && \
    /env/bin/pip install --upgrade pip && \
    /env/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django_user


ENV PATH="/env/bin:$PATH"

USER django_user

# # start django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



