FROM python:3.11-slim
WORKDIR /code
COPY . /code/
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
WORKDIR /code/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]