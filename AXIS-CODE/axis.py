import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from numbers_gui import NumberPage
from snipx import SnipXPage
from encoder import EncoderPage


# Sample 

class CustomWidget(QWidget):
  def __init__(self, name):
    super().__init__()
    self.layout = QVBoxLayout()
    self.layout.setAlignment(Qt.AlignTop)


    self.label = QLabel(name)

    self.layout.addWidget(self.label)



    self.setLayout(self.layout)










class MainWindow(QMainWindow):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Axis - X$Y")
    self.setFixedSize(QSize(800,500))
    tabs = QTabWidget()
    tabs.setTabPosition(QTabWidget.North)
    tabs.setMovable(True)

    tabs.addTab(SnipXPage(),"SnipX")
    tabs.addTab(NumberPage(),"Number Programs")
    tabs.addTab(EncoderPage(),"Encoder")

    self.setCentralWidget(tabs)
  






app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()