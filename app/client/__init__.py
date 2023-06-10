from flask import Flask, Response
import cv2

app = Flask(__name__)

# 영상 처리 함수
def processed_frames():
    # 카메라 및 영상 처리 로직을 여기에 구현하세요
    while True:
        # ... 카메라로부터 프레임 읽기
        # ... 영상 처리 수행
	yield processed_frame

@app.route('/video_feed')
def video_feed():
    return Response(processed_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)