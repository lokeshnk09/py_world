import calendar
m = 1
cal = calendar.Calendar()
while m <= 12:
    for x in cal.itermonthdates(2019, m):
        print(x)
    m += 1


