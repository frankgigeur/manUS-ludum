from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

import qtawesome as qta
import utils
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("itération 1 : interface de jeux")
        self.setGeometry(0, 0, 1900, 980)
        self.container = QWidget()
        self.setCentralWidget(self.container)

        self.l1 = QLabel(self)
        self.set_etiquette(self.l1, "why is life", 10, 0)
        self.b1 = QPushButton(self)
        self.set_bouton(self.b1, "because", 10, 40)
        self.b1.clicked.connect(self.show_popup)
        # self.b1.clicked.connect(lambda: self.on_button_clicked_change_label(self.l1, "ok"))

    @staticmethod
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on PyQt5")
        msg.setText("This is the main text!")
        msg.setIcon(QMessageBox.Question)

        x = msg.exec_()

    @staticmethod
    def set_etiquette(obj, text, x, y):
        obj.setText(text)
        obj.move(x, y)  # x, y from top left hand corner.

    @staticmethod
    def set_bouton(obj, text, x, y):
        obj.setText(text)
        obj.move(x, y)  # x, y from top left hand corner.

    # @staticmethod
    # def on_button_clicked_change_label(obj_to_change, text):
    #    obj_to_change.setText(text)
    #    obj_to_change.update()

    # def update(self):
    #    self.l1.adjustSize()
