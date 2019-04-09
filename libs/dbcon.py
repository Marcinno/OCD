import psycopg2
import urllib
import time

from configparser import ConfigParser


def check_internet_connection():
    try:
        urllib.request.urlopen("https://www.google.com")
    except urllib.error.URLError:
        print("Internet connection is down")
        return False
    else:
        print("Internet is up")
        return True


def config(filename="database.ini", section="pq1"):
    parser = ConfigParser()
    parser.read(filename)

    dataBase = {}
    if parser.has_section(section):
        parameters = parser.items(section)
        for param in parameters:
            dataBase[param[0]] = param[1]
    else:
        raise Exception(
            "Section {0} not found format{1}".format(section, filename))
    return dataBase


class BaseConnection:
    def __init__(self):
        self.config = config()
        self.connection = None
        try:
            while check_internet_connection() is not True:
                print("Connection down")
                time.sleep(3)
                check_internet_connection()

            parameters = self.config
            print("Try to connect to database")
            self.connection = psycopg2.connect(**parameters)  # only under vpn
            self.cursor = self.connection.cursor()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            print("Connected")

    def make_query(self, query, parameters):
        # sql = """INSERT INTO test1 VALUES (2,3,'TEST','1997-01-01');"""
        try:
            self.cursor.execute(query, parameters)
            self.connection.commit()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            print("Query done")