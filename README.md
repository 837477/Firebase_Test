# Firebase Test
<br><br>

<div align=center>
    <strong># Python</strong> &nbsp;
    <strong># Kotlin</strong> &nbsp;
    <strong># Firebase</strong> &nbsp;
</div>
<br>

## What is this?
어플리케이션에 Push 알람을 보내주는 로직을 테스트한 레파지토리입니다.

Firebase Message Cloud는 다음과 같이 두 개의 라이브러리를 통하여 사용할 수 있습니다.
- FCM
- firebase_admin (권장)

Google에서 지원하는 firebase_admin 라이브러리를 사용하는 것을 권장합니다.

#### 테스트 항목
- 특정 기기에 메시지 전송
- 여러 기기에 메시지 전송
- Topic(주제)로 메시지 전송
- 다중 조건으로 메시지 전송

<br>

## Dependency
```shell
python 3.8.X
Kotlin 1.4.X
```
<br>

## How to use
```shell
# Environments
export FMC_FIREBASE_API_SECRET_KEY="<Google Console API Secret KEY>"
export GOOGLE_APPLICATION_CREDENTIALS="<Google Console Service Account Key.json Path>"
```
```shell
# Run
pip install -r requirements.txt
uvicorn main:app --reload --host=0.0.0.0 --port=80
```
<br>

## About Me
🙋🏻‍♂️ Name: 837477

📧 E-mail: 8374770@gmail.com

🐱 Github: https://github.com/837477

<br>

## Contributing
1. Fork this repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -m 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
