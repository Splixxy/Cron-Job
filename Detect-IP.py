#import needed packages
import os
import datetime
#pulls in the datetime package
dt = datetime.datetime.now()
#sets strings for the abreviated month and day and hour in military time
monthAbrv = dt.strftime("%b%d")
monthAbrv = str(monthAbrv)
hour = dt.strftime("%H")
hour = str(hour)
#opens /var/log/secure in read mode
fOpen = open("/var/log/secure","r")
#sets fRead as the output of fOpen.read
fRead = fOpen.read()
#opens a file and then writes fRead to the file
redFlagFile = open("tcpDlogs/redflags%s%s.txt" % (monthAbrv, hour),"a")
redFlagFile.write(fRead)
redFlagFile.close()
#starts tcpdump for icmp, port 22, 80, and 443
os.system("tcpdump -w tcpDlogs/icmplog-%s-%s.pcap -i any -c10 icmp" % (monthAbrv, hour))
os.system("tcpdump -w tcpDlogs/sshlog-%s-%s.pcap -i any -c10 port 22" % (monthAbrv, hour))
os.system("tcpdump -w tcpDlogs/httplog-%s-%s.pcap -i any -c10 port 80" % (monthAbrv, hour))
os.system("tcpdump -w tcpDlogs/httpslog-%s-%s.pcap -i any -c10 port 443" % (monthAbrv, hour))
