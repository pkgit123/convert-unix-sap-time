import time
import datetime

# https://stackoverflow.com/questions/19801727/convert-datetime-to-unix-timestamp-and-convert-it-back-in-python
start_d = datetime.date(2021,8,8)
start_unixtime = time.mktime(start_d.timetuple())
print(start_d)
print(start_d.timetuple())
print(start_unixtime)
