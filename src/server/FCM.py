from pyfcm import FCMNotification


class FCM:
    def __init__(self, api_key):
        self.api_key = api_key
        self.push_service = FCMNotification(self.api_key)
        self.message = {
            'title': None,
            'body': None
        }

    def send_single(self, token, title, body):
        self.message['title'] = title
        self.message['body'] = body
        result = self.push_service.single_device_data_message(
            registration_id=token,
            data_message=self.message
        )
        return result

    def send_multi(self, title, body):
        self.message['title'] = title
        self.message['body'] = body
        result = self.push_service.notify_topic_subscribers(
            topic_name="test",
            data_message=self.message
        )
        return result