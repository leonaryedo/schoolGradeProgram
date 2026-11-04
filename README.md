# 미션1: 내 컴퓨터에 개발자용 '작업실' 꾸미기


## 프로젝트 개요
  '손글씨 채점 프로그램(grading-app)' 을 만드는 가상의 상황을 설정하여 협업이 가능한 '작업실'꾸미기

***
### 기술 스택 
  1. 언어 및 프레임워크
     
     * 프로젝트의 메인 언어: Python 3.11-slim (이미지 처리 및 AI라이브러리 풍부)
    
       - 나의 로컬 프로젝트 폴더에는  Python 3.14 등의 최신 버전을 깔려있고, Dockerfile에는 Python 3.11-slim을 깐 이유는 개발은 최신으로 실현 및 배포는 가볍고 안정성을 구현) 
     
     * 경량 웹 프레임 워크: Flask 3.x (가볍고 빠르게 웹 서버 및 백엔드 로직 추가로 일부 프론트엔드 구현, 손글씨 시험지 업로드 및 채점 결과 반환에 사용, 라이브러리 처럼 사용하는 경량 프레임 워크)
    
       - 문제: Flask를 사용하는데... 내 컴에서 바로 사용은 안 되고 도커로 컨테이너 피키징 한 후에 깔려서 사용됨. 내 컴에서 바로 사용하려면...

  2. 컨테이너 및 실행 환경

     * 개발 환경: Docker 29.9.2 (컨테이너로 패키징하여 동일하게 프로그램을 개발 및 배포 가능, Linux 필요)

       - WSL2 Ubuntu 26.04.1 LTS (Windows에서 Linux 환경을 구성)
       
       - Docker Desktop (Windows에서 Docker를 관리)

  3. 버전 관리 및 협업

     * 로컬 소스코드 버전 관리: Git
    
     * 원격 저장소, 팀 협업: GitHub


### 향후 추가 기술 스택
  1. 이미지 처리

     * OpenCV 또는 Pillow (손글씨 이미지 전처리)
    
     *  EasyOCR 또는 Tesseract OCR (손글씨를 텍스트로 변환)

        - EasyOCR이 손글씨 인식은 잘 되나 용량이 크기에 requirements.txt에 easyocr(소문자)쓰게 되면 매번 docker build할 때 마다 빌드 시간이 길어질 수 있음
     
  2. 데이터 저장

     * SQLite (채점 결과, 학생 정보 등 저장)
    
  3. 프론트엔드

     * HTML, CSS, JavaScript (사용자 인터페이스 구성, Flask에 자체적으로 연결 예정)

***   
## 손글씨 채점 프로그램 (grading-app) 프로젝트의 폴더 구조와 권한 


<img width="254" height="460" alt="image" src="https://github.com/user-attachments/assets/41e4e8e0-9bef-48dc-be8c-9e8a4b00d4d8" />

  1. 프로젝트 폴더 및 파일 구조
     
     * app/(grading-app의 구현 부분)
       
       - main.py: web server(Flask)의 구현과 API엔드 포인트
      
       - grader.py: 핵심채점로직(OCR호출, 채점 로직, 채점 결과 json파일로 results/로 보내기)
      
       - utils.py: 이미지(손글씨 등) 처리를 위한 보조 함수 등
      
       - templates/: HTML파일(사용자 화면)
      
       - static/: css, js, 이미지 파일 등
      
     * data/(데이터 저장소 - 채점 할 시험지, 정답지, 채점 결과지 등)

       - test_papers/: 채점 할 시험지 저장소
      
       - answers.json: 정답지, 추후에 폴더로 바꾸어서 확인 할 필요가 있음
      
       - results/: 채점 결과지 저장소
      
     * Dockerfile: 도커 이미지 생성 설계도
    
     * docker-compose.yml: 전체 실행 설계도(포트, 볼륨 설정 등)
    
     * requirements.txt: 필요한 라이브러리 목록(Flask, Pillow, easyocr 등 작업과정에 추가 가능)
    
     * .gitignore:깃에 제외 할 목록
    
     * .dockerignore: 도커에서 제외 할 목록
    
     * .env: 개인 환경 파일

      주요 표현
       ```
       wsl --install
       wsl
       cd ~
       mkdir projects                    #폴더 만들기
       cd projects
       mkdir grading-app
       pwd                               #현재 위치 확인
       cd grading-app
       mkdir -p app/static app/templates #-p는 중간 폴더까지 한 번에 만들어 줌
       mkdir -p data/test_papers data/results
       touch app/main.py app/grader.py app/utils.py                #빈 파일 생성
       touch Dockerfile docker-compose.yml requirements.txt .gitignore .dockerignore .env
       echo "{}" > data/answers.json    #파일 없으면 파일 생성 및 덮어쓰기, >>는 이어서 쓰기
       ```

  1. 프로젝트 폴더 및 파일 권한(설정 이유: Docker 권한 문제, 서버 배포 시에 권한 문제)

     * 755 drwxr-xr-x  .
    
     * 755 drwxr-xr-x  ..
    
     * 664 -rw-rw-r--  .dockerignore
    
     * 644 -rw-r--r--  .env
    
     * 755 drwxr-xr-x  .git
    
     * 664 -rw-rw-r--  .gitignore
    
     * 664 -rw-rw-r--  Dockerfile
    
     * 775 drwxrwxr-x  app
    
     * 644 -rw-r--r--  grader.py
    
     * 644 -rw-r--r--  main.py
    
     * 644 -rw-r--r--  utils.py
    
     * 775 drwxrwxr-x  data
    
     * 644 -rw-r--r--  answers.json
    
     * 664 -rw-rw-r--  docker-compose.yml
    
     * 664 -rw-rw-r--  requirements.txt
    
      주요 표현
       ```
       find app data -type d exec chmod 775 {} \;                    #찾아라 app과 data 타입이 폴더(app data 폴더 및 그 안에 있는 모든 폴더) 그리고 실행하라 권한을 775로 바꾸기, {}에 앞에서 찾은 폴더가 들어감
       find app data -type f exec chmod 644 {} \;
       chmod 664 .dockderignore .gitignore Dockerfile docker-compose.yml requirements.txt      #권한을 바꾸어라 664로 .dockderignore .gitignore Dockerfile docker-compose.yml requirements.txt 에서 
       ``` 
     
  
