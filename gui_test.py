"""
C:\Users\Flyknit\AppData\Local\Programs\Python\Python37\Scripts\pyuic5.exe "C:\Users\Flyknit\Dropbox\Dev Soft\App - TriTout\gui.ui"
"""
import sys
from PyQt5.QtWidgets import QApplication, QLabel


def window():
    app = QApplication([])
    app.setStyle('Fusion')
    label = QLabel('Hello World!')
    label.show()

    app.exec_()

window()
