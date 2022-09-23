import sys
import datetime

started = False
type_cnt = 0
type_times = []
speed = 0
for line in sys.stdin:
    if started:
        type_cnt += 1
        now = datetime.datetime.now()
        type_times.append(now)
        speed10 = 0
        if type_cnt > 11:
            speed10 = 60 / (type_times[type_cnt-1] - type_times[type_cnt-11]).total_seconds() * 10
        if type_cnt > 2:
            speed = speed * .8 + 60 / (type_times[type_cnt-1] - type_times[type_cnt-2]).total_seconds() * .2
        print(now.isoformat(), line.strip(), "{:.2f}".format(speed), "{:.2f}".format(speed10))
    else:
        started = line.startswith("Logging")
