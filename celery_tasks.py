from celery import Celery
from celery.schedules import crontab
from telegram.ext import Updater

from kursi import inform_subscribers, TOKEN, updater
from utils.models import DB_FILENAME, initialize_db


app = Celery(
    'lariskursibot',
    broker=f'sqla+{DB_FILENAME}',
    timezone='Asia/Tbilisi'   
)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes everyday at 17:05 Tbilisi time (UTC+4)
    sender.add_periodic_task(
        crontab(hour=17, minute=5),
        daily_informer.s(),
    )


@app.task
def daily_informer():
    db_session = initialize_db()
    inform_subscribers(db_session)
    db_session.close()