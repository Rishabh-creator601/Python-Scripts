from functools import partial




'''
partial kind of fixes a parameter and helps us to not keep things repeatdly

'''


# just a sample fnc 
def execute(name='xyz',age=45):
    print(f"MY NAME IS {name}  AND AGE IS {age} ")
    
    
new_func =  partial(execute,name='baap') 


new_func(age=67)
new_func(age=89)