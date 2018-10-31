
# Jamil Hasibul
# wireless link quality measurement
# Parses the output of iwlist scan into a a variable

import sys
import subprocess
import socket
import random
import time
import datetime

script='cat /sys/class/net/wlan0/statistics/tx_compressed'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_compressed_start=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_fifo_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_fifo_errors_start=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_window_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_window_errors_start=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_heartbeat_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_heartbeat_errors_start=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_aborted_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_aborted_errors_start=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_carrier_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_carrier_errors_start=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_errors_start=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_bytes'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_bytes_start=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_dropped'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_dropped_start=int(output.decode('utf8'))



tx_packets_stop=0
tx_packets_start=0



script='cat /sys/class/net/wlan0/statistics/tx_packets'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_packets_start=int(output.decode('utf8'))

sensorTag=2
sensor_data=75
mySocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host_IP='10.88.105.222'
host_port=5005  
#mySocket.connect((host_IP,host_port))
rateTime=1/120
sendingTime=0
def job():
    packetSerialNo=1
    messageCount=20



    
    
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
    
job()
print(datetime.datetime.time(datetime.datetime.now()))

script='cat /sys/class/net/wlan0/statistics/tx_packets'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_packets_stop=int(output.decode('utf8'))
       

script='cat /sys/class/net/wlan0/statistics/tx_compressed'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_compressed_stop=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_fifo_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_fifo_errors_stop=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_window_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_window_errors_stop=int(output.decode('utf8'))
            
script='cat /sys/class/net/wlan0/statistics/tx_heartbeat_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_heartbeat_errors_stop=int(output.decode('utf8'))
            
script='cat /sys/class/net/wlan0/statistics/tx_aborted_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_aborted_errors_stop=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_carrier_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_carrier_errors_stop=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_errors'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_errors_stop=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_bytes'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_bytes_stop=int(output.decode('utf8'))

script='cat /sys/class/net/wlan0/statistics/tx_dropped'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
tx_dropped_stop=int(output.decode('utf8'))


mySocket.sendto("bye", (host_IP,host_port))

print("tx_packets= " + str(tx_packets_stop-tx_packets_start)+ " Start= " + str(tx_packets_start)+" Stop= "+str(tx_packets_stop))


print("tx_dropped= " + str(tx_dropped_stop-tx_dropped_start)+" Start= " + str(tx_dropped_start)+" Stop= "+str(tx_dropped_stop))
print("tx_bytes= "    + str(tx_bytes_stop-tx_bytes_start)+" Start= " + str(tx_bytes_start)+" Stop= "+str(tx_bytes_stop))
print("tx_errors= "    + str(tx_errors_stop-tx_errors_start)+" Start= " + str(tx_errors_start)+" Stop= "+str(tx_errors_stop))
print("tx_carrier_errors= "    + str(tx_carrier_errors_stop-tx_carrier_errors_start)+" Start= " + str(tx_carrier_errors_start)+" Stop= "+str(tx_carrier_errors_stop))
print("tx_aborted_errors= "    + str(tx_aborted_errors_stop-tx_aborted_errors_start)+" Start= " + str(tx_aborted_errors_start)+" Stop= "+str(tx_aborted_errors_stop))
print("tx_heartbeat_errors= "    + str(tx_heartbeat_errors_stop-tx_heartbeat_errors_start)+" Start= " + str(tx_heartbeat_errors_start)+" Stop= "+str(tx_heartbeat_errors_stop))
print("tx_window_errors= "    + str(tx_window_errors_stop-tx_window_errors_start)+" Start= " + str(tx_window_errors_start)+" Stop= "+str(tx_window_errors_stop))
print("tx_fifo_errors= "    + str(tx_fifo_errors_stop-tx_fifo_errors_start)+" Start= " + str(tx_fifo_errors_start)+" Stop= "+str(tx_fifo_errors_stop))
print("tx_compressed= "    + str(tx_compressed_stop-tx_compressed_start)+" Start= " + str(tx_compressed_start)+" Stop= "+str(tx_compressed_stop))







