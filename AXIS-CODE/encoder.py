from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from encodings_name import encodings_list
from convert import Coder
from pyperclip import copy 


class EncoderPage(QWidget):
	def __init__(self):
		super().__init__()
		self.layout = QVBoxLayout()
		self.layout.setAlignment(Qt.AlignTop)




		#Widgets 


		self.label = QLabel("Choose Encoding :")

		self.choices = QComboBox()
		self.choices.addItems(encodings_list)

		self.text =QLineEdit()
		self.text.setText("Hello World")
		self.text.setPlaceholderText("Press Enter after Text")
		self.text.returnPressed.connect(self.encode_text)

		self.display = QTextEdit()
		self.display.hide()


		self.copy_btn =QPushButton("Copy Me")
		self.copy_btn.clicked.connect(self.copy_)
		self.copy_btn.hide()


		self.back =QPushButton("< Back ")
		self.back.clicked.connect(self.back_)
		self.back.hide()







		#Add Widgets
		self.layout.addWidget(self.label)
		self.layout.addWidget(self.choices)
		self.layout.addWidget(self.text)
		self.layout.addWidget(self.display)
		self.layout.addWidget(self.copy_btn)
		self.layout.addWidget(self.back)





		self.setLayout(self.layout)



	def encode_text(self):
		string = self.text.text()
		encoded  = Coder(encoding=self.choices.currentText(),text=string).ans
		self.display.show()
		self.back.show()
		self.display.setPlainText(str(encoded))
		self.copy_btn.show() 
		self.setFixedSize(QSize(600,400))


	def copy_(self):
		copy(self.display.toPlainText())
		self.copy_btn.setText("Copied")

	def back_(self):
		self.display.hide()
		self.copy_btn.hide()
		self.back.hide()
		


