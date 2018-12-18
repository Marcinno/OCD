import obd
import csv
connection = obd.OBD() # auto-connects to USB or RF port
import datetime

#cmd = obd.commands.SPEED # select an OBD command (sensor)

#response = connection.query(cmd) # send the command, and parse the response

#print(response.value) # returns unit-bearing values thanks to Pint
#print(response.value.to("mph")) # user-friendly unit conversions

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

while(True):
    data()
