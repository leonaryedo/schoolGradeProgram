# 미션1: 내 컴퓨터에 개발자용 '작업실' 꾸미기


## 프로젝트 개요
  '손글씨 채점 프로그램(grading-app)' 을 만드는 가상의 상황을 설정하여 협업이 가능한 '작업실'꾸미기

***
### 기술 스택 
  1. 언어 및 프레임워크
     
     * 프로젝트의 메인 언어: Python 3.11-slim (이미지 처리 및 AI라이브러리 풍부)
    
       - 나의 로컬 프로젝트 폴더에는  Python 3.14 등의 최신 버전을 깔려있고, Dockerfile에는 Python 3.11-slim을 깐 이유는 개발은 최신으로 실현 및 배포는 가볍고 안정성을 구현

         ```
         [windows 검색 -> 관리자 권한으로 powershell 열기]
         wsl  --install                       #Docker 및 개발도구가 Linux에서 작동이 많이 되기에, windows에서 Linux를 사용할 수 있는 wsl 설치하기
                                              #가상 머신 플랫폼 및 Linux용 Windows 하위 시스템 기능 활성화 및 최신 리눅스 커널 다운로드, 적용을 위해서는 시스템 다시 시작 
         wsl --install                        #WSL 기능은 이미 켜져 있으므로, 그럼 기본 리눅스 배포판(보통 Ubuntu)을 다운로드해서 설치
         wsl -l -v                            #wsl의 리눅스 설치 확인하기
         wsl                                  #wsl linux환경 열기
         python3 --version                    #만약 파이썬이 없다면(보통 파이썬이 같이 깔림)
         sudo apt update
         sudo apt install python3 python3-pip python3-venv          #pip는 파이썬 전용 도구 상점, venv는 가상환경으로 여러 프로젝트가 다른 환경에서 돌아간다면 필요함
         ```
     
     * 경량 웹 프레임 워크: Flask 3.x (가볍고 빠르게 웹 서버 및 백엔드 로직 추가로 일부 프론트엔드 구현, 손글씨 시험지 업로드 및 채점 결과 반환에 사용, 라이브러리 처럼 사용하는 경량 프레임 워크)
    
       - 문제: Flask를 사용하는데... 내 컴에서 바로 사용은 안 되고 도커로 컨테이너 피키징 한 후에 깔려서 사용됨. 내 컴에서 바로 사용하려면...
      
       - 가설: Flask는 라이브러니니 install이 가능할 것이다. 그래서 pip으로 해보자
       - 해결1 실패: pip install flask(전체에 설치 되기에 이점은 가상환경을 설정하는 것도 고려할 필요가 있음. 그런데 여전히 설치가 안됨. WSL의 Python 3.14의 시스템 정책으로 안 됨. 가상환경을 하라고 에러가 뜸)
       - 가설: 프로젝트 폴더를 만들때 가상 환경을 설정하고 실시
       - 해결2:
         ```
         [해당 프로젝트 폴더 안으로 들어감]
         python3 -m venv .venv
         source .venv/bin/activate    #source는 "스크립트(파일) 안의 설정을 '현재 내 터미널 세션'에 그대로 적용해라. 파일은 activate 임
         pip install flask        #flask 등을 설치하기 또는 pip install -r requirements.txt 로 한꺼 번에 할 수 있음
         deactivate
         ```

  2. 컨테이너 및 실행 환경

     * 실행 환경 설정 프로그램: Docker 29.9.2 (컨테이너로 패키징하여 동일하게 프로그램을 개발 및 배포 가능, Linux 필요)

       - WSL2 Ubuntu (Windows에서 Linux 환경을 구성)
       
       - Docker Desktop (Windows에서 컨테이너를 관리하는 역할
                         Docker Desktop의 다운로드 파일은 컴퓨터 시스템 정보에서 확인가능
                         AMD와 ARM은 CPU의 설계 방식(아키텍처)을 의미하고, 보통 intel의 x64 또는 x86_64는 AMD이고 애플 m1 m2 m3 등은 ARM임
                         설치하는 과정에서 VMM설정에 wsl2 지정하고 못하면 나중에 setting도 가능,
                         이후에 프로그램을 열어서 setting에 들어가 WSL intergration에 체크하여 wsl - Ubuntu에서 Docker 명령어를 사용 가능하게 하기)
         ```
         [도커 설치 및 점검]
         wsl
         cd ~
         cd projects/schooGradeProgram
         docker --version
         docker info
         docker run hello-world
         docker build -t my-app-name    #Dockerfile을 읽어서 이미지 만듬
         docker run my-app-name         #위에서 만든 이미지로 컨테이너 만듬. 단, flask같은 접속 포트가 필요하면 포트 포워딩을 해야 함 docker run -p 8080:5000 my-app-name
         docker images          #이미지 목록 확인
         docker ps -a         #현재 실행중인 프로세스 ps = process status 즉, 현재 도커에서 돌아가고 있는 컨테이너 목록 확인
         ```
         <img width="1029" height="522" alt="image" src="https://github.com/user-attachments/assets/8bb56142-ea92-4e40-a727-5e650e4ed42d" />
      
         <img width="1679" height="674" alt="image" src="https://github.com/user-attachments/assets/ca288c8f-4045-4e73-9579-d9b5ccae5492" />

         <img width="1191" height="794" alt="image" src="https://github.com/user-attachments/assets/513aa737-e4fb-46e0-9192-2c1414d5f4f7" />

         <img width="1700" height="347" alt="image" src="https://github.com/user-attachments/assets/b296cc12-f30a-4011-b2f9-b380ea51f0b6" />

         ```
         [docker-compose.yml을 통한 포트매핑, 바인드마운트, 명명볼륨]
         wsl
         cd ~
         cd projects/schooGradeProgram
         docker-compose up --build -d
         curl http://localhost:8080         #포트매핑을 통한 브라우저 호출

         ```

         <img width="1176" height="76" alt="image" src="https://github.com/user-attachments/assets/37cf1acd-207f-4d65-9ebb-b8ead1e3bab1" />



  3. 버전 관리 및 협업

     * 로컬 소스코드 버전 관리: Git
    
       - Git 설치:
         ```
         wsl
         sudo apt update
         sudo apt install git
         git -v
         cd ~                          #home으로 이동
         mkdir projects
         cd projects
         cd schoolGradeProgram         #여기에서 git clone https://github.com/사용자명/grading-app.git 해도 됨. 그럼 전체 레포지토리가 복사되고 git관리가 시작됨
         git init                      #git 관리가 시작됨, git clone을 했으면 git관리가 시작되고 있음( .git의 숨겨진 파일이 있으면 git으로 관리하고 있는 곳임)
         ```
    
     * 원격 저장소, 팀 협업: GitHub
     
       - 웹에서 가입하고 레포지토리 schoolGradeProgram을 만들기, 평가를 위해서 외부에서 접근할 수 있도록 레포지토리를 public로 설정
      
       - developer setting에서 token(classic)을 발급 받아서 코디세이 코드저장소에 넣어두기, 이 토큰은 나중에 git push origin main에서도 사용됨, 자주 사용되기에 별도의 .env파일에 저장해둘 필요가 있음

  4. 개발 도구

     * 소스코드 편집기: vscode
    
       - vscode를 다운 받아서 설치, 그 과정에서 PATH에 추가 꼭 하기. 
      
       - vscode와 wsl을 연결하기 위해서 vscode의 extensions 에서 wsl을 install
      
       ```
       wsl
       cd ~
       cd projects/schoolGradeProgram
       code .                          #code명령으로 현재 폴더에서 vscode 실행함
       ```

       - 문제: wsl에서 vscode로 접근하는게 안 됨
         
       <img width="542" height="58" alt="image" src="https://github.com/user-attachments/assets/1b8bd220-ff3c-40dd-90f7-c16aace67e2b" />

       - 가설: 대부분의 프로그램이 접근이 안 되는 경우는 path문제 이므로 이를 해결하기로 함.
      
       - 해결1: windows의 시스템환경변수 편집에 해당되는 변수를 넣음. 그런데 C:\Users\leo\AppData\Local\Programs\Microsoft VS Code\bin 게 있었음.
      
       - 가설: path가 있으므로, 그럼 wsl이 가져오지 못 하는 게 아닐까?
      
       - 해결: echo $PATH | grep "VS Code"  #echo출력하라 $PATH주소록을 그리고 그걸 받아서 VS Code만 찾아서 출력해라. 그런데 반응 없음
      
       - 가설: wsl이 vscode를 가져오지 못 하다.
      
       - 해결: sudo nano /etc/wsl.conf    #wsl의 설정을 가져와서 [interop] appendwindowspath=false -> true로 변경
      
         <img width="358" height="202" alt="image" src="https://github.com/user-attachments/assets/691260f3-d269-42a2-98c2-89bfdbae6654" />

       

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
       
      사용기록 일부
    
<img width="1002" height="267" alt="image" src="https://github.com/user-attachments/assets/53c53e4e-a714-4dc5-83c2-b0c3639216c5" />


  2. 프로젝트 폴더 및 파일 권한(설정 이유: Docker 권한 문제, 서버 배포 시에 권한 문제)

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
     
  
