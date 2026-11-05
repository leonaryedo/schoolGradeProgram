#단일 컨테이너를 만들기 위한 레시피
FROM python:3.11-slim               #가져와 python:3.11-slim이 설치된 리눅스 환경을 

WORKDIR	 /app                       #컨테이너 안에서 작업할 공간은 /app 즉, 최상위 폴더에 있는 app임

COPY requirements.txt /tmp/requirements.txt        #복사해라 내 작업 프로젝트의 requirements.txt를 /tmp/requirements.txt로 
RUN pip install --no-cache-dir -r /tmp/requirements.txt   #실행해라 ,--no-cache-dir 설치 중에 생기는 임시 파일들을 남기지 않겠다는 뜻, -r 읽어라 /tmp/requirements.txt

COPY app/ /app/                     #복사해라 내 작업 프로젝트의 app/을 /app/으로

COPY data/ /data/                   #복사해라 내 작업 프로젝트의 data/을 /data/으로

EXPOSE 5000                         #이 컨테이너는가 사용할 포트는  5000번 포트

CMD ["python", "main.py"]          # 컨테이너가 딱 켜지는 순간 명령어를 실행해라 python main.py 
