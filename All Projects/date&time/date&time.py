




import datetime
import pytz


time_now = datetime.datetime.now()
eu_amsterdam = pytz.timezone('US/Alaska')
time_now = eu_amsterdam.localize(time_now)

print(time_now)




for a in pytz.all_timezones:
    print(a)  