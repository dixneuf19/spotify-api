FROM python:3.8.2

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src src

EXPOSE 80

CMD ["uvicorn", "src.main:app" , "--host", "0.0.0.0", "--port", "80"]