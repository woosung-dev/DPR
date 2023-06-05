import requests
# 1. 직접 입력해서 보내기
# url에 보내고자 하는 데이터를 입력해서 전송한다.
URL = "http://192.168.0.21:5000/drt/woosung"
response = requests.get(URL)
print("status code :", response.status_code)
print("status code :", response.text)

# 2. dict 이용하기
param = { "user" : "comp", "num" : 42 }
response = requests.get(URL, params=param)
print("status code :", response.status_code)
print("status code :", response.text)