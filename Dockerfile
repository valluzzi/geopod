FROM geopython/pygeoapi:latest

COPY ./.kube/config /root/.kube/config
COPY ./config.yml config.yml
ENV PYGEOAPI_CONFIG=config.yml

COPY ./plugins/ ./plugins
RUN pip install ./plugins
RUN rm -rf ./process

EXPOSE 5000
ENTRYPOINT ["pygeoapi", "serve"]