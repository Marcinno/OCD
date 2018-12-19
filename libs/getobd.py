import obd
import csv

import time
import datetime
import queue

q = queue.Queue()

#cmd = obd.commands.SPEED # select an OBD command (sensor)
#response = connection.query(cmd) # send the command, and parse the response
#print(response.value) # returns unit-bearing values thanks to Pint
#print(response.value.to("mph")) # user-friendly unit conversions

# FSTILO = [1,2,4,5,6,7,11,12,13,14,15,16,18,20,21,22,29,30,32,33]

connection = None 

def connect():
    global connection
    try:
        connection = obd.OBD() # auto-connects to USB or RF port
    except(Exception) as error:
        print(error)

def xx():
    while (True):
        print("pizda")
        time.sleep(4)
        ts = datetime.datetime.now()
        x = [4,ts]
        q.put(x)


 # collecting data to csv file    
def data():
    Temp = []
    now = datetime.datetime.now()
    for i  in range(0,96):
        print(i)
        try:
            cmd = obd.commands[1][i]
            response = connection.query(cmd)
        finally:
            Temp.append(str(response.value))
    with open("test1.csv", "a") as csvfile:
        #for item in Temp:
        Temp.append(now.hour)
        Temp.append(now.minute)
        Temp.append(now.second)
        writer = csv.writer(csvfile)
        writer.writerow(Temp)
            #f.write("  Command table:%s  Value%s" %(ie,item))
            #ie += 1
        #f.write("\n")

