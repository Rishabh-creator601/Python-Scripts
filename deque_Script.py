from collections import deque 

'''

promotes adding and removing elements from both ends 

| a | b | c |

default is right one 

functions :

append()
appendleft()
extend()
extendleft()


pop()
popleft()
clear()
remove()



reverse()
index()
count()


'''

array  =  deque([1,2,3,4])  


### ADDING  ITEMS 

print( "NORMAL ARRAY : ",  array)

array.append(8)  # appends to right 
array.appendleft(8)


print("ADDING ITEMS : " , array)



###   DELETING ITEMS 

array.pop()  # removes item from right 
array.popleft() 

print("REMOVING ITEMS" , array)

## OTHER FUNCTIONS 

print("\nOTHER FIUNCTIONS : ")

for (index,i) in enumerate(['reverse()','clear()','index()','remove()','count()','extend()','extendleft()']):
    
    print(f"{index+1}) {i}")