FROM python:3.8-slim-buster
ADD server.py .
ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --log /tmp/pip-log.txt --verbose
RUN mkdir -p ./templates
ADD ./templates/index.html ./templates/index.html
ADD ./templates/index2.html ./templates/index2.html
CMD ["python", "./server.py"]
