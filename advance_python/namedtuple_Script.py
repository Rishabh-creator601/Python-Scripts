from collections import namedtuple


'''
tuple with name 
it is fascination just or presentation will be good 
also it is back of traditional tuple
'''

user = namedtuple("USER",['names','age'])


u1 = user(['rashesh','rashesh'],18)
u2 = user('snek',23)

print(u1)
print(u1.name)
print(u1.name.count('rashesh'))