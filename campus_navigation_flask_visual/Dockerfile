FROM python:3.10

WORKDIR /app
COPY backend /app/backend
RUN pip install -r /app/backend/requirements.txt
EXPOSE 5000
CMD ["python", "/app/backend/app.py"]