import obd
import csv
import sys

import time
import datetime
import queue


readValueQueue = queue.Queue()
valueList = None
connection = None 
timer = 0 
#cmd = obd.commands.SPEED # select an OBD command (sensor)
#response = connection.query(cmd) # send the command, and parse the response
#print(response.value) # returns unit-bearing values thanks to Pint
#print(response.value.to("mph")) # user-friendly unit conversions

FSTILO = [1,2,4,5,6,7,11,12,13,14,15,16,18,20,21,22,29,30,32,33] # Hard-Coded values for defined car


def connect():
    global timer 
    global connection

    try:
        ports = obd.scan_serial() # return list of valid ports
    except(Exception) as error:
        print(error)
      
    try:
        connection = obd.OBD(ports[0], baudrate=38400, protocol=None, fast=True) # auto-connects to USB or RF port
    except(Exception) as error:
        print(error)
        #
            #BUZZER
        #
        if timer > 20 :
            sys.exit("Too many attempts")
        timer += 1
        connect()
    finally:
        readData()

def readData():
    while (True):
        valueList = None
        valueList.append(datetime.datetime.now())
        for i in FSTILO:
            command = obd.commands[1][i] # 1 is a default 
            response = connection.query(command,True)
            valueList.append(response.value.magnitude)
        readValueQueue.put(valueList)

# optionally,  extra method ; to develop in future # 
def data():  # collecting data to csv file    
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
