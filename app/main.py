from flask import Flask                                      #파이썬으로 웹서버를 만들기 위한 flask라이브러리를 추가하기

app = Flask(__name__)                                        #파이썬이 해당 파일을 직접 실행한 상황이면 파이썬 내장변수인 __name__에는 "__main__"이 입력된다
                                                             #다른 파일(예: app.py)에서 flask가 있는 파일(web.py)이 import해서 시작이 되었다면 __name__ 내장변수에는 "web" 즉 해당파일의 이름이 들어간다.
@app.get("/")												 #데코레이터로 브라우저에 / 홈주소  http://localhost:8080/ 접속을 하면 아래 함수 실행
def home():
	return "grading-app is runnint!"

if __name__ ==  "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)           #host="0.0.0.0"는 접속의 허용 범위로 내 컴퓨터는 127.0.0.1(localhost)인데 0.0.0.0으로 하면 내 컴퓨터가 접속한 네트워크를 통해서 모두 접속이 가능하다는 의미임
	                                                         #보통은 Flask는 보통 5000을 쓰기에 서버에는 5000포트를 통해서 접속이 가능하다는 말임. 
															 #이것은 도커는 docker-compose.yml에서 작성한데로 외부 브라우저 8080번이 접속하면 컨테이너 내부의 5000번에 연결하고 다시 이 5000번을 통해서 FLask 서버에 연결이 된다는 뜻임.
															 #debug=True는 코드를 수정하고 저장(Ctrl + S)하면, 서버를 껐다 켜지 않아도 Flask가 알아서 수정된 내용을 반영. 
