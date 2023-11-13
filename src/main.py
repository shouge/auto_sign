from apscheduler import Scheduler
from apscheduler.triggers.cron import CronTrigger

from task.sign_task import SignTask

if __name__ == '__main__':
    scheduler = Scheduler()
    task: SignTask = SignTask()
    scheduler.add_schedule(task.__call__,
                           CronTrigger.from_crontab(expr="*/1 9 * * *", timezone="Asia/Shanghai"), id="signIn")

    scheduler.add_schedule(task.__call__,
                           CronTrigger.from_crontab(expr="*/1 21 * * *", timezone="Asia/Shanghai"), id="signOut")
    scheduler.start_in_background()
