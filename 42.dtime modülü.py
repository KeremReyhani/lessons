#tarih ve zaman ile iletişime geçmeye yarar.
import datetime
date1=datetime.date(2003, 9, 18)
print(date1)
print(date1.year)
print(date1.month)
print(date1.day)
print()
date1=datetime.date.today()
print(date1)
print(date1.year)
print(date1.month)
print(date1.day)

print()

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

date1=datetime.date.today()
print(date1.weekday()) #0'dan başlar
print(date1.isoweekday()) #1'den başlar
print(date1.isocalendar()) #hangi yıl hangi hafta hangi gün

print()
print()
print()

time1=datetime.time(19, 29, 48, 2689)
print(time1)
print(time1.hour)
print(time1.minute)
print(time1.second)
print(time1.microsecond)

print()
print()

datetime1=datetime.datetime(1994, 11, 25, 16, 45, 58, 5634)
print(datetime1)
print(datetime1.month)
print(datetime1.minute)

print()
print()

date2=datetime.date.today()
print(date2.strftime("%Y/%m/%d"))
print(date2.strftime("%Y/%B/%d"))

print()
print()

today=datetime.date.today()
birthday=datetime.date(2003,9,18)
tdelta=today-birthday
print(type(tdelta))
print(tdelta)

print()
print()

datetime2=datetime.datetime.now()
print(datetime2)
tdelta=datetime.timedelta(hours=10) #ekler
print(datetime2+tdelta)
print(datetime2)