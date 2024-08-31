import matplotlib.pyplot as plt 


def plot_values(epochs,value,val_value,type_='Accuracy'):


	plt.figure()
	plt.plot(epochs,value,'bo',label=f'Training {type_}')
	plt.plot(epochs,val_value,'b',label=f'Validation {type_}')
	plt.title(f"Training and validation {type_}")
	plt.legend()
	plt.show()
