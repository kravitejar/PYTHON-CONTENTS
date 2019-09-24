import time;

localtime = time.localtime(time.time())
print( "Local current time :", localtime)



import time;

localtime = time.asctime( time.localtime(time.time()) )
print( "Local current time :", localtime)



import calendar

cal = calendar.month(2019, 9)
print(cal)


from datetime import date

today = date.today()

print("Current date =", today)


from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)




from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2019, month = 8, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2021, month = 8, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)
