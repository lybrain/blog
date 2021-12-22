FROM python:3.9


WORKDIR /blog 

COPY Pipfile* /blog/ 

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear 

COPY . /blog/ 

EXPOSE 8000 
