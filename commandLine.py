import subprocess

#host =raw_input("Enter a host to ping: ")




p1=subprocess.Popen(['iwlist','wlan0','scan'],stdout=subprocess.PIPE)
#p1=subprocess.Popen(['iwconfig','wlan0','|','grep','Signal'],stdout=subprocess.PIPE)


output=p1.communicate()[0]
print(type(output))

string_output=output.decode('utf8')
index_signal=string_output.find("Signal level")
signal_strength=int(string_output[index_signal+13:index_signal+16])
print(signal_strength)
