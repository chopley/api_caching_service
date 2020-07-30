FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install --upgrade pip
RUN pip install requests requests_cache config redis python-dotenv
