# Jamil Hasibul
# wireless link quality measurement
# Parses the output of iwlist scan into a a variable

import sys
import subprocess
import socket
import random
import time


interface = "wlan0"
sensorTag=1
sensor_data=75
#mySocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#host_IP='172.20.10.4'
#host_port=5005  
#mySocket.connect((host_IP,host_port))
rateTime=2

def main():
    packetSerialNo=0
    while True:
        

        p1=subprocess.Popen(['iwconfig'],stdout=subprocess.PIPE)
        #Rss_SignalLevel_Current=int(float(parsed_cells[0]['Signal'][0:3]))
        
        output=p1.communicate()[0]
        #print((output))
        string_output=output.decode('utf8')
        
        #Rss_SignalLevel_Current=int(string_output[index_signal+13:index_signal+16])
       # print(type(Rss_SignalLevel_Current))
        #print(Rss_SignalLevel_Current)
        #parsed_cells=[]
	#sensorTag=random.randint(1,5)    
        sensor_data=random.randint(100,110)
        #message='%000'+str(sensorTag)+'000'+str(Rss_SignalLevel_Current)+'000'+str(sensor_data)+'000'+str(packetSerialNo)+'%'
        #mySocket.sendall(message)
        #mySocket.sendto(message, (host_IP,host_port))
        packetSerialNo=packetSerialNo+1
        #print("Message sent successfully with packet sequence no!!")
        time.sleep(rateTime)
	#except socket.error:
       #print("Failed to Send")
       #sys.exit()

       #data=mySocket.recv(1000)
       #print("The pinged message is " + data)
              
       # print (type(parsed_cells[0]['Signal']))
       # print (parsed_cells[0]['Signal'])
        #sort_cells(.0.0.1'
        
       #try:
       #print(rules)
       #print_cells(parsed_cells)
        
       #except socket.error:
       #print("Failed to Create Socket")
       #sys.exit()
main()




