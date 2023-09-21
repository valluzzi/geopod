FROM geopython/pygeoapi:latest


COPY ./config.yml config.yml
ENV PYGEOAPI_CONFIG=config.yml

COPY ./process/ ./process
RUN pip install ./process


EXPOSE 5000
ENTRYPOINT [ "pygeoapi", "serve" ]