FROM python:3.6

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY sp/ ./sp
COPY beers/ ./beers
COPY fifarank ./fifarank
COPY blog/ ./blog
COPY accounts/ ./accounts
COPY manage.py .

EXPOSE 8000
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
