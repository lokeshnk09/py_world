import calendar


def fetch_dates():
    n = int(input("Enter the Year: "))
    m = 1
    dates = []
    cal = calendar.Calendar()
    while m <= 12:
        for x in cal.itermonthdates(n, m):
            dates.append(x)
        m += 1
    return dates


def print_dates(items):
    for item in items:
        print(item)


if __name__ == '__main__':
    d = fetch_dates()
    print_dates(d)






