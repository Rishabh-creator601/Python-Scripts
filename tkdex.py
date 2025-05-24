import tkinter as tk 
from tkinter import ttk 
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure 
from matplotlib.animation import FuncAnimation
from matplotlib import style
import matplotlib.pyplot as plt
import urllib,json
import pandas as pd
import numpy as np


matplotlib.use("TkAgg")
style.use("ggplot")


LARGE_FONT= ("Verdana", 12)




f = Figure(figsize=(5,4),dpi=100)

a = f.add_subplot(111)

def animate(i):
	data =  open("sample.txt").read().split("\n")

	xvar = []
	yvars  = []

	for d in data:

		if len(d)>1:
			x,y = d.split(",")
			xvar.append(int(x))
			yvars.append(int(y))
	a.clear()
	a.plot(xvar,yvars)






class StartPage(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)



		label =ttk.Label(self,text="""ALPHA Bitcoin trading application
        use at your own risk. There is no promise
        of warranty.""",font=LARGE_FONT).pack(padx=10,pady=10)


		b1 = ttk.Button(self,text="Agree",command=lambda :controller.show_frame(1))
		b2 = ttk.Button(self,text='Disagree',command=quit)
		



		b1.pack()
		b2.pack()









class PageOne(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)



		label =ttk.Label(self,text="This is  Page 1").pack()


		b1 = ttk.Button(self,text="< Back To Home",command=lambda :controller.show_frame(0))



		b1.pack()


		






class BTC_PAGE(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)



		label =ttk.Label(self,text="Graph Page").pack(padx=10,pady=10)


		b1 = ttk.Button(self,text="To Home",command=lambda :controller.show_frame(0))
		b1.pack()




		canvas = FigureCanvasTkAgg(f,self)
		canvas.draw()

		canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)



		toolbar = NavigationToolbar2Tk(canvas,self)
		toolbar.update()

		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)











class SeaofBTCapp(tk.Tk):

	def __init__(self,*args,**kwargs):



		tk.Tk.__init__(self,*args,**kwargs)

		container = tk.Frame(self)
		container.pack(side="top",fill="both",expand=True)


		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)


		self.frames  = {}



		pages = [StartPage,BTC_PAGE]





		for idx,F in enumerate(pages):

			frame = F(container,self)

			self.frames[idx] = frame

			frame.grid(row=0,column=0,sticky='nsew')




		


		self.show_frame(0)




	def show_frame(self,cont):

		frame = self.frames[cont]
		frame.tkraise()





app = SeaofBTCapp()
app.geometry("400x300")
app.title("Nova BTC")


ani = FuncAnimation(f,animate,interval=1000)
plt.show()

app.mainloop()

