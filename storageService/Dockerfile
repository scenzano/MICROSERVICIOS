FROM alpine:latest

RUN apk add --update py-pip
RUN pip install --upgrade pip
ADD . /usr/src/storageService
WORKDIR /usr/src/storageService
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8082

CMD ["python", "/usr/src/storageService/storage.py"]
