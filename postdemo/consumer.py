import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CoilConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            "message": "WebSocket connection established!"
        }))

    async def receive(self, text_data):
        data = json.loads(text_data)
        coil_name = data.get("coil_name", "Unknown Coil")
        weight = data.get("weight", 0)

        await self.send(text_data=json.dumps({
            "status": "Received from frontend",
            "coil_name": coil_name,
            "weight": weight
        }))

    async def disconnect(self, close_code):
        print("WebSocket disconnected:", close_code)
