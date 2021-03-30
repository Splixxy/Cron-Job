from crontab import CronTab
cron = CronTab(user=True)
detectIPjob = cron.new(command="python3 Detect-IP.py")
cron.write()
