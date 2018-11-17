import socket
import json
import asyncio
from threading import Thread

async def sendData(dataJson):
    reader, writer = await asyncio.open_connection('127.0.0.1',5005)
    
    writer.write(json.dumps(dataJson).encode())
    writer.close()