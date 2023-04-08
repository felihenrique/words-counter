FROM python:3.8.2

COPY . .

RUN pip install -r requirements.txt

EXPOSE 7600

CMD ["gunicorn", "--bind=0.0.0.0:7600", "--workers=4", "app:app"]