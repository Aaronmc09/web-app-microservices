FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /main
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /main
EXPOSE 5000