FROM python:3.8

WORKDIR /test_actions

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3001

CMD ["python", "main.py"]