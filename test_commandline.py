
import subprocess

script='cat /sys/class/net/wlan0/statistics/rx_packets'
p1=subprocess.Popen([script],stdout=subprocess.PIPE,shell=True)
output=p1.communicate()[0]
string_output=output.decode('utf8')
print(string_output)
print(len(string_output))
