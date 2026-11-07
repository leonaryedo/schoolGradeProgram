from flask import Flask                                      #파이썬으로 웹서버를 만들기 위한 flask라이브러리를 추가하기
import os
from datetime import datetime


app = Flask(__name__)                                        #파이썬이 해당 파일을 직접 실행한 상황이면 파이썬 내장변수인 __name__에는 "__main__"이 입력된다
                                                             #다른 파일(예: app.py)에서 flask가 있는 파일(web.py)이 import해서 시작이 되었다면 __name__ 내장변수에는 "web" 즉 해당파일의 이름이 들어간다.
@app.get("/")												 #데코레이터로 브라우저에 / 홈주소  http://localhost:8080/ 접속을 하면 아래 함수 실행
def home():
	return "grading-app is running!"

@app.get("/create-test-data")								 #새로운 엔드 포인트 생성
def creat_test_data():										 #브라우저에 접속하면  /data 디렉토리에 파일 생성				
	data_dir = "/data/results"								 #컨테이너 상에서 저장할 위치 변수에 넣기, 왜냐하면 app.py가 컨테이너 안에서 작동하기에 생성된 데이터도 컨테이너 상에서 저장할 위치를 만들고 이후에 named volumns를 통해서 지정된 외부의 저장소에 저장됨. 
	os.makedirs(data_dir, exist_ok=True)					 #폴더만들기, exist_ok=True는 폴더가 있어도 에러 안 남

	test_file = os.path.join(data_dir, "grades.txt")		 #os.path.join은 단순히 경로를 만드는 함수이나 os에 맞추어 수정함(예: Linux /, Windows \). 그리고 경로를 조합할 때 중복 오타 실수 줄임(예: /data/results//grades.txt). 그래서 만들어 지는 것은 test_file = "/data/results/grades.txt"
	with open(test_file, "w") as f:							 #with 리소스 open(test_file, "w") as f 획득 후에 블록이 끝나면 자동으로 파일 닫기 f.close() 실행, open(파일명, "w") 파일이 없으면 생성해서 파일에 (덮어)쓰기 모드로 열기, as f 열린 파일을 변수 f에 저정
		f.write(f"Grading App Test Data\n")					 #위에서 open으로 쓰기 모드로 열어 놓은 상태에서 이어서 쓰기 f.write(f"  ") 실시
		f.write(f"Created at: {datetime.now()}\n")
		f.write(f"this file demonstates data persistence.\n")

	return f" Test file crested at {test_file}"

if __name__ ==  "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)           #host="0.0.0.0"는 접속의 허용 범위로 내 컴퓨터는 127.0.0.1(localhost)인데 0.0.0.0으로 하면 내 컴퓨터가 접속한 네트워크를 통해서 모두 접속이 가능하다는 의미임
	                                                         #보통은 Flask는 보통 5000을 쓰기에 서버에는 5000포트를 통해서 접속이 가능하다는 말임. 
															 #이것은 도커는 docker-compose.yml에서 작성한데로 외부 브라우저 8080번이 접속하면 컨테이너 내부의 5000번에 연결하고 다시 이 5000번을 통해서 FLask 서버에 연결이 된다는 뜻임.
															 #debug=True는 코드를 수정하고 저장(Ctrl + S)하면, 서버를 껐다 켜지 않아도 Flask가 알아서 수정된 내용을 반영. 
