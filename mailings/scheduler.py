from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler.triggers.cron import CronTrigger


def job():
    pass


@register_job
def configure_scheduler():
    scheduler = BackgroundScheduler()

    pass

