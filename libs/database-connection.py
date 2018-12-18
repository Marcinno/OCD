import psycopg2
from configparser import ConfigParser

def config(filename = "database1.ini", section = "postgresql"):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found format{1}".format(section, filename))
        
    return db
class baseConnection:
    def __init__(self):
        self.config = config()
        self.connection = None
        try:
            params = self.config
            print("Try to connect to database")
            self.connection = psycopg2.connect(**params)
            self.cursor = self.connection.cursor()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            print("Connected")

    def makeQuery(self,query):
        # sql = """INSERT INTO test1 VALUES (2,3,'DUPA','1997-01-01');"""
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            print("Query done")
        