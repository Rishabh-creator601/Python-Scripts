import sys,json,os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from snip_path import SnipPath
from jsonDB import JsonDB 
import pyperclip as pc


class SnipXPage(QWidget,SnipPath):

   def __init__(self):
    super().__init__()




    self.manage_snippy_path()

    self.snippets_path = self.get_snippy_path()
    self.db = JsonDB(self.snippets_path)



    self.layout = QVBoxLayout()
    self.layout.setAlignment(Qt.AlignTop)



    self.details = QLabel()
    self.details.setText(f"Total Snippets Found : {len(self.db.read().keys())}")


    self.list_snip = QListWidget()
    self.list_snip.addItems(list(self.db.read().keys()))
    self.list_snip.currentTextChanged.connect(self.show_snips)




    self.display = QTextEdit()



    self.copy_btn  = QPushButton("Copy Text")
    self.copy_btn.clicked.connect(self.copy_text)




    self.layout.addWidget(self.details)
    self.layout.addWidget(self.list_snip)
    self.layout.addWidget(self.display)
    self.layout.addWidget(self.copy_btn)





    self.setLayout(self.layout)
  

   def show_snips(self,i):
      code = self.db.read()[i]
      self.display.setPlainText(code)
  	   


   def copy_text(self):

      pc.copy(self.display.toPlainText())
      self.copy_btn.setText("Copied!")





