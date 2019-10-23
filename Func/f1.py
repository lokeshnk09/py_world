# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.



def up_low(s):

    d = {"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d['upper']+=1
        elif c.islower():
            d['lower']+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])


v = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(v)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

u = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print(u)

