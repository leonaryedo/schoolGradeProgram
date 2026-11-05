from flask import Flask                                      #파이썬으로 웹서버를 만들기 위한 flask라이브러리를 추가하기

app = Flask(__name__)                                        #

@app.get("/")
def home():
	return "grading-app is runnint!"

if __name__ ==  "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
