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

    def __init__(self):
        self.owner = input('Enter Vehicle Owner Name: ')
        self.make = input('Enter make:')
        self.model = int(input('Enter model:'))
        self.dmv = self.Dmv()

    def show_vehicle(self):
        print(self.owner, self.make, self.model)

    class Dmv:
        def set_lic_plate(self, value=input('Enter License Plate No:')):
            m = re.fullmatch('[0-9][A-Z]{3}\d{3}', value)
            if m != None:
                return m

        def get_lic_plate(self):
            print(self.set_lic_plate)


if __name__ == '__main__':
    v = Vehicle()
    v.show_vehicle()
    v.dmv.set_lic_plate
    v.dmv.get_lic_plate()










