ARG CERVER_VERSION=2.0b-29

FROM ermiry/mongoc:builder as builder

RUN apt-get update && apt-get install -y libssl-dev

# build cerver with production flags
ARG CERVER_VERSION
RUN mkdir /opt/cerver && cd /opt/cerver \
    && wget -q --no-check-certificate https://github.com/ermiry/cerver/archive/${CERVER_VERSION}.zip \
    && unzip ${CERVER_VERSION}.zip \
    && cd cerver-${CERVER_VERSION} \
    && make TYPE=production -j4 && make TYPE=production install

############
FROM ermiry/mongoc:latest

WORKDIR /home/todo

# cerver
ARG CERVER_VERSION
COPY --from=builder /opt/cerver/cerver-${CERVER_VERSION}/bin/libcerver.so /usr/local/lib/
COPY --from=builder /opt/cerver/cerver-${CERVER_VERSION}/include/cerver /usr/local/include/cerver

# todo
WORKDIR /opt/todo
COPY *.py .

RUN ldconfig

CMD ["/bin/bash", "start.sh"]