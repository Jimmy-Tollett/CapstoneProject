FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
ENV FLASK_APP=app.main:app
EXPOSE 8000

# --debug enables auto-reload; remove it later for prod
CMD ["flask", "run", "--host=0.0.0.0", "--port", "8000", "--debug"]
