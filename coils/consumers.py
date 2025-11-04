import json
import random
from channels.generic.websocket import AsyncWebsocketConsumer

class CoilConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send_random_data()

    async def send_random_data(self):
        statuses = ['Produced', 'Quality Hold', 'Ready for Dispatch', 'In Dispatch']
        data = []

        for i in range(20):
            data.append({
                "coil_id": f"A{i:03d}",
                "status": random.choice(statuses)
            })

        await self.send(text_data=json.dumps(data))

