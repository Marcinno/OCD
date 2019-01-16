#PiOBD
from libs import dbcon
from libs import getobd
from threading import Thread

import json
import csv
import re
import queue
import time

dbconnection = None

def setConnection():
    global dbconnection
    dbconnection = dbcon.baseConnection()

def sendToDataBase():
    sqlQuery = """INSERT INTO FIATSTILO VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""" #Hard-Coded database name
    while (True):
        print("Debug1")
        if getobd.readValueQueue.not_empty:
            x = getobd.readValueQueue.get()
            dbconnection.makeQuery(sqlQuery,(x[0], x[1]))
        time.sleep(2)

if __name__ == "__main__":
    setConnection()
    getobd.connect()
    
    if getobd.connection.status is True:
        readThread = Thread(target=getobd.readData, args=())
        sendThread = Thread(target=sendToDataBase, args=())

        readThread.start()
        sendThread.start()

        readThread.join()
        sendThread.join()

def readFromFile(): # method to read from file it's just test only
    with open('test1.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        try:
            for row in csv_reader:
                if row is not None:
                    date = +row[0]+":"+row[1]+":"+row[2]
                    thr = row[7]
                    m = re.findall(r'\d+',thr)
                    a = float(m[0]) 
                    b = float(float(m[1])/10000000000)
                    c = a + b
                    sqlQuery = """INSERT INTO FST4 VALUES (%s,%s);"""
                    params = (c,date)
                    dbconnection.makeQuery(sqlq,params)
        except:
            print("error")
