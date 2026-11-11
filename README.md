# 미션1: 내 컴퓨터에 개발자용 '작업실' 꾸미기


## 프로젝트 개요
  '손글씨 채점 프로그램(grading-app)' 을 만드는 가상의 상황을 설정하여 협업이 가능한 '작업실'꾸미기

***
## 1. 실행 환경
- OS: Ubuntu 26.04.1 LTS
  
```bash
cat /etc/os-release      #운영체제에 대한 정보가 담긴 문서를 읽기
```
- Shell: bash
- Docker: 29.9.2
```
docker -v
```
- Git: 2.53.0
```
git -v
```

## 2. 수행 체크리스트

### 가. 터미널 기본 조작 및 폴더 구성

---
    
##### 📂 1) 경로 및 파일 탐색 (Navigation)  
    
| 명령어 | 설명 | 예시 |
| :--- | :--- | :--- |
| `pwd` | 현재 작업 중인 디렉토리의 절대 경로를 출력합니다. | `pwd` |
| `ls` | 현재 디렉토리의 파일 및 폴더 목록을 출력합니다. | `ls -la` (숨김 파일 포함 상세 보기) |
| `cd` | 다른 디렉토리로 이동합니다. | `cd /var/log`, `cd ~` (홈), `cd ..` (상위) |
<img width="1204" height="183" alt="image" src="https://github.com/user-attachments/assets/3f2b8bfe-888d-4ab1-b127-fbd7abd60a89" />


##### 🛠️ 2) 파일 및 디렉토리 관리 (File & Directory Management)    

| 명령어 | 설명 | 예시 |
| :--- | :--- | :--- |
| `mkdir` | 새로운 디렉토리를 생성합니다. | `mkdir -p my_folder/sub` (하위 폴더 동시 생성) |
| `touch` | 크기가 0인 빈 파일을 생성하거나 파일의 수정 시간을 갱신합니다. | `touch index.html` |
| `cp` | 파일이나 디렉토리를 복사합니다. | `cp file.txt backup.txt`, `cp -r dir1 dir2` |
| `mv` | 파일이나 디렉토리를 이동하거나 이름을 변경합니다. | `mv old.txt new.txt` |
| `rm` | 파일이나 디렉토리를 삭제합니다. | `rm -rf target_dir` (⚠️ 주의: 강제 삭제) |
<img width="1360" height="505" alt="image" src="https://github.com/user-attachments/assets/f25b6e4d-083a-4e2d-af3d-5bfa3f56d080" />


##### 📖 3) 파일 내용 확인 (Viewing File Contents)

텍스트 파일의 내용을 터미널 창에서 확인하는 명령어입니다.

