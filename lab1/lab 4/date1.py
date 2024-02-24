
from datetime import date,timedelta
#1
today = date.today()
not_today = today-timedelta(days=5)
print(not_today)

#2
today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=-1)
print(yesterday,today,tomorrow)

#3
from datetime import datetime
mow = datetime.now()
mow = mow.replace(microsecond=0)
print(mow)

#4
from datetime import datetime,timedelta
cur_date = datetime.now()

new_date = cur_date-timedelta(days=1)

print(cur_date,new_date,sep="\n")