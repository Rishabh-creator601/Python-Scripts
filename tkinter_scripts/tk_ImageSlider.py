from tkinter import * 
from PIL import ImageTk,Image
import os 

root = Tk()


def load_img(path):
    img =  Image.open(path).resize((500,500))
    img = ImageTk.PhotoImage(img)
    return img
	
	
	
class imgController:
	
	def __init__(self):
		self.imgno = 0
	
	
	def fwd_img(self):
		self.imgno += 1
		
		
		try :
			screen.configure(image=img_list[self.imgno])
			tag.configure(text=self.imgno)
		
		except:
			self.imgno = -1
			self.fwd_img()
	
	
	
	def bwd_img(self):
			self.imgno -=1 
			try:
				screen.configure(image=img_list[self.imgno])
				tag.configure(text=self.imgno)
			
			except:
				self.imgno = 4
				self.bwd_img()
			
			
				

				
			

		  
		
# Just change the path of images set 
		
imgT = imgController()

img1= load_img("C:/Users/RISHABH/Pictures/images/cat.jpg")
img2 = load_img("C:/Users/RISHABH/Pictures/images/humanImg.jpg")
img3 = load_img("C:/Users/RISHABH/Pictures/images/image.jpg")
img4 = load_img("C:/Users/RISHABH/Pictures/images/Modi.jpg")


img_list= [img1,img2,img3,img4]






screen = Label(root,image=img_list[imgT.imgno])
screen.pack()


tag = Label(root,text=imgT.imgno)
tag.pack()

btn = Button(root,text="quit",command=root.quit).pack()


fwd= Button(root,text=">>>",command=imgT.fwd_img)
fwd.pack()



bwd= Button(root,text="<<<",command=imgT.bwd_img)
bwd.pack()



root.mainloop()
