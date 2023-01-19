FROM python:3.9
USER root

COPY ./ds/docker/requirements.txt /tmp/requirements.txt
COPY ./ds/docker/ds_package /ds_package/
COPY ./ds/docker/training_config.json /training_config.json
COPY ./ds/docker/main.py /main.py
COPY ./ds/docker/utils.py /utils.py
COPY ./mle/mle_package /mle_package/

COPY ./ds/docker/setup.sh /setup.sh
RUN chmod +x /setup.sh
RUN /setup.sh
RUN rm /tmp/requirements.txt

CMD [ "python", "-u", "./main.py"]