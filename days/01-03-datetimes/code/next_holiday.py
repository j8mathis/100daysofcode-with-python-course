from datetime import date
from datetime import datetime
import holidays

todaydate = date.today()
today = datetime.today()

us_holidays = holidays.US(years=today.year)

top3 = []

for date, name in sorted(us_holidays.items()):
    if date >= todaydate:
        top3.append(date)

print("The next three major holidays coming up are:")
for i in top3[:3]:
    dt = datetime.combine(i, datetime.min.time())
    print(i, us_holidays[i], " in ", (dt - today))