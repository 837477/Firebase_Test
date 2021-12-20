from firebase_admin import (initialize_app,
                            messaging,
                            delete_app,
                            get_app)


class FirebaseAdmin:
    def __init__(self):
        self.app = initialize_app()
        self.message = {
            'title': None,
            'body': None
        }

    def send_single(self, token: str, title, body):
        """
        특정 기기에 메시지 전송
        :param token: 특정 기기 토큰
        :param title: 푸시 알림 제목
        :param body: 푸시 알림 내용
        :return: 결과
        """
        self.message['title'] = title
        self.message['body'] = body
        message = messaging.Message(
            self.message,
            token=token
        )
        result = messaging.send(message)
        return result

    def send_multi(self, tokens: list, title, body):
        """
        여러 기기에 메시지 전송
        :param tokens: 특정 기기 토큰 리스트
        :param title: 푸시 알림 제목
        :param body: 푸시 알림 내용
        :return: 결과
        """
        self.message['title'] = title
        self.message['body'] = body
        message = messaging.MulticastMessage(
            data=self.message,
            tokens=tokens,
        )
        result = messaging.send_multicast(message)
        return result

    def send_topic(self, topic: str, title, body):
        """
        Topic(주제)로 메시지 전송
        :param topic: 주제
        :param title: 푸시 알림 제목
        :param body: 푸시 알림 내용
        :return: 결과
  과     """
        self.message['title'] = title
        self.message['body'] = body
        message = messaging.Message(
            data=self.message,
            topic=topic
        )
        """
        # 조건으로 보내는 방법
        condition = "'test' in topics || 'test_2' in topics"
        message = messaging.Message(
            notification=messaging.Notification(
                title=self.message['title'],
                body=self.message['body']
            ),
            condition=condition
        )
        """
        result = messaging.send(message)
        return result

    def send_all(self, token: str, title, body):
        messages = [
            messaging.Message(
                notification=messaging.Notification('Price drop', '5% off all electronics'),
                token=token,
            ),
            # ...
            messaging.Message(
                notification=messaging.Notification('Price drop', '2% off all books'),
                topic='readers-club',
            ),
        ]
        result = messaging.send_all(messages)
        return result

    def __del__(self):
        delete_app(self.app)
