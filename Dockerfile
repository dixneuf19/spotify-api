FROM python:3.8-buster

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY spotifyapi spotifyapi

EXPOSE 80

CMD ["uvicorn", "spotifyapi.main:app" , "--host", "0.0.0.0", "--port", "80"]
