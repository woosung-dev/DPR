from flask import Flask, render_template, Response
import cv2
import requests

app = Flask(__name__)

def generate_frames():
    camera = cv2.VideoCapture(0)  # Use the appropriate camera index if not the default
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


def gen_frames():
    while True:
        # get에 clinet ip를 넣기
        response = requests.get("http://raspberry_pi_2_address:5001/video_feed", stream=True)
        if not response:
            break
        else:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + chunk + b'\r\n')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
