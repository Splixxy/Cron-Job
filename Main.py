#imports contab package
from crontab import CronTab
#creates the cron job of Detect-IP.py script to run every hour
cron = CronTab(user="root")
detectIPjob = cron.new(command="python3 Detect-IP.py")
detectIPjob.hour.every(1)
cron.write()
#creates the cron job of Backup.py to run every Friday
cron = CronTab(user="root")
Backupjob = cron.new(command="python3 Backup.py")
Backupjob.day.on(5)
cron.write()
