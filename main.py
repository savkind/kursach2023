import sys
from MainWindow import *
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()