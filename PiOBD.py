#PiOBD
from libs import tcp_connection #async connection modules contains send funcs
import threading
import asyncio
import time

dataJson = {
    'A' : 1,
    'B' : 2,
}
if __name__ == "__main__":
    while True:
        asyncio.run(tcp_connection.sendData(dataJson))
        time.sleep(1) #testing loop

    print("Elo")    
