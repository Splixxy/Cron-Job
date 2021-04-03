#cron job to run on startup
import os
from inotify_simple import INotify, flags
inotify = INotify()
watch_flags = flags.CREATE | flags.DELETE | flags.MODIFY | flags.DELETE_SELF
wdVarLog = inotify.add_watch("/var/log", watch_flags)
wdETC = inotify.add_watch("/etc", watch_flags)

for event in inotify.read():
    fOpen = open("~/directorylogs.txt","a")
    fOpen.write(event)
    fOpen.close()
    for flag in flags.from_mask(event.mask):
        fstring = (" " + str(flag))
        fOpen = open("~/directorylogs.txt","a")
        fOpen.write(fstring)
        fOpen.close()
