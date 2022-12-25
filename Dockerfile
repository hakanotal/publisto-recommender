FROM python:3.9
WORKDIR /code
COPY requirements.txt .
RUN CLFAGS='-g0 -Wl -I/usr/include:/usr/local/include -L/usr/lib:/usr/local/lib' pip install --global-option=build_ext -r requirements.txt
COPY app .
RUN cd app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]