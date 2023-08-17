import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class PickConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'pick_group'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'pick_message',
                'message': message
            }
        )

        
    def pick_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'pick',
            'message': message
        }))

class TimerConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'timer_group'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'timer_message',
                'message': message
            }
        )

        
    def timer_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'timer',
            'message': message
        }))