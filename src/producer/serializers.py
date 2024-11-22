from rest_framework import serializers
from producer.producer import send_message


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()

    def send_message(self):
        send_message(self.validated_data['message'])
