FROM geopython/pygeoapi:latest

COPY ./example-config.yml example-config.yml
ENV PYGEOAPI_CONFIG=example-config.yml
EXPOSE 5000
ENTRYPOINT [ "pygeoapi", "serve" ]