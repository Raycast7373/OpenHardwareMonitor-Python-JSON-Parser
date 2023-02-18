import json 
import requests 
import time

HostIP = '127.0.0.1'
HostPort = '8123'
loop = True

def PrintData(sensorid1, sensorid2):
    count = 0
    for i in OHW_DICT['Children'][0]['Children'][sensorid1]['Children'][sensorid2]['Children']:
        data = OHW_DICT['Children'][0]['Children'][sensorid1]['Children'][sensorid2]['Children'][count]
        data_min = data['Min']
        data_max = data['Max']
        data_current = data['Value']
        data_name = data['Text']
        print(data_name, ":", "min:", data_min, "max:", data_max, "current:", data_current)
        count+=1

def PrintAllInfo():
    counta=0
    countb=0
    countc=0
    print("")
    print(OHW_DICT['Children'][0]['Text'])
    for i in OHW_DICT['Children'][0]['Children']:
        print("")
        print(OHW_DICT['Children'][0]['Children'][counta]['Text'])
        for o in OHW_DICT['Children'][0]['Children'][counta]['Children']:
            print("")
            print(OHW_DICT['Children'][0]['Children'][counta]['Children'][countb]['Text'])
            for p in OHW_DICT['Children'][0]['Children'][counta]['Children'][countb]['Children']:
                data = OHW_DICT['Children'][0]['Children'][counta]['Children'][countb]['Children'][countc]
                data_min = data['Min']
                data_max = data['Max']
                data_current = data['Value']
                data_name = data['Text']
                print(data_name, ":", "min:", data_min, "max:", data_max, "current:", data_current)
                countc+=1
            countc=0
            countb+=1
        countb=0
        counta+=1
        print("")
    counta=0

print("Currently connected to: http://"+HostIP+":"+HostPort)

while loop == True:
    OHW_ADDRESS = "http://"+HostIP+":"+HostPort+"/data.json"
    OHW_DICT = json.loads(requests.get(OHW_ADDRESS).text)
    PrintAllInfo() # prints all data from openhardwaremonitor
    time.sleep(1)

if loop == False:
    OHW_ADDRESS = "http://"+HostIP+":"+HostPort+"/data.json"
    OHW_DICT = json.loads(requests.get(OHW_ADDRESS).text)
    PrintAllInfo() # prints all data from openhardwaremonitor

#CPU
#BLCK
#PrintData(1, 0)
#CPU Temperature
#PrintData(1, 1)
#CPU Usage
#PrintData(1, 2)
#CPU Power Usage
#PrintData(1, 3)

#RAM
#RAM Usage
#PrintData(2, 0)
#RAM Usage Info
#PrintData(2, 1)
#RAM Other Values
#PrintData(2, 2)

#GPU

