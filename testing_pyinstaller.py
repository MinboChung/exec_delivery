import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class window(QWidget):
   def __init__(self, parent = None):
      super(window, self).__init__(parent)
      self.resize(200,50)
      self.setWindowTitle("From Minbo Chung")
      self.label = QLabel(self)
      self.label.setText("Testing")
      font = QFont()
      font.setFamily("Arial")
      font.setPointSize(26)
      self.label.setFont(font)
      self.label.move(50,20)
def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()