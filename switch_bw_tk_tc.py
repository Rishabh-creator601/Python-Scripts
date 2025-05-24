import tkinter as tk 
from tkinter import ttk ,StringVar,IntVar
from tkinter.messagebox import showerror



class TempratureConverter:

	@staticmethod
	def f2c(f):

		result = (f -32 ) * 5/9 

		return f"{f} Fahrenheit = {result:.2f} Celcius"



	@staticmethod
	def c2f(c):

		result= c *9/5 +32 
		return f"{f} Celcius = {result:.2f} Fahrenheit"




class ConverterFrame(ttk.Frame):

	def __init__(self,container,unit_From,converter):


		super().__init__(container)


		self.unit_From = unit_From # C or F 
		self.converter = converter


		options ={"padx":5,"pady":0}



		self.temp_label =ttk.Label(self,text=self.unit_From)
		self.temp_label.grid(column=0,row=0,sticky='w',**options)



		self.temp_var = StringVar()
		self.temprature = ttk.Entry(self,textvariable=self.temp_var)
		self.temprature.grid(column=1,row=0,**options)
		self.temprature.focus()




		self.btn = ttk.Button(self,text="Convert ")
		self.btn.grid(column=2,row=0,sticky='w',**options)
		self.btn.configure(command=self.convert)


		self.result = ttk.Label(self)
		self.result.grid(row=1,columnspan=3,**options)



		self.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')








	def convert(self,event=None):


		try:
			value = float(self.temprature.get())

			result = self.converter(value)

			self.result.config(text=result)
		except ValueError as e:
			showerror(title="Error Found",message=e)



	def reset(self):

		self.temprature.delete(0,"end")
		self.result.text = ""





class ControlFrame(ttk.LabelFrame):

	def __init__(self,container):

		super().__init__(container)



		self['text'] =  'Options'

		self.selected = IntVar()


		ttk.Radiobutton(


			self,
			text="F to C",
			value=0,
			variable=self.selected,
			command=self.change_frame,
		).grid(column=0,row=0,padx=5,pady=5)




		ttk.Radiobutton(


			self,
			text="C to F",
			variable=self.selected,
			value=1,
			command=self.change_frame
		).grid(column=1,row=0,padx=5,pady=5)




		self.grid(column=0,row=1,padx=5,pady=5,sticky='ew')



		self.frames = {}

		self.frames[0] =  ConverterFrame(container,"Fahrenheit",TempratureConverter.f2c)
		self.frames[1]= ConverterFrame(container,"Celcius",TempratureConverter.c2f)

		self.change_frame()




	def change_frame(self):


		frame = self.frames[self.selected.get()]
		frame.reset()
		frame.tkraise()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Temperature Converter')
        self.geometry('300x120')
        self.resizable(False, False)





root = App()
ControlFrame(root)
root.mainloop()