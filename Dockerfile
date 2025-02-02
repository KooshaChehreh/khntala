FROM python:3.13  

# RUN mkdir /app

WORKDIR /app
 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
RUN pip install --upgrade pip 
 
COPY requirements.txt  /app/requirements.txt
 
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . /app
 
EXPOSE 80

CMD ["gunicorn", "--reload", "--workers=4", "--worker-tmp-dir", "/dev/shm", "--bind=0.0.0.0:80", "--chdir", "/app/khanetala", "khabetala.wsgi"]