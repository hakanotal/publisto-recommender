FROM python:3.9
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY app .
CMD ["python3", "main.py"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]