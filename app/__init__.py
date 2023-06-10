# Flask import
from flask import Flask, jsonify, request, render_template, session, redirect
from camera import Camera
import time
import psycopg2
import cv2
import time

pin=13

# app 객체 생성
app = Flask(__name__)

# secret_key 설정
app.secret_key = 'your_secret_key'

# 데이터베이스 연결 함수
def connect_db():
    conn = psycopg2.connect(database='bota',
                            user='postgres',
                            password='postgres',
                            host='127.0.0.1',
                            port=5432)
    return conn

# 기본 페이지 표시 및 인증
@app.route('/')
def mainPage():
    username = ''
    if 'username' in session:
        username = session['username']
    return render_template('home.html', user=username)

# DB test
@app.route('/select')
def mainPage2():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM b_user;")
    records = cur.fetchall()

    result = ''
    for row in records:
        result += f"{row}<br>"

    return result

@app.route('/signup', methods=['GET'])
def sigin_form():
    return render_template('signup.html')

def gen():
    while True:
        retVale,frame =vc.read()
        fram=cv2.resize(frame,(160,120))
        retVale,frame =cv2.imencode(".jpg", frame)
        yield(b'--frame\r\n'b'Content-Type:image/jpeg\r\n\r\n'+frame.tobytes()+b'\r\n')

@app.route('/video_feed')
def get_video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace;boundary=frame')

# camera
@app.route('/camera')
def get_data():
    return render_template('camera.html')

#동적 경로 테스트
@app.route('/drt/<username>')
def hello_user(username):
    var1=request.args
    print(var1)
    for key,value in var1.items():
        print(key,value)

    return render_template('index.html', user=username)

# caemra 구현 부분
@app.route('/video_feed')
def video_feed():
   return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')
def gen(camera):
   while True:
       frame = camera.get_frame()
       yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# caemra 구현 부분2
@app.route('/video_feed2')
def video_feed2():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
def generate_frames():
    video = cv2.VideoCapture(0)  # Change 0 to the video file path if streaming from a file
    
    while True:
        success, frame = video.read()
        if not success:
            break
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 로그인 처리 로직
        username = request.form['username']
        password = request.form['password']
        
        # 로그인 성공 시 세션에 사용자 정보 저장
        session['username'] = username
        return redirect('/')
    
    return '''
        <form method="post" action="/login">
            <input type="text" name="username" placeholder="Username"><br>
            <input type="password" name="password" placeholder="Password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# 마이페이지
@app.route('/mypage')
def homeTes():
    username = ''
    if 'username' in session:
        # 세션에 사용자 정보가 있으면 로그인 상태로 간주
        username = session['username']
    return render_template('mypage.html', user=username)

# 로그아웃
@app.route('/logout')
def logout():
    # 세션에서 사용자 정보 제거
    session.pop('username', None)
    return redirect('/')

# 웹 서버 구동
if __name__ == '__main__': # 모듈이 아니라면, 웹서버를 구동시켜라!
    app.run(host='0.0.0.0',port = '5000',debug=True)