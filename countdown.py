import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

nbDecompte = 5

app = QApplication(sys.argv)

label = QLabel()
label.resize(360, 40)
label.show()

count = nbDecompte


def countdown():
    global count
    if count < 1:
        count = nbDecompte

    if count == 5:
        label.setText("Prêt ?")
        count = count - 1
    elif count == 4:
        label.setText("C'est parti!")
        count = count - 1
    elif count == 3:
        label.setText("Roche")
        count = count - 1
    elif count == 2:
        label.setText("Papier")
        count = count - 1
    elif count == 1:
        label.setText("Ciseaux")
        count = count - 1


timer = QTimer()
timer.timeout.connect(countdown)
timer.start(1000)

app.exec_()
