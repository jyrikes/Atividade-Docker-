
FROM python:3.12-slim


WORKDIR /app


COPY app.py .


RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir flask


EXPOSE 5000


CMD ["python", "app.py"]
