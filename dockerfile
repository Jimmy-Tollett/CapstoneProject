FROM python:3.11-slim
WORKDIR /capstone
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
ENV FLASK_APP=app.main:app
EXPOSE 8000

# --debug enables auto-reload; remove it later for prod
CMD ["python", "app/main.py"]
