from collections import ChainMap

a = {"a":1,"b":2}
b = {'name':32,'age':45}

c =  ChainMap(a,b)


# print(c['a'],c['name'])
# print()
# print("Just keys : ",list(c.keys()))
# print("Just values : ",list(c.values()))

# print("All values combined" ,c.maps)


### IMP ONE 

'''
new_child()

same key but multiple values but show last value if you log it 


parents()

discard the last one of the same key


'''


arr =  ChainMap() # empty chainmap

#new child 

arr['x'] =  1

print(arr['x'])


arr = arr.new_child()  # sample element but different value  || adding new type
arr['x'] = 2

arr =  arr.new_child()

arr['x'] =  3
print(arr.maps)


# parents 

arr =  arr.parents # discard last one  || pop type

print(arr.maps)