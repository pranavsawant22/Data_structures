xr = [i for i in range(9) if i % 2 != 0]
print(xr)

a, b, *c = "pranav"
print(a, b, c)
from random import *

z = [i for i in range(randint(1, 100))]


D = {'a': 1, 'b': 2, 'c': 3}
D
# Output: {'a':1, 'c':3, 'b':2}
# If we need to impose an ordering on dictionary's items, one common
# solution is to grab a list of keys, sort that list and then step through
# the dictionary using for loop.
k = list(D.keys())
# ['a', 'b', 'c']
k.sort()
for key in k:
    print(key, '=', D[key])
print()
for key in sorted(D):
    print(key, '=', D[key])
# In above example, we saw - how to make a list of 'keys' in a dictionary:
k = list(D.keys())  #

v = list(D.values())
p = list(D.items())
print(k, v)
country_to_capital = {
    'UK': 'London',
    'Brazil': 'Brazilia',
    'Morocco': 'Rabat',
    'Sweden': 'Stockholm'
}
capital_to_country = {
    capital: country for country, capital in country_to_capital.items()
}

rec = {
    'name': {'first': 'Bob', 'last': 'Smith'},
    'job': ['dev', 'mgr'],
    'age': 40.5
}

g = {
    op:pr for op,pr in rec.items()
}
print(g)

print()
T = (1,2,4,5,6,21)
h = (123,)
print(type(h))
p = 1,2,3,4,5,6
print((p))

def minmax(items):
    return min(items),max(items)
print(minmax([1,2,3,4,6,5,8,9]))

#Sets
x = set('spammer')
print(x)

x.add('z')
x.add((4,5))
print(x)
a=4
b=a
print(b)
a=6
print(b)

L1 = [2, 3, 4]
L2 = L1
L1[0] = 1
print(L1,L2)

x = 10
while x:
    x -=1
    if x % 2 != 0: continue
    print(x, end=' ')
v=0
if v==1:
    def func(a,b):
        print(a+b)
else:
    def func(a,b):
        print(a-b)

func(3,4)

arr= [None]*5
print(arr)