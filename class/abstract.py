from abc import ABC, abstractmethod

import calendar
import datetime
import re

#cur_year = (calendar.TextCalendar(calendar.SUNDAY).formatyear(2019, 2, 1, 1, 2))
#help(datetime)
#now = datetime.datetime.now()
#prev = datetime.date(2018, 12, 31)
#pre_year = (calendar.TextCalendar(calendar.SUNDAY).formatyear(2018, 2, 1, 1, 2))


class Dmv:

    def __init__(self):
        self.lic_plate = None
        self.vehicle = self.Vehicle()

    def set_lic_plate(self):
        self.lic_plate = input('Enter License Plate No:')
        l_P = re.fullmatch('[0-9][A-Z]{3}\d{3}', self.lic_plate)
        if l_P != None:
            return self.lic_plate
        else:
            print('Invalid No!')
            # print("OwnerName: {0}: \nLicense_plate: {1}".format(owner, self.set_Lic_Plate))

    def get_lic_plate(self):
        return self.lic_plate

    class Vehicle:
        def __init__(self):
            pass

        def owner(self):
            return input('Enter Vehicle owner Name: ')

        def make(self):
            return input('Enter make:')

        def model(self):
            return int(input('Enter model:'))


car = Dmv()
car.set_lic_plate()
print(car.get_lic_plate())