| 명령어 | 설명 | 예시 |
| :--- | :--- | :--- |
| `cat` | 파일의 전체 내용을 출력합니다. | `cat /etc/os-release` |
| `less` | 파일 내용을 페이지 단위로 끊어서 확인합니다. (종료: `q`) | `less large_file.log` |
| `head` | 파일의 **처음부터** 지정한 줄 수만큼 출력합니다. (기본 10줄) | `head -n 20 file.txt` (n = number |
| `tail` | 파일의 **마지막부터** 지정한 줄 수만큼 출력합니다. (기본 10줄) | `tail -n 20 -f /var/log/syslog` (f = follow 실시간 생성되는 자료 추적) |
<img width="1850" height="1699" alt="image" src="https://github.com/user-attachments/assets/baf935ca-6789-472f-9ccc-d0f0d4ea84e1" />


##### 🔒 4) 권한 및 관리자 제어 (Permissions & Superuser)

파일 권한을 조정하거나 관리자 권한을 획득하는 명령어입니다.

| 명령어 | 설명 | 예시 |
| :--- | :--- | :--- |
| `sudo` | 관리자(root) 권한으로 명령어를 실행합니다. | `sudo apt update` |
| `chmod` | 파일이나 디렉토리의 접근 권한을 변경합니다. | `chmod 755 script.sh` |
| `chown` | 파일이나 디렉토리의 소유자와 그룹을 변경합니다. | `chown user:user file.txt` |
<img width="1616" height="339" alt="image" src="https://github.com/user-attachments/assets/b940424c-28c1-46b7-a6f9-e93662dcdacf" />
<img width="1172" height="289" alt="image" src="https://github.com/user-attachments/assets/da0118cd-6da3-4632-ad85-42abe1a71fb4" />


##### 💻 5) 시스템 정보 및 프로세스 (System & Processes)

시스템 상태, 디스크 용량, 실행 중인 프로세스를 확인하는 명령어입니다.

| 명령어 | 설명 | 예시 |
| :--- | :--- | :--- |
| `df` | 파일 시스템의 디스크 사용량을 확인합니다. | `df -h` (Human-readable 사람이 읽기 편한 단위) |
| `du` | 특정 디렉토리의 용량을 확인합니다. | `du -sh /home` (Summarize 전체용량 + Human-readable |
| `free` | 시스템 메모리(RAM) 사용량을 확인합니다. | `free -h` |
| `ps` | 현재 실행 중인 프로세스 목록을 확인합니다. | `ps aux` ( all모든 프로세스 user-oriented사용자별 extended백그라운드까지 |
| `top` | 실시간으로 시스템 자원 사용량과 프로세스를 모니터링합니다. | `top` |
<img width="1700" height="324" alt="image" src="https://github.com/user-attachments/assets/4baa6b33-92a9-420e-a4df-ac1f7ae0a1b4" />
<img width="1453" height="362" alt="image" src="https://github.com/user-attachments/assets/783b3e45-377e-42da-83ac-e148a058f09d" />
<img width="1465" height="437" alt="image" src="https://github.com/user-attachments/assets/93bc4bd2-efa1-473e-9c45-e70500f2f21f" />

  
### 나. 권한 변경 실습

---

##### 🔐 1) 리눅스 파일 권한 (`rwx`) 및 권한 변경 (`chmod`)

리눅스(WSL/Ubuntu 포함)에서는 **다중 사용자 환경**을 안전하게 보호하기 위해 파일과 디렉터리에 **읽기, 쓰기, 실행 권한**을 엄격하게 관리합니다.

| 권한 | 기호 | 파일에서의 의미 | 디렉터리(폴더)에서의 의미 |
| :---: | :---: | :--- | :--- |
| **Read (읽기)** | `r` | 파일의 내용을 읽거나 출력할 수 있습니다. | 디렉터리 안의 **파일 목록(ls)을 조회**할 수 있습니다. |
| **Write (쓰기)** | `w` | 파일의 내용을 수정, 저장, 삭제할 수 있습니다. | 디렉터리 안에 **파일을 생성, 삭제, 이름 변경**할 수 있습니다. |
| **Execute (실행)** | `x` | 파일을 프로그램이나 스크립트로 **실행**할 수 있습니다. | 디렉터리 내부로 **진입(`cd`)**하거나 하위 경로에 접근할 수 있습니다. |

##### 👥 2) 권한 대상 (Who)

권한은 누구에게 부여하느냐에 따라 3가지 그룹으로 나뉩니다.
1. **User (u):** 파일을 소유한 **사용자(나)**
2. **Group (g):** 사용자가 속한 **그룹**
3. **Others (o):** 시스템을 쓰는 **그 외의 모든 사용자**

터미널에서 `ls -l` 명령어를 치면 다음과 같이 10글자로 표시됩니다.
> 예시: `-rwxr-xr--`
> * 첫 글자 `-`: 파일 유형 (`-`는 일반 파일, `d`는 디렉터리)
> * 앞 3글자 (`rwx`): 소유자(User) 권한
> * 중간 3글자 (`r-x`): 그룹(Group) 권한
> * 마지막 3글자 (`r--`): 기타 사용자(Others) 권한

#### 🛠️ 3) 권한 변경하기 (`chmod` 명령어)

권한을 변경할 때는 **숫자(8진수) 방식**을 사용하는 것이 가장 직관적이고 편리합니다.

🧮 8진수(숫자) 권한 계산법
각 권한에는 고유한 숫자가 부여됩니다.
* **`r` (읽기) = 4**
* **`w` (쓰기) = 2**
* **`x` (실행) = 1**
* **없음 = 0**

이 숫자들을 더해서 **[소유자][그룹][기타사용자]** 순서로 3자리의 숫자를 만들어 지정합니다.

| 권한 조합 | 합산 숫자 | 의미 |
| :---: | :---: | :--- |
| `rwx` | **7** | 읽기 + 쓰기 + 실행 모두 가능 |
| `r-x` | **5** | 읽기 + 실행 가능 (쓰기 불가) |
| `r--` | **4** | 읽기만 가능 |
| `---` | **0** | 권한 없음 |

```bash
# 실습 예제
mkdir app
touch app/my_script.sh
ls -l 
chmod 775 app
ls -l
cd app
ls -l my_script.sh
chmod 775 my_script.sh
ls -l my_script.sh
```
<img width="998" height="95" alt="image" src="https://github.com/user-attachments/assets/759ec487-7c20-4f1f-b6c4-a3d48324b3aa" />
<img width="1012" height="113" alt="image" src="https://github.com/user-attachments/assets/a3763eeb-e791-47b9-9a87-bd27fdebc100" />
<img width="1014" height="175" alt="image" src="https://github.com/user-attachments/assets/ae7698c1-74c5-4dc8-8d8b-701637148c95" />

### 다.  Docker 설치/점검

---

##### 🐳 1) Docker 버전 및 데몬(Daemon) 상태 확인 방법

WSL(Ubuntu) 환경에서 도커가 정상적으로 설치되었는지, 그리고 도커 엔진(데몬)이 현재 정상적으로 실행되어 작동하고 있는지 점검하는 방법입니다.

| 점검 항목 | 명령어 | 설명 |
| :---: | :--- | :--- |
| **Docker 버전 확인** | `docker --version` | 현재 설치된 도커 클라이언트 및 엔진의 버전을 확인합니다. |
| **Docker 데몬 상태 확인** | `docker info` | 도커 데몬의 실행 여부와 상세 시스템 정보(컨테이너 수, 스토리지 드라이버 등)를 확인합니다. |
| **서비스 상태 확인 (WSL용)** | `sudo service docker status` | WSL 우분투 내부에서 도커 백그라운드 서비스의 구동 상태를 확인합니다. |
<img width="1065" height="415" alt="image" src="https://github.com/user-attachments/assets/5363ab71-7a25-4ab2-b9a8-cc42fe38cd6d" />
<img width="1056" height="108" alt="image" src="https://github.com/user-attachments/assets/79c1442d-b84f-4fcc-ad46-9586877c0987" />

#### 🐳 2) Docker 기본 운영 명령어 및 실습 가이드

도커를 활용할 때 가장 빈번하게 사용하는 핵심 명령어들을 **이미지 관리**, **컨테이너 제어**, **운영 및 모니터링** 3가지 카테고리로 나누어 정리한 내용입니다.

  - 이미지(Image) 관리 명령어

이미지는 컨테이너를 생성하기 위한 읽기 전용 설계도입니다.

| 명령어 | 설명 | 대표적인 사용 예시 |
| :--- | :--- | :--- |
| **`docker pull`** | 원격 저장소(Docker Hub)에서 이미지 다운로드 | `docker pull nginx:latest` |
| **`docker images`** | 내 컴퓨터에 다운로드된 이미지 목록 확인 | `docker images` |
| **`docker rmi`** | 불필요한 이미지 삭제 | `docker rmi nginx` |
<img width="1470" height="737" alt="image" src="https://github.com/user-attachments/assets/b982868d-7562-4a53-aea7-b33b831f77da" />

  - 컨테이너(Container) 제어 명령어

컨테이너는 이미지를 실행하여 동작시키는 독립된 실행 공간입니다.

| 명령어 | 설명 | 대표적인 사용 예시 |
| :--- | :--- | :--- |
| **`docker run`** | 이미지를 기반으로 새로운 컨테이너 생성 및 실행 | `docker run -d -p 80:80 --name my-web nginx` |
| **`docker ps`** | 현재 **실행 중인** 컨테이너 목록 확인 | `docker ps` |
| **`docker ps -a`** | 정지된 것을 포함해 **모든** 컨테이너 목록 확인 | `docker ps -a` |
| **`docker stop`** | 실행 중인 컨테이너 안전하게 중지 | `docker stop my-web` |
| **`docker start`** | 정지된 컨테이너 다시 시작 | `docker start my-web` |
| **`docker rm`** | 중지된 컨테이너 삭제 | `docker rm my-web` |
<img width="1779" height="626" alt="image" src="https://github.com/user-attachments/assets/4ba707ab-6652-4dab-b64b-47f77c7b895e" />

  - ubuntu 컨테이너를 실행하고 내부 진입 후 간단 명령 실습
<img width="2115" height="280" alt="image" src="https://github.com/user-attachments/assets/502b1586-cb44-4134-9b08-0e6fa5bbb0c0" />
문제: ubuntu컨테이너를 실행했는데 바로 종료되는 문제 발생

해결: docker는 컨테이너 안에서 메인 프로세스가 실행되는 동안에만 유지됨.
ubuntu컨테이너해서 실행하면 쉘이 실행되나 입력받을 터미널창과 입력이 없으면 바로 종료되기에 터미널(--interactive 키보드입력을 받음, --tty 터미널 단말기)
그래서 `-it`옵션을 사용하기.
<img width="1649" height="475" alt="image" src="https://github.com/user-attachments/assets/c61c805d-d529-41b2-ba27-33f7ab08828b" />

#### 📊 3) 운영 및 모니터링 명령어

실행 중인 컨테이너의 상태를 점검하고 디버깅할 때 사용합니다.

| 명령어 | 설명 | 대표적인 사용 예시 |
| :--- | :--- | :--- |
| **`docker logs`** | 컨테이너 내부의 로그(출력 내용) 확인 | `docker logs my-web` |
| **`docker stats`** | 실시간으로 컨테이너의 자원(CPU, 메모리 등) 사용량 확인 | `docker stats` |
<img width="1471" height="363" alt="image" src="https://github.com/user-attachments/assets/18fa2b1a-ed15-4f85-8e0d-76ac78f4b5f6" />

#### 💡 4) 실전 테스트 및 결과 기록 예시 (테스트용 Nginx 실행)

가장 가벼운 테스트용 웹서버인 `nginx`를 이용해 전체 흐름을 실습하고 기록하는 예시입니다.

#### ① 이미지 다운로드 및 목록 확인
```bash
# 1. Nginx 이미지 받기
docker pull nginx

# 2. 이미지 목록 확인
docker images




- [x] hello-world 실행
- [x] Dockerfile 빌드/실행
- [x] 포트 매핑 접속(2회)
- [x] 바인드 마운트 반영
- [x] 볼륨 영속성
- [x] Git 설정 + VSCode GitHub 연동

 ## 3) 수행 로그(발췌)
bash$ pwd
/home/user
$ mkdir -p ~/codyssey/practice
$ ls -la
...
   



# 미션1을 실전처럼 바꾸기: 내 컴퓨터에 개발자용 '작업실'로 '손글씨 채점 프로그램' 만들기


## 프로젝트 개요
  '손글씨 채점 프로그램(grading-app)' 을 만드는 가상의 상황을 설정하여 협업이 가능한 '작업실'꾸미기


## 기술 스택 
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
     
  
