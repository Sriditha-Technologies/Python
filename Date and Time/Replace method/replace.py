import datetime
dt=datetime.time(22,30,19)
print("Before replacement the time is:",dt)
dt1=dt.replace(hour=11,minute=15,second=20)
print("After replacement the time is:",dt1)