
string  = ' make over '


print("\n","*"*10,"STRIPPING","*"*10)
print(string)
print(string.strip()) # strip from both sides 
print(string.lstrip()) # strip from left only
print(string.rstrip()) # strip from right only 


print("\n","*"*10,"ADJUST","*"*10)

print(string.ljust(20)) # pushes string to 20 units to left
print(string.ljust(20,"*")) # pushes string to 20 units to left


print(string.rjust(20)) # pushes string to 20 units to left
print(string.rjust(20,"*")) # pushes string to 20 units to left


print(string.center(20)) # centers the string in width of 20 units 
print(string.center(20,"*")) # centers the string in width of 20 units 