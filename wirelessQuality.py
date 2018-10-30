
# Jamil Hasibul
# wireless link quality measurement
# Parses the output of iwlist scan into a a variable

import sys
import subprocess
import socket
import random
import time
import datetime


sensorTag=2
sensor_data=75
mySocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host_IP='10.88.105.222'
host_port=5005  
#mySocket.connect((host_IP,host_port))
rateTime=0.05
sendingTime=0
def main():
    packetSerialNo=1
    messageCount=2000
    print(datetime.datetime.time(datetime.datetime.now()))
    while messageCount>0:
        

        p1=subprocess.Popen(['iwconfig'],stdout=subprocess.PIPE)
        
        
        output=p1.communicate()[0]
        

        string_output=output.decode('utf8')
        index_signal=string_output.find("Signal level")
        Rss_SignalLevel_Current=int(string_output[index_signal+13:index_signal+16])
       
        print(Rss_SignalLevel_Current)
          
        sensor_data=random.randint(100,110)
        message='%###'+str(sensorTag)+'###'+str(Rss_SignalLevel_Current)+'###'+str(sensor_data)+'###'+str(packetSerialNo)+'###'+str(datetime.datetime.time(datetime.datetime.now()))+'%'
        
        mySocket.sendto(message, (host_IP,host_port))
        packetSerialNo=packetSerialNo+1
        print("Message sent successfully with packet sequence no!!")
        messageCount-=1
	time.sleep(rateTime)
	
       
main()
print(datetime.datetime.time(datetime.datetime.now()))
mySocket.sendto("bye", (host_IP,host_port))



