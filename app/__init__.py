# Flask import
from flask import Flask, jsonify, request, render_template
import jwt
import bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# app 객체 생성
app = Flask(__name__)

# JWT 설정
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

# 라우터 설정
admin_id = "Minsu"
admin_pw = "123456"
SECRET_KEY = 'apple'

@app.route('/')
def mainPage():
    return "<h1>Main Page</h1>"

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


# 웹 서버 구동
if __name__ == '__main__': # 모듈이 아니라면, 웹서버를 구동시켜라!
    app.run(host="127.0.0.1", port="8080")