import calendar

print(calendar.weekheader(3))
print(calendar.firstweekday())
print(calendar.month(2021,3))
print(calendar.monthcalendar(2021,3))
print(calendar.calendar(2021))

day_of_the_week=calendar.weekday(2021,3,18)
print(day_of_the_week)
# 0=mon, 1=tues, 2=wed, 3=thurs...

is_leap=calendar.isleap(2019)
print(is_leap)
is_leap=calendar.isleap(2020)
print(is_leap)

how_many_leap_day=calendar.leapdays(2021,2050)
