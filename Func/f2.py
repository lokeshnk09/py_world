import re
l_P = input('Enter License Plate No:')
m = re.fullmatch('[0-9][A-Z]{3}\d{3}', l_P)
if m != None:
    print(l_P)
    # print("OwnerName: {0}: \nLicense_plate: {1}".format(owner, self.set_Lic_Plate))