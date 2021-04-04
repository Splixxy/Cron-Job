#import the os package
import os
#installs gzip
os.system("%s install gzip" % distro)
#tars the / directory
os.system("tar -zcvf Full-Backup.tar.gz /*")
#prints out that it has been backupped
print("/ has been backupped.")
