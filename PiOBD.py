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

def xx2():
    sqlq = """INSERT INTO FST5 VALUES (%s,%s);"""
    while (True):
        print("Debug1")
        if getobd.q.not_empty:
            x = getobd.q.get()
            dbconnection.makeQuery(sqlq,(x[0], x[1]))
        time.sleep(2)

if __name__ == "__main__":
    setConnection()

    thread1 = Thread(target=getobd.xx, args=())
    thread2 = Thread(target=xx2, args=())

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

def readFromFile():
    with open('test1.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        try:
            for row in csv_reader:
                if row is not None:
                    date = "2018-12-13"+" "+row[0]+":"+row[1]+":"+row[2]
                    thr = row[7]
                    m = re.findall(r'\d+',thr)
                    a = float(m[0]) 
                    b = float(float(m[1])/10000000000)
                    c = a + b
                    sqlq = """INSERT INTO FST4 VALUES (%s,%s);"""
                    params = (c,date)
                    dbconnection.makeQuery(sqlq,params)
        except:
            print("error")
