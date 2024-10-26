import asyncio
import websockets
import json
import random

async def send_data_periodically():
    url = "ws://localhost:5236/ws/dumptruck"
    
    async with websockets.connect(url) as websocket:
        while True:
            # Команда "update" с полным набором данных
            data = {
            "Command": "update",
            "Name": "Самосвал-01",
            "StateNumber": "АБВ123",
            "TypeTransport": 1,  
            "FuelLevel": random.uniform(0, 100),  
            "DistanceToTarget": random.uniform(0, 500),  
            "MaxLoadCapacity": 10.0,  
            "CurrentLoadWeight": random.uniform(0, 10),  
            "CargoName": "Уголь",  
            "Speed": random.uniform(0, 90),  
            "Throttle": random.uniform(0, 1), 
            "Brake": random.uniform(0, 1),  
            "Steer": random.uniform(-1, 1),  
            "DistanceToNearestVehicle": random.uniform(0, 100), 
            "Latitude": 52.5200 + random.uniform(-0.01, 0.01), 
            "Longitude": 13.4050 + random.uniform(-0.01, 0.01),  
            "Altitude": random.uniform(0, 50),  
            "LocalX": random.uniform(0, 100),  
            "LocalY": random.uniform(0, 100), 
            "LocalZ": random.uniform(0, 10), 
            "CurrentStatusName": "Активен",
            "StatusDescription": "Работоспособен"  
        }
            json_data = json.dumps(data)
            await websocket.send(json_data)

            response = await websocket.recv()
            print(f"Получен ответ от сервера: {response}")
            request_data = {
                "Command": "get",
                "StateNumber": "ABC123"
            }
            json_request = json.dumps(request_data)
            await websocket.send(json_request)
            print(f"Отправлен запрос на получение данных: {json_request}")
            
            server_response = await websocket.recv()
            print(f"Получен ответ на запрос данных: {server_response}")

            await asyncio.sleep(1)  


asyncio.get_event_loop().run_until_complete(send_data_periodically())
