import RPi.GPIO as GPIO
from time import sleep
import time
from collections import deque

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
servoPin2 = 18
servoPin3 = 23
servoPin4 = 24
GPIO.setup(servoPin2, GPIO.OUT)
GPIO.setup(servoPin3, GPIO.OUT)
GPIO.setup(servoPin4, GPIO.OUT)
SERVO_MAX_DUTY = 12  # 서보의 최대(180도) 위치의 주기
SERVO_MIN_DUTY = 3  # 서보의 최소(0도) 위치의 주기
TRIG = 27
ECHO = 17
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)
time.sleep(1)
AIN1 = 12
BIN1 = 16
AIN2 = 20
BIN2 = 21
sig = deque([1, 0, 0, 0])
GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BIN2, GPIO.OUT, initial=GPIO.LOW)
servo2 = GPIO.PWM(servoPin2, 50)  # 서보 핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo2.start(0)
servo3 = GPIO.PWM(servoPin3, 50)
servo3.start(0)
servo4 = GPIO.PWM(servoPin4, 50)
servo4.start(0)

def test():
    print('aaaa')


test()