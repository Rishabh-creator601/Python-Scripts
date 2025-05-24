import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from factorial import factorial


class NumberPage(QWidget):
  def __init__(self):
    super().__init__()
    self.layout = QVBoxLayout()
    self.layout.setAlignment(Qt.AlignTop)


    self.label = QLabel("Factorial :")
    self.no = QLineEdit()
    self.no.setPlaceholderText("Enter Number :")
    self.no.returnPressed.connect(self.get_factorial)

    self.layout.addWidget(self.label)
    self.layout.addWidget(self.no)


    self.setLayout(self.layout)


  def get_factorial(self):

    number = self.no.text()
    ans =  0

    if "," in  number:
      step,stop = int(number.split(",")[0]),int(number.split(",")[1])
      ans = factorial(step=step,stop=stop)


    else:
      stop = int(number)
      ans = factorial(stop=stop)


    self.no.setText(str(ans))