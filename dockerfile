FROM python:2.7.18-alpine3.11

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

# run server when container is started

CMD ["python", "app.py"]

# expose server port
EXPOSE 5000
