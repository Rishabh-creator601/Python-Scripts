

def mul(obj:[]):
	a  = 1
	for b in obj:
		a  = a *b 

	return a





def factorial(step=1,stop=0):

	if step in [0,None]:
		a = [x for x  in range(stop+1)]
	else:
		a = [x for x  in range(step,stop+1)]

	

	return mul(a)









