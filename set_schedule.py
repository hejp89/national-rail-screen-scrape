import datetime

from screen_scrape import screen_scrape
from util import datetime_total_seconds

# Schedule screen scrape to run once every minute from 5 minutes before departure to 5 minutes after.
def set_schedule(scheduler, train_from, train_to, train_time):
  current_time = datetime.datetime.now().time()
  today = datetime.datetime.now()
  schedule_time = None

  # If the the current time is early enough schdule the scrape for today other tomorrow
  if train_time.hour * 60 + train_time.minute - 5 > current_time.hour * 60 + current_time.minute:
    schedule_time = today.replace(hour=train_time.hour, minute=train_time.minute, second=0, microsecond=0)
  else:
    one_day = datetime.timedelta(days=1)
    schedule_time = today.replace(hour=train_time.hour, minute=train_time.minute, second=0, microsecond=0) + one_day

  for i in range(-5, 6):
    scheduler.enterabs(datetime_total_seconds(schedule_time) + i * 60, 1, screen_scrape, (train_from, train_to, train_time))

  scheduler.enterabs(datetime_total_seconds(schedule_time) + 5 * 60, 1, set_schedule, (scheduler, train_from, train_to, train_time))

  print(schedule_time)

  scheduler.run()