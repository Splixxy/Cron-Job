#imports the os package and inotify
import os
from inotify_simple import INotify, flags
#pulls in the package
inotify = INotify()
#runs the below command so this script will keep running once it's finished
os.system("while :; do python3 File-Changes.py; done")
#creates the watch flags
watch_flags = flags.CREATE | flags.DELETE | flags.MODIFY | flags.DELETE_SELF
#creates watches for the below directory
wdVarLog = inotify.add_watch("/var/log", watch_flags)
wdETC = inotify.add_watch("/etc", watch_flags)

#for event in inotify prints to directorylogs
for event in inotify.read():
    fOpen = open("directorylogs.txt","a")
    fOpen.write(event)
    fOpen.close()
    #for flag in event prints out to the same file as the events
    for flag in flags.from_mask(event.mask):
        fstring = (" " + str(flag))
        fOpen = open("directorylogs.txt","a")
        fOpen.write(fstring)
        fOpen.close()
