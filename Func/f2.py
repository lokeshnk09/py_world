
import re

string = 'John has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fishes'


st = re.findall('([A-Za-z]+) \w+ (\d+) (\w+)', string)
print(st)

t = list(zip(*st))
print(t)

m = re.search('([A-Za-z]+) \w+ (\d+) (\w+)', string)
print(m.group())





