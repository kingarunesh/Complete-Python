#SECTION :      time

# from time import time, ctime, localtime


# print(time())

# print(ctime())

# print()

# print(localtime())
# print(localtime().tm_year)
# print(localtime().tm_isdst)
# print(localtime().tm_gmtoff)
# print(localtime().tm_min)
# print(localtime().tm_zone)
# print(localtime().tm_mon)

#NOTE :         sleep

# from time import sleep

# for i in range(10):
#     if i == 5:
#         sleep(5)
#     print(i)



#SECTION :      datetime

#NOTE :         datetime
# from datetime import datetime

# print(datetime(year=2019, month=10, day=1))
# print(datetime(year=2019, month=10, day=1, hour=11, minute=11))
# print(datetime(2000, 1, 20))
# print(datetime(2000, 1, 20).year)
# print(datetime(2000, 1, 20).now())

# print()

# print(datetime.now())
# print(datetime.now().year)
# print(datetime.now().month)

# print()

# print(datetime.today())
# print(datetime.today().year)
# print(datetime.today().month)


#NOTE :         date

# from datetime import date

# print(date(year=2019, month=10, day=1))
# print(date(year=2019, month=10, day=1).year)
# print(date.today())
# print(date.today().year)
# print(date.today().month)



#NOTE :         time

# from datetime import time

# print(time())
# print(time(hour=11, minute=21, second=13, microsecond=22))
# print(time(hour=11, minute=21, second=13, microsecond=22).hour)
# print(time(hour=11, minute=21, second=13, microsecond=22).microsecond)
# print(time(hour=11, minute=21, second=13, microsecond=22).minute)


#NOTE :         timedelta

# from datetime import timedelta, date

# x = timedelta(days=10)
# y = date.today()

# print(y)

# print()

# print(x + y)
# print(y - x)


#NOTE :     compare 2 dates

# from datetime import date

# a = date(year=2020, month=12, day=12)
# # b = date(year=2020, month=12, day=12)
# b = date(year=2020, month=11, day=12)

# print(a == b, "\n")

# print(a > b, "\n")

# print(a >= b, "\n")

# print(a < b, "\n")

# print(a <= b, "\n")


#NOTE :         formatting date and time

# from datetime import datetime

# print(datetime.now())

# print(datetime.now().strftime("%B %d %Y"))


