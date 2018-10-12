import subprocess

#host =raw_input("Enter a host to ping: ")

p1=subprocess.Popen(['iwlist','wlan0','scan'],stdout=subprocess.PIPE)

output=p1.communicate()[0]
print(type(output))
print (output)
