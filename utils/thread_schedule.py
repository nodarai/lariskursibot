#! /usr/bin/env python
# coding: utf-8
import schedule
import time
from threading import Thread


class ThreadSchedule(Thread):
    def __init__(self, fn):
        super(ThreadSchedule, self).__init__()
        self.fn = fn

    def run(self):
        """
        Run the thread which will schedule a task (self.fn) that will be
        executed every day at 13:02 UTC/GMT this time is chosen because it
        corresponds to 17:01 Georgian Time in winter (17:00 is the time when
        National Bank of Georgia publishes its currency exchange rates).
        As the Georgian Time does not have winter/summer time in summer this
        time will be different.
        """
        schedule.every().day.at("13:02").do(self.fn)
        while True:
            schedule.run_pending()
            time.sleep(1)
