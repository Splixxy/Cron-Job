import os
import datetime
import re
dt = datetime.datetime.now()
monthAbrv = dt.strftime("%b %d")
if re.match("0*",monthAbrv):
    monthAbrv = monthAbrv.replace("0", " ")
fOpen = open("/var/log/secure","r")
if monthAbrv in fOpen:
    redFladFind = re.findall("%s*",fOpen % monthAbrv)
    redFlagFile = open("~/redflags.txt","a")
    redFlagFile.write(redFladFind)
    redFlagFile.close()
os.system("tcpdump -w icmplog.pcap -i eth0 icmp")
os.system("tcpdump -w sshlog.pcap -i eth0 port 22")
os.system("tcpdump -w httplog.pcap -i eth0 port 80")
os.system("tcpdump -w httpslog.pcap -i eth0 port 443")
