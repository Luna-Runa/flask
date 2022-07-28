FROM python:3.10.5

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/src
#위 과정중 도커 내부에도 똑같이 /src 폴더가 생김

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=4000"]
#이 앱은 도커 내부의 localhost에서 실행되기 때문에 컨테이너 외부에서 서비스를 사용하기 위해