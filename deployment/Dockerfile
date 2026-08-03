FROM python:3.15.0b4-alpine

COPY ../requirements /requirements
COPY ../scripts /scripts
COPY ../src /src

WORKDIR /src

EXPOSE 8000

RUN /py/bin/pip install -r /requirements/deployment.txt

RUN chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home octashop && \
    chown -R octashop:octashop /vol && \
    chmod -R 755 /vol

ENV PATH="/scripts:/py/bin:$PATH"

USER octashop

CMD ["run.sh"]