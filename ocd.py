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
    sqlQuery = """INSERT INTO FST5 VALUES (%s,%s);""" #TODO check how many parameteres we want to send
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
        thread1 = Thread(target=getobd.readData, args=())
        thread2 = Thread(target=sendToDataBase, args=())

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()


# optionally,  extra method ; to develop in future # 
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
