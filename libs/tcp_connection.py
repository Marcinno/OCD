import socket
import json
import asyncio
from threading import Thread

#testing section
P = 1
C = 3
dataJson = {
    '1' : P,
    '2' : C,
}
#testing section

async def sendData(dataJson):
    reader, writer = await asyncio.open_connection('127.0.0.1',5005)
    
    writer.write(json.dumps(dataJson).encode())
    writer.close()