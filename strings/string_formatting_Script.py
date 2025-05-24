
name="rishabh"
age=32
year=1
  
string  = "hello world my name is {name} and age is {age} "

#string = string.format(name="rishabh",age=23)
string = string.format_map(vars())

print(string)

