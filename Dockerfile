FROM python:3.7.13-alpine

RUN addgroup -S py
RUN adduser -S py -u 7447

USER py
WORKDIR /home/prometheus_py

COPY . .

EXPOSE 80
EXPOSE 8000

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "main.py"]
