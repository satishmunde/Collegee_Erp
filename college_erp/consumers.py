from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(json.dumps({"message": "WebSocket connection established!"}))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(json.dumps({"message": f"You said: {data['message']}"}))
