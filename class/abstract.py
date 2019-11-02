from abc import ABC, abstractmethod

import calendar
import datetime
import re

#cur_year = (calendar.TextCalendar(calendar.SUNDAY).formatyear(2019, 2, 1, 1, 2))
#help(datetime)
#now = datetime.datetime.now()
#prev = datetime.date(2018, 12, 31)


#pre_year = (calendar.TextCalendar(calendar.SUNDAY).formatyear(2018, 2, 1, 1, 2))

class Vehicle:

    def __init__(self, car, truck):
        self.car = car
        self.truck = truck

    def make(self):
        return input('Enter make:')

    def model(self):
        return int(input('Enter model:'))



class Dmv(Vehicle):
    def __init__(self, ct, pt, lic_plate):
        self.ct = ct
        self.pt = pt
        self.lic_plate = lic_plate(input('Enter Lic Plate No:'))
        m = re.fullmatch('[0-9][A-Z]{3}\d{3}', lic_plate)
        if m!= None:
            print("valid number")
        else:
            print('Invalid number')

    def cur_time(self):
        self.ct = datetime.datetime.now()
        return self.ct.strftime("%m-%d-%Y %I:%M")

    def pre_time(self):
        self.pt = datetime.date(2018, 12, 31)
        return self.pt

    def __lt__(self, date):
        print(self.pt - date)

    def set_lic(self):
        pass

    def get_lic(self):
        pass






