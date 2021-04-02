from crontab import CronTab
cron = CronTab(user="username")
detectIPjob = cron.new(command="python3 Detect-IP.py")
detectIPjob.hour.on(24,1,2,3,4,5,6)
cron.write()
