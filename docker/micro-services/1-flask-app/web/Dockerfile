FROM ubuntu:latest
MAINTAINER bhagavan "bhagavan@auranetworks.in"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app

COPY app.py /usr/src/app/
COPY index.html /usr/src/app/templates/


WORKDIR /app
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["app.py"]

EXPOSE 5000

CMD ["python", "/usr/src/app/app.py"]

