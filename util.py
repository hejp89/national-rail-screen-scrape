import datetime

def datetime_total_seconds(dt):
  epoch = datetime.datetime(1970, 1, 1)
  return (dt - epoch).total_seconds()