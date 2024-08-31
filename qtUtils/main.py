from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *





def button(text,width=None,height=None,func=None,hide=False):

	btn = QPushButton(text)

	if width != None:
		btn.setFixedWidth(width)

	if height != None:
		btn.setFixedHeight(height)

	if func != None:
		btn.clicked.connect(func)

	if hide == True:
		btn.hide()

	return btn 



def take_input(placeholderText=''):

	a = QLineEdit()
	a.setPlaceholderText(placeholderText)
	return a


	



