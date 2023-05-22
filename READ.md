# smart disaster prevention robot
- disaster prevention robot 이라는 주제의 서버 역할을 맡은 레포지토리이다.

# 가상환경
- 호불호에 따라 다르지만 주로 pipenv, virualenv가 주로 사용된다고 알고 있다.
- 해당 프로제트에서는 node.pack 등에 같은 방식인 pipenv를 사용해보고 싶다는 생각이 들었고, 뭔가 좀 더 직관적인 느낌이다.

## install pipenv
`pipenv`를 사용하면 `pip freeze`으로 남겨주었던 `requirements.txt`를 나기지 않고도 `pipfile`으로 자동으로 남는다. 장점이라고 생각함

```
 $ pip3 install pipenv # 설치되어있지 않을시
 $ pipenv shell # 가상환경을 자동으로 만들어주고 실행
 (가상환경 이름) $ pipenv install [package_name] # 가상환경 내에 설치
```

## pipfile
설치를 하면, 같은 경로 내의 pipfile로 저장이 된다.

# 파일 구조
- 프로구젝트 구조는 업데이트 ... 중


## 구조

# DB
- mysql을 사용한다.
- db-config로 따로 관리한다.

