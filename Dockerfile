FROM python:3-slim

WORKDIR /usr/src/app

COPY app ./
RUN pip install fastapi uvicorn

COPY . .

EXPOSE 9001

CMD ["uvicorn", "--host", "0.0.0.0",  "--port", "9001", "app.main:app"]
