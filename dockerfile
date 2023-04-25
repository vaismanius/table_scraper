FROM python:10-slim
WORKDIR /app
COPY . /app
RUN pip install -r /requirements.txt
CMD python scraper.py