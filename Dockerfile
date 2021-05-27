# Dockerfile, Image, Container

FROM python:3.9

ADD sandbox/main.py .

CMD ["python", "./main.py"]