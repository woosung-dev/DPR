##########--로봇팔_최종코드_서보/스텝/초음파--##########
# 역기구학 (x, y, z) 좌표 -> (객체인식 x 좌표 , 초음파 거리 값, 객체인식 y 좌표)
# x, z = 모터 3, 4번(서보) / y = 모터 1번(스텝)

#####--초기 설정--#####
import RPi.GPIO as GPIO
from time import sleep
import math
import time
from collections import deque

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#서보모터
servoPin2 = 18  # 손
servoPin3 = 23
servoPin4 = 24

GPIO.setup(servoPin2, GPIO.OUT)
GPIO.setup(servoPin3, GPIO.OUT)
GPIO.setup(servoPin4, GPIO.OUT)
max_duty = 12.5  # 서보의 최대(180도) 위치의 주기
min_duty = 2.5  # 서보의 최소(0도) 위치의 주기

servo2 = GPIO.PWM(servoPin2, 50)
servo2.start(0)
servo2.ChangeDutyCycle(2.5)

servo3 = GPIO.PWM(servoPin3, 50)
servo3.start(0)  # PWM 신호 시작
servo3.ChangeDutyCycle(2.5)  # 듀티 사이클 변경

servo4 = GPIO.PWM(servoPin4, 50)
servo4.start(0)  # PWM 신호 시작
servo4.ChangeDutyCycle(12.5)  # 듀티 사이클 변경

# 일정 시간 대기
time.sleep(1)

#초음파
TRIG = 27
ECHO = 17
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)
time.sleep(1)

# 스텝모터
AIN1 = 12
BIN1 = 16
AIN2 = 20
BIN2 = 21
sig = deque([1, 0, 0, 0])
GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BIN2, GPIO.OUT, initial=GPIO.LOW)

# 팔 길이
L0 = 10
L1 = 5.0
L2 = 5.0

x = 0
y = 0
z = 0

# 초기 위치
angle1 = 0
angle2 = 0

distance = None

def Distance():
   
    cnt = 0
   
    while (cnt == 0):
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
        cnt += 1
#         if distance < 10 :
#             break
    return distance



def convert_to_range(value, width=640, range_start=1, range_end=9):
    ratio = (value - 0) / (width - 0)
    converted_value = range_start + (range_end - range_start) * ratio
    return round(converted_value)

# 로봇 팔 제어 함수 (어깨 / y값)
def move_robot_arm_A():,
    l = convert_to_range(y, 480, 1, 10)
    print("목표 y 좌표 입력 (cm): ", l)
   
    if l > 0:
        theta = math.acos((L0^2) / (2 * L0**2))
        angle0 = math.degrees(theta)
        # y값에 따라 스텝모터 회전 방향 설정
        step = 0
        while step < angle0:  
       
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
       
        sleep(1)
       
    else:
        y = abs(y)
        theta = math.acos((L0^2) / (2 * L0**2))
        angle0 = math.degrees(theta)
        # y값에 따라 스텝모터 회전 방향 설정
        step = 0
        while step < angle0:  
       
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
       
        sleep(1)

# 로봇 팔 제어 함수 (팔꿈치, 손목 / x, z값)
def move_robot_arm_B():
   
#     print("//////")
    distance = Distance()

    # 사용자로부터 x, z 값을 키보드로 입력받음
#     x = float(input("목표 x 좌표 입력 (cm): "))
    k = convert_to_range(x)
    print("목표 x 좌표 입력 (cm): ", k)
    if (distance < 10):
        z = Distance()
        print("목표 z 좌표 입력 (cm): ", z)
    else:
        z = 5
        print("목표 z 좌표 입력 (cm): ", z)
       
       
    #역기구학 계산
    r = math.sqrt(x**2 + z**2)
    theta2 = math.acos((L1**2 + L2**2 - (x**2) - (z**2)) / (2 * L1 * L2))
    theta1 = math.atan2(z, x) - math.atan2(L1 * math.sin(theta2), 2 * L1 * math.cos(theta2))

    # 관절 각도 계산 (라디안값에서 각도값으로 변경)
    angle1 = math.degrees(theta1)
    angle2 = math.degrees(theta2)

    # 관절1 제어
    GPIO.setup(servoPin3, GPIO.OUT)
    servo3.start(0)  # PWM 신호 시작

    duty1 = angle1 * (12.5 - 2.5) / (angle1 + 2.5)  # 각도를 PWM 듀티 사이클로 변환
    servo3.ChangeDutyCycle(duty1)  # 듀티 사이클 변경

    # 관절2 제어
    GPIO.setup(servoPin4, GPIO.OUT)
    servo4.start(0)  # PWM 신호 시작

    duty2 = angle2 * (12.5 - 2.5) / (angle2 + 2.5)  # 각도를 PWM 듀티 사이클로 변환
    servo4.ChangeDutyCycle(duty2)  # 듀티 사이클 변경

    # 일정 시간 대기
    time.sleep(1)
 
    # 초기화
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPin3, GPIO.OUT)
    GPIO.setup(servoPin4, GPIO.OUT)

def hand():
    servo2.start(0)
    servo2.ChangeDutyCycle(7.5)
    sleep(3)
    servo2.start(0)
    servo2.ChangeDutyCycle(2.5)
    sleep(2)
   
def original_deg_servo():
    servo3.start(0)  # PWM 신호 시작
    servo3.ChangeDutyCycle(2.5)  # 듀티 사이클 변경
    sleep(1)
   
    servo4.start(0)  # PWM 신호 시작
    servo4.ChangeDutyCycle(12.5)  # 듀티 사이클 변경
    sleep(1)
   
   
def original_deg_step():
    sig = deque([1, 0, 0, 0])
    GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BIN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BIN2, GPIO.OUT, initial=GPIO.LOW)
    sleep(1)


try:
    while True:
        # 로봇 팔 이동
        print("///동작 실행///")
        move_robot_arm_A()
        move_robot_arm_B()
        hand()        
        original_deg_servo()
        original_deg_step()
        print("///동작 종료///")
       
except KeyboardInterrupt:
    pass

# 종료 시 GPIO 해제
GPIO.cleanup()