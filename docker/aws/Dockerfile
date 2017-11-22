FROM ubuntu:15.04

RUN apt-get update

RUN apt-get install -y python curl unzip wget

RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" \
	&& unzip awscli-bundle.zip \
	&& ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

ADD aws_config /root/.aws

ADD scripts /root

RUN chmod +x /root/*.sh

CMD while true; do /root/put_monitor.sh; sleep 3600; done
