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

    def __init__(self, make, model, owner):
        self.make = make
        self.model = model
        self.owner = owner

    def owner_name(self):
        self.owner = input('Enter Vehicle owner Name: ')
        return

    def make(self):
        return self.make(input('Enter make:'))

    def model(self):
        return self.model(int(input('Enter model:')))

    def set_Lic_Plate(self, owner):
        print('OwnerName:', owner)
        l_p = input('Enter License Plate no:')
        m = re.fullmatch('[0-9][A-Z]{3}\d{3}', l_p)
        if m != None:
            return {owner: l_p}


if __name__ == '__main__':
    v = Vehicle('Lokesh', 2017, 'Mazda')
    v.set_Lic_Plate('Lokesh')

