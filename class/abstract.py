from abc import ABC, abstractmethod

import calendar
import datetime
import re

#cur_year = (calendar.TextCalendar(calendar.SUNDAY).formatyear(2019, 2, 1, 1, 2))
help(datetime)
now = datetime.datetime.now()
prev = datetime.date(2018, 12, 1)
print(now.strftime("%m-%d-%Y %I:%M"))
print(prev)

#pre_year = (calendar.TextCalendar(calendar.SUNDAY).formatyear(2018, 2, 1, 1, 2))

class Vehicle:

    def __init__(self, ct, pt):
        self.ct = ct
        self.pt = pt

    def cur_time(self):
        self.ct = datetime.datetime.now()
        return now.strftime("%m-%d-%Y %I:%M")

    def pre_time(self):
        self.pt = datetime.date(2018, 12, 31)
        return

    def __lt__(self):
        return


class Dmv(Vehicle):
    def lic_plate(self):
        self.lic_plate = lic_plate(input('Enter Lic Plate No:'))
        m = re.fullmatch('[0-9][A-Z]{3}\d{3}', lic_plate)
        if m!= None:
            print("valid number")
        else:
            print('Invalid number')

    def set_lic(self):
        pass

    def get_lic(self):
        return self.vehicle


car = Vehicle.set_lic(2019)



