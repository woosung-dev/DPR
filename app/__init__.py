# Flask import
from flask import Flask, jsonify, request, render_template
import jwt
import bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import time
from camera import Camera
import cv2
import time

pin=13

# app 객체 생성
app = Flask(__name__)

# JWT 설정
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

# 라우터 설정
admin_id = "Minsu"
admin_pw = "123456"
SECRET_KEY = 'apple'


# 기본 페이지 표시 및 인증
@app.route('/')
def mainPage():
    return "<h1>Main Page</h1>"


@app.route('/signup', methods=['GET'])
def sigin_form():
    return render_template('signup.html')

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login_form.html')

@app.route('/login2', methods=['GET'])
def login_form2():
    return render_template('login.html')


@app.route("/login", methods=["POST"])  
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({'msg': '아이디 또는 비밀번호를 입력하세/요.'}), 400

    if username != admin_id and password != admin_pw:
        return jsonify({'msg': '아이디 또는 비밀번호가 일치하지 않습니다.'}), 401

    # JWT 생성
    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'msg': f'{current_user}님, 인증에 성공하셨습니다!'}), 200

@app.route('/get_camera')
def get_camera():
    get_time=time.strfrime("%Y-%m-%d%H:%M:%M:%S", time.localtime())

def gen():
    while True:
        retVale,frame =vc.read()
        fram=cv2.resize(frame,(160,120))
        retVale,frame =cv2.imencode(".jpg", frame)
        yield(b'--frame\r\n'b'Content-Type:image/jpeg\r\n\r\n'+frame.tobytes()+b'\r\n')

@app.route('/video_feed')
def get_video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace;boundary=frame')

# 비디오 스트림 테스트
@app.route('/get_data')
def get_data():
    return render_template('get_data.html')

#동적 경로 테스트
@app.route('/drt/<username>')
def hello_user(username):
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

# 웹 서버 구동
if __name__ == '__main__': # 모듈이 아니라면, 웹서버를 구동시켜라!
    app.run(host="0.0.0.0", port="5000")