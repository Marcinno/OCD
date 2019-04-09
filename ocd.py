import json
import csv
import re
import queue
import time

from libs import dbcon
from libs import getobd
from threading import Thread

dbconnection = None


def set_connection():
    global dbconnection
    dbconnection = dbcon.BaseConnection()


def send_to_data_base():
    sql_query = """INSERT INTO FIATSTILO VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""  # Hard-Coded database name
    while (True):
        print("Debug1")
        if getobd.read_value_queue.not_empty:
            x = getobd.read_value_queue.get()
            dbconnection.make_query(sql_query, (x[0], x[1]))
        time.sleep(2)

if __name__ == "__main__":
    set_connection()
    getobd.connect()
    if getobd.connection.status is True:
        readThread = Thread(target=getobd.read_data, args=())
        sendThread = Thread(target=send_to_data_base, args=())

        readThread.start()
        sendThread.start()

        readThread.join()
        sendThread.join()


def read_from_file():  # method to read from file it's just test only
    with open('test1.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        try:
            for row in csv_reader:
                if row is not None:
                    date = +row[0]+":"+row[1]+":"+row[2]
                    thr = row[7]
                    m = re.findall(r'\d+', thr)
                    a = float(m[0])
                    b = float(float(m[1])/10000000000)
                    c = a + b
                    sql_query = """INSERT INTO FST4 VALUES (%s,%s);"""
                    params = (c, date)
                    # dbconnection.make_query(sqlq,params)
        except:
            print("error")
