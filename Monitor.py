#import required modules
import os
import datetime
from inotify_simple import INotify, flags
import re
#runs this command to make this script keep running after it has been started
os.system("while :; do python3 Monitor.py; done")
#pulls in the datetime package
dt = datetime.datetime.now()
#gets strings of the monday and day without a space and month and day with a space.
monthDay = (dt.strftime("%b%d"))
monthDay = str(monthDay)
monthAbrv = (dt.strftime("%b %d"))
monthAbrv = str(monthAbrv)
#removes the 0 from monthAbrv
if re.match("0*",monthAbrv):
    monthAbrv = monthAbrv.replace("0", " ")
#sets inotify
inotify = INotify()
#creates the watch flags
watch_flags = flags.CREATE | flags.DELETE | flags.MODIFY | flags.DELETE_SELF
#creates the watches with watch_flags
wdDot = inotify.add_watch("/.", watch_flags)
wdBashHisotry = inotify.add_watch(".bash_history", watch_flags)
wdBashLogout = inotify.add_watch(".bash_logout", watch_flags)
wdBashProfile = inotify.add_watch(".bash_profile", watch_flags)
wdBashRC = inotify.add_watch(".bashrc", watch_flags)
wdCache = inotify.add_watch(".cache", watch_flags)
wdConfig = inotify.add_watch(".config", watch_flags)
wdESDauth = inotify.add_watch(".esd_auth", watch_flags)
wdGem = inotify.add_watch(".gem", watch_flags)
wdICEauth = inotify.add_watch(".ICEauthority", watch_flags)
wdLocal = inotify.add_watch(".local", watch_flags)
wdMozilla = inotify.add_watch(".mozilla", watch_flags)
wdPki = inotify.add_watch(".pki", watch_flags)
wdViminfo = inotify.add_watch(".viminfo", watch_flags)
wdWget = inotify.add_watch(".wget-hsts", watch_flags)
#creates functions for each watch to log to
def WD0():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if re.search("wd=1,",fRead):
        print(fRead)
        os.system("stat /. > logs/wdDotstat.txt")
        os.system("last > logs/wdDotlastlog.txt")

def WD1():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=1" in fRead:
        os.system("stat .bash_history > logs/wdBashHisotrystat.txt")
        os.system("last > logs/wdBashHisotrylast.txt")

def WD2():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=2" in fRead:
        os.system("stat .bash_logout > logs/wdBashLogoutstat.txt")
        os.system("last > logs/wdBashLogoutlast.txt")

def WD3():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=3" in fRead:
        os.system("stat .bash_profile > logs/wdBashProfilestat.txt")
        os.system("last > logs/wdBashProfilelast.txt")

def WD4():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=4" in fRead:
        os.system("stat .bashrc > logs/wdBashRCstat.txt")
        os.system("last > logs/wdBashRClast.txt")

def WD5():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=5" in fRead:
        os.system("stat .cache > logs/wdCachestat.txt")
        os.system("last > logs/wdCachelast.txt")

def WD6():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=6" in fRead:
        os.system("stat .config > logs/wdConfigstat.txt")
        os.system("last > logs/wdConfiglast.txt")

def WD7():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=7" in fRead:
        os.system("stat .esd_auth > logs/wdESDauthstat.txt")
        os.system("last > logs/wdESDauthlast.txt")

def WD8():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=8" in fRead:
        os.system("stat .gem > logs/wdGemstat.txt")
        os.system("last > logs/wdGemlast.txt")

def WD9():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=9" in fRead:
        os.system("stat .ICEauthority > logs/wdICEauthstat.txt")
        os.system("last > logs/wdICEauthlast.txt")

def WD10():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=10" in fRead:
        os.system("stat .local > logs/wdLocalstat.txt")
        os.system("last > logs/wdLocallast.txt")

def WD11():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=11" in fRead:
        os.system("stat .mozilla > logs/wdMozillastat.txt")
        os.system("last > logs/wdMozillalast.txt")

def WD12():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=12" in fRead:
        os.system("stat .pki > logs/wdPkistat.txt")
        os.system("last > logs/wdPkilast.txt")

def WD13():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=13" in fRead:
        os.system("stat .viminfo > logs/wdViminfostat.txt")
        os.system("last > logs/wdViminfolast.txt")

def WD14():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"r")
    fRead = fOpen.read()
    if "wd=14" in fRead:
        os.system("stat .wget-hsts > logs/wdWgetstat.txt")
        os.system("last > logs/wdWgetlast.txt")
#for events in inotify writes the event and then runs each functions to test for the watch event
for event in inotify.read():
    file = ("logs/Monitorlogs-%s.txt" % monthDay)
    fOpen = open(file,"a")
    fOpen.write(str(event))
    fOpen.close()
    WD0()
    WD1()
    WD2()
    WD3()
    WD4()
    WD5()
    WD6()
    WD7()
    WD8()
    WD9()
    WD10()
    WD11()
    WD12()
    WD13()
    WD14()
    #for the flags in event prints them into the same file with the events
    for flag in flags.from_mask(event.mask):
        fstring = str(("\n " + str(flag)))
        fOpen = open(file,"a")
        fOpen.write(fstring)
        fOpen.close()
