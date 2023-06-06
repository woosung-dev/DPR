# 희수님 코드
# 라즈베리 파이 2 서브 모트 부분 코드

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
servo4.start(0)  # 서보 PWM 시작, duty = 0이면 서보는 동작하지 않는다.

def setServoPos(servo, degree):
    # 각도는 180도를 넘을 수 없다.
    if degree > 180:
        degree = 180
    duty = SERVO_MIN_DUTY + (degree * (SERVO_MAX_DUTY - SERVO_MIN_DUTY) / 180.0)
    print("Degree: {} to {}(Duty)".format(degree, duty))
    servo.ChangeDutyCycle(duty)

def Distance():
    while True:
        stop = 0
        start = 0
        GPIO.output(TRIG,True)
        time.sleep(0.00001)        # 10uS의 펄스 발생을 위한 딜레이
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
            start = time.time()     # Echo핀 상승 시간값 저장
        while GPIO.input(ECHO)==1:
            stop = time.time()      # Echo핀 하강 시간값 저장
        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance : %.1f cm" % distance)
        time.sleep(0.1)
        if distance < 10 :
            break

def Step_45():
    step = 0
    while step < 230:
        GPIO.output(AIN1, sig[0])
        GPIO.output(BIN1, sig[1])
        GPIO.output(AIN2, sig[2])
        GPIO.output(BIN2, sig[3])
        time.sleep(0.01)
        sig.rotate(1)
        step += 1
    GPIO.output(AIN1, 0)
    GPIO.output(BIN1, 0)
    GPIO.output(AIN2, 0)
    GPIO.output(BIN2, 0)

def Step_90():
    step = 0
    while step < 465:
        GPIO.output(AIN1, sig[0])
        GPIO.output(BIN1, sig[1])
        GPIO.output(AIN2, sig[2])
        GPIO.output(BIN2, sig[3])
        time.sleep(0.01)
        sig.rotate(1)
        step += 1
    GPIO.output(AIN1, 0)
    GPIO.output(BIN1, 0)
    GPIO.output(AIN2, 0)
    GPIO.output(BIN2, 0)

def Step_135():
    step = 0
    while step < 695:
        GPIO.output(AIN1, sig[0])
        GPIO.output(BIN1, sig[1])
        GPIO.output(AIN2, sig[2])
        GPIO.output(BIN2, sig[3])
        time.sleep(0.01)
        sig.rotate(1)
        step += 1
    GPIO.output(AIN1, 0)
    GPIO.output(BIN1, 0)
    GPIO.output(AIN2, 0)
    GPIO.output(BIN2, 0)

def Step_45_reverse():
    step = 0
    while step < 230:
        GPIO.output(AIN1, sig[0])
        GPIO.output(BIN1, sig[1])
        GPIO.output(AIN2, sig[2])
        GPIO.output(BIN2, sig[3])
        time.sleep(0.01)
        sig.rotate(-1)
        step += 1
    GPIO.output(AIN1, 0)
    GPIO.output(BIN1, 0)
    GPIO.output(AIN2, 0)
    GPIO.output(BIN2, 0)

def Step_90_reverse():
    step = 0
    while step < 465:
        GPIO.output(AIN1, sig[0])
        GPIO.output(BIN1, sig[1])
        GPIO.output(AIN2, sig[2])
        GPIO.output(BIN2, sig[3])
        time.sleep(0.01)
        sig.rotate(-1)
        step += 1
    GPIO.output(AIN1, 0)
    GPIO.output(BIN1, 0)
    GPIO.output(AIN2, 0)
    GPIO.output(BIN2, 0)

def Step_135_reverse():
    step = 0
    while step < 695:
        GPIO.output(AIN1, sig[0])
        GPIO.output(BIN1, sig[1])
        GPIO.output(AIN2, sig[2])
        GPIO.output(BIN2, sig[3])
        time.sleep(0.01)
        sig.rotate(-1)
        step += 1
    GPIO.output(AIN1, 0)
    GPIO.output(BIN1, 0)
    GPIO.output(AIN2, 0)
    GPIO.output(BIN2, 0)

def Case1():
    setServoPos(servo2, 45)
    setServoPos(servo3, 0)
    setServoPos(servo4, 45)
    sleep(1)

def Case2():
    setServoPos(servo2, 0)
    setServoPos(servo3, 0)
    setServoPos(servo4, 95)
    sleep(1)

def Case3():
    setServoPos(servo2, 45)
    setServoPos(servo3, 85)
    setServoPos(servo4, 0)
    sleep(1)


# 메인 무한 반복
try:
    while True:
        choice = int(input(" choice : "))
        if choice == 0:
            Distance()
        elif choice == 1:
            Step_45()
        elif choice == 2:
            Step_90()
        elif choice == 3:
            Step_135()
        elif choice == 4:
            Step_45_reverse()
        elif choice == 5:
            Step_90_reverse()
        elif choice == 6:
            Step_135_reverse()
        elif choice == 7:
            Case1()
            servo2.start(0)
            servo3.start(0)
            servo4.start(0)
        elif choice == 8:
            Case2()
            servo2.start(0)
            servo3.start(0)
            servo4.start(0)
        elif choice == 9:
            Case3()
            servo2.start(0)
            servo3.start(0)
            servo4.start(0)
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
    servo2.stop()
    servo3.stop()
    servo4.stop()
except KeyboardInterrupt:
    pass

GPIO.cleanup()