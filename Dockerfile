FROM python:3.9
WORKDIR /shark
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 5001
COPY . .
CMD ["python3", "-m", "shark"]