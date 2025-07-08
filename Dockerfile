FROM python:3.11.9
EXPOSE 7500
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app