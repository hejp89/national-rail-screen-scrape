############################################################
#
# Daily log the status (on time, delayed, or cancelled)
# of a particular train by scraping the National Rail site.
# 
# Written by Howard Paget (@hejp, www.howardpaget.co.uk)
#
############################################################

import datetime
import time
import sched

from set_schedule import set_schedule

def main(train_from, train_to, train_time):

  print('From: ' + train_from)
  print('To: ' + train_to)
  print('At: ' + train_time.strftime('%H:%M'))

  # screen_scrape(train_from, train_to, train_time)

  scheduler = sched.scheduler(time.time, time.sleep)

  set_schedule(scheduler, train_from, train_to, train_time)

  scheduler.run()

if __name__ == '__main__':

  # Train time and location information
  train_from = 'Merstham'
  train_to = 'Redhill'
  train_time = datetime.time(hour=22, minute=36)

  main(train_from, train_to, train_time)
  