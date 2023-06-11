#동적 경로 테스트
from flask import Flask, jsonify, request, render_template, session, redirect, Response


app = Flask(__name__)

@app.route('/drt/<username>')
def hello_user(username):
    print('Hello')
    var1=request.args
    x1=1
    x2=1
    y1=1
    y2=1
    h=1
    w=1

    print(var1)
    for key,value in var1.items():
        print(key,value)
        if key == 'x1':
            x1 = float(value)
        elif key == 'x2':
            x2 = float(value)
        elif key == 'y1':
            y1 = float(value)
        elif key == 'y2':
            y2 = float(value)
        elif key == 'w':
            w = float(value)
        elif key == 'h':
            h = float(value)

    print('x', (x1+x2)/2, 'y', (y1+y2)/2, 'w', w, 'h', h)
    return render_template('server2_main.html', x=(x1+x2)/2, y=(y1+y2)/2, h=h, w=w)


# 웹 서버 구동
if __name__ == '__main__': # 모듈이 아니라면, 웹서버를 구동시켜라!
    app.run(host='0.0.0.0',port = '5001',debug=True)