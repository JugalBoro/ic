FROM python:3.8-slim
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
WORKDIR /src
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]