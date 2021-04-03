import os
os.system("%s install gzip" % distro)
os.system("tar -zcvf Full-Backup.tar.gz /*")
print("/ has been backupped.")
