FROM python:3.12
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY req.txt /app/
RUN pip install --upgrade pip && pip install -r req.txt
ADD . /app/
WORKDIR /app/mail-service/
RUN chmod +x run.sh

ENTRYPOINT ["/app/mail-service/run.sh"]