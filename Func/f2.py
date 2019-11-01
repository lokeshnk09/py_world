import re
count = 0
pattern = re.compile('ab')
matcher = pattern.finditer('absaabaddab')
for match in matcher:
    count+=1
    print("match avialable at stat index is:", match.start())

print("no of times match found", count)