FROM python:3.13-slim 
RUN pip install --upgrade pip
RUN groupadd -r todogroup && useradd -r -g todogroup todouser 
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
USER todouser
EXPOSE 8080 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
