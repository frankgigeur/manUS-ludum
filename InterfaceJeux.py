# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfaceJeux.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *


class UiManUSludumInterface(object):

    # Variable globale du décompte
    nbDecompte = 5
    count = 0
    start = False

    def setup_ui(self, ManUS_ludum_Interface):
        """
        Initialisation du UI et de toutes ces composantes

        :param ManUS_ludum_Interface:
        :return:
        """

        # Initialisation de la fenêtre principale
        ManUS_ludum_Interface.setObjectName("ManUS_ludum_Interface")
        ManUS_ludum_Interface.resize(1620, 958)
        self.centralwidget = QtWidgets.QWidget(ManUS_ludum_Interface)
        self.centralwidget.setObjectName("centralwidget")

        # Initialisation de l'entête
        self.header = QtWidgets.QGroupBox(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(10, 10, 1600, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.header.setFont(font)
        self.header.setTitle("")
        self.header.setFlat(False)
        self.header.setObjectName("header")

        # Bouton qui permet de lancer le décompte (débute la partie)
        self.boutonLancementJeux = QtWidgets.QPushButton(self.header)
        self.boutonLancementJeux.setGeometry(QtCore.QRect(10, 10, 700, 50))
        self.boutonLancementJeux.setObjectName("boutonLancementJeux")
        self.boutonLancementJeux.clicked.connect(self.decompte)

        # Bouton qui fait apparaître un popup qui explique comment jouer
        self.boutonInfo = QtWidgets.QPushButton(self.header)
        self.boutonInfo.setGeometry(QtCore.QRect(1540, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.boutonInfo.setFont(font)
        self.boutonInfo.setObjectName("boutonInfo")
        self.boutonInfo.clicked.connect(self.show_popup)

        # Nom du projet (label)
        self.titre = QtWidgets.QLabel(self.header)
        self.titre.setGeometry(QtCore.QRect(720, 10, 810, 50))
        font = QtGui.QFont()
        font.setPointSize(37)
        self.titre.setFont(font)
        self.titre.setAutoFillBackground(False)
        self.titre.setAlignment(QtCore.Qt.AlignCenter)
        self.titre.setObjectName("titre")

        # Initialisation de la section de contrôle du robot
        self.robot = QtWidgets.QGroupBox(self.centralwidget)
        self.robot.setGeometry(QtCore.QRect(10, 85, 350, 570))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.robot.setFont(font)
        self.robot.setTitle("")
        self.robot.setObjectName("robot")

        # Nom de la section (label)
        self.titreContMain = QtWidgets.QLabel(self.robot)
        self.titreContMain.setGeometry(QtCore.QRect(10, 10, 330, 90))
        self.titreContMain.setAutoFillBackground(True)
        self.titreContMain.setFrameShape(QtWidgets.QFrame.Box)
        self.titreContMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titreContMain.setLineWidth(2)
        self.titreContMain.setAlignment(QtCore.Qt.AlignCenter)
        self.titreContMain.setObjectName("titreContMain")

        # Bouton qui indique à la main de jouer roche
        self.boutonRobotRoche = QtWidgets.QPushButton(self.robot)
        self.boutonRobotRoche.setGeometry(QtCore.QRect(35, 160, 280, 90))
        self.boutonRobotRoche.setObjectName("boutonRobotRoche")

        # Bouton qui indique à la main de jouer papier
        self.boutonRobotPapier = QtWidgets.QPushButton(self.robot)
        self.boutonRobotPapier.setGeometry(QtCore.QRect(35, 260, 280, 90))
        self.boutonRobotPapier.setObjectName("boutonRobotPapier")

        # Bouton qui indique à la main de jouer ciseaux
        self.boutonRobotCiseaux = QtWidgets.QPushButton(self.robot)
        self.boutonRobotCiseaux.setGeometry(QtCore.QRect(35, 360, 280, 90))
        self.boutonRobotCiseaux.setObjectName("boutonRobotCiseaux")

        # Initialisation de la section de contrôle de l'humain
        self.humain = QtWidgets.QGroupBox(self.centralwidget)
        self.humain.setGeometry(QtCore.QRect(370, 85, 350, 570))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.humain.setFont(font)
        self.humain.setTitle("")
        self.humain.setObjectName("humain")

        # Nom de la section (label)
        self.titreContHum = QtWidgets.QLabel(self.humain)
        self.titreContHum.setGeometry(QtCore.QRect(10, 10, 330, 90))
        self.titreContHum.setAutoFillBackground(True)
        self.titreContHum.setFrameShape(QtWidgets.QFrame.Box)
        self.titreContHum.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titreContHum.setLineWidth(2)
        self.titreContHum.setAlignment(QtCore.Qt.AlignCenter)
        self.titreContHum.setObjectName("titreContHum")

        # Bouton qui indique que l'humain à joué roche
        self.boutonHumainRoche = QtWidgets.QPushButton(self.humain)
        self.boutonHumainRoche.setGeometry(QtCore.QRect(35, 160, 280, 90))
        self.boutonHumainRoche.setObjectName("boutonHumainRoche")

        # Bouton qui indique que l'humain à joué papier
        self.boutonHumainPapier = QtWidgets.QPushButton(self.humain)
        self.boutonHumainPapier.setGeometry(QtCore.QRect(35, 260, 280, 90))
        self.boutonHumainPapier.setObjectName("boutonHumainPapier")

        # Bouton qui indique que l'humain à joué ciseaux
        self.boutonHumainCiseaux = QtWidgets.QPushButton(self.humain)
        self.boutonHumainCiseaux.setGeometry(QtCore.QRect(35, 360, 280, 90))
        self.boutonHumainCiseaux.setObjectName("boutonHumainCiseaux")

        # Initialisation de la section Statistiques
        self.statistiques = QtWidgets.QGroupBox(self.centralwidget)
        self.statistiques.setGeometry(QtCore.QRect(10, 659, 710, 271))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.statistiques.setFont(font)
        self.statistiques.setTitle("")
        self.statistiques.setObjectName("statistiques")

        # Bouton qui réinitialise les statistiques
        self.boutonStatsReset = QtWidgets.QPushButton(self.statistiques)
        self.boutonStatsReset.setGeometry(QtCore.QRect(10, 10, 150, 40))
        self.boutonStatsReset.setObjectName("boutonStatsReset")

        # Nom de la section (label)
        self.titreStats = QtWidgets.QLabel(self.statistiques)
        self.titreStats.setGeometry(QtCore.QRect(170, 10, 531, 40))
        self.titreStats.setAutoFillBackground(True)
        self.titreStats.setFrameShape(QtWidgets.QFrame.Box)
        self.titreStats.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titreStats.setLineWidth(2)
        self.titreStats.setAlignment(QtCore.Qt.AlignCenter)
        self.titreStats.setObjectName("titreStats")

        # Texte des stats de l'AI (label)
        self.statsAIwin = QtWidgets.QLabel(self.statistiques)
        self.statsAIwin.setGeometry(QtCore.QRect(10, 90, 510, 25))
        self.statsAIwin.setObjectName("statsAIwin")

        # Indicateur numérique du nombre de victoire de l'AI
        self.nbAiWin = QtWidgets.QLCDNumber(self.statistiques)
        self.nbAiWin.setGeometry(QtCore.QRect(530, 90, 170, 25))
        self.nbAiWin.setObjectName("nbAiWin")

        # Indicateur numérique du nombre de victoire de l'humain
        self.nbHumWin = QtWidgets.QLCDNumber(self.statistiques)
        self.nbHumWin.setGeometry(QtCore.QRect(530, 140, 170, 25))
        self.nbHumWin.setObjectName("nbHumWin")

        # Texte des stats de l'humain (label)
        self.statsHumWin = QtWidgets.QLabel(self.statistiques)
        self.statsHumWin.setGeometry(QtCore.QRect(10, 140, 510, 25))
        self.statsHumWin.setObjectName("statsHumWin")

        # Indicateur numérique du pourcentage de roche
        self.pourcentRoche = QtWidgets.QLCDNumber(self.statistiques)
        self.pourcentRoche.setGeometry(QtCore.QRect(10, 200, 75, 50))
        self.pourcentRoche.setSmallDecimalPoint(False)
        self.pourcentRoche.setObjectName("pourcentRoche")

        # Texte des stats pourcentage de roche (label)
        self.statsRoche = QtWidgets.QLabel(self.statistiques)
        self.statsRoche.setGeometry(QtCore.QRect(95, 200, 125, 50))
        self.statsRoche.setObjectName("statsRoche")

        # Texte des stats pourcentage de papier (label)

        self.statsPapier = QtWidgets.QLabel(self.statistiques)
        self.statsPapier.setGeometry(QtCore.QRect(335, 200, 125, 50))
        self.statsPapier.setObjectName("statsPapier")

        # Indicateur numérique du pourcentage de papier
        self.pourcentPapier = QtWidgets.QLCDNumber(self.statistiques)
        self.pourcentPapier.setGeometry(QtCore.QRect(250, 200, 75, 50))
        self.pourcentPapier.setSmallDecimalPoint(False)
        self.pourcentPapier.setObjectName("pourcentPapier")

        # Texte des stats pourcentage de ciseaux (label)
        self.statsCiseaux = QtWidgets.QLabel(self.statistiques)
        self.statsCiseaux.setGeometry(QtCore.QRect(575, 200, 125, 50))
        self.statsCiseaux.setObjectName("statsCiseaux")

        # Indicateur numérique du pourcentage de ciseaux
        self.pourcentCiseaux = QtWidgets.QLCDNumber(self.statistiques)
        self.pourcentCiseaux.setGeometry(QtCore.QRect(490, 200, 75, 50))
        self.pourcentCiseaux.setSmallDecimalPoint(False)
        self.pourcentCiseaux.setObjectName("pourcentCiseaux")

        # Initialisation de la section de la caméra
        self.camera = QtWidgets.QGroupBox(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(730, 85, 880, 610))
        self.camera.setObjectName("camera")

        # Widget qui contient la caméra
        self.camHolder = QtWidgets.QTabWidget(self.camera)
        self.camHolder.setGeometry(QtCore.QRect(10, 10, 860, 590))
        self.camHolder.setTabPosition(QtWidgets.QTabWidget.South)
        self.camHolder.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.camHolder.setUsesScrollButtons(False)
        self.camHolder.setObjectName("camHolder")

        self.available_cameras = QCameraInfo.availableCameras()
        self.viewfinder = QCameraViewfinder()
        self.viewfinder.show()

        self.camHolder.addTab(self.viewfinder, self.available_cameras[0].description())
        self.select_camera(0)

        # Initialisation de la section du décompte
        self.decompte = QtWidgets.QGroupBox(self.centralwidget)
        self.decompte.setGeometry(QtCore.QRect(730, 700, 880, 230))
        self.decompte.setObjectName("decompte")

        # Texte du décompte
        self.txtDecompte = QtWidgets.QLabel(self.decompte)
        self.txtDecompte.setGeometry(QtCore.QRect(10, 20, 860, 200))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.txtDecompte.setFont(font)
        self.txtDecompte.setAutoFillBackground(False)
        self.txtDecompte.setAlignment(QtCore.Qt.AlignCenter)
        self.txtDecompte.setObjectName("txtDecompte")

        # Initialisation de la barre de statut
        ManUS_ludum_Interface.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ManUS_ludum_Interface)
        self.statusbar.setObjectName("statusbar")
        ManUS_ludum_Interface.setStatusBar(self.statusbar)

        # Écriture des étiquettes et connexion des fenêtres
        self.retranslate_ui(ManUS_ludum_Interface)
        QtCore.QMetaObject.connectSlotsByName(ManUS_ludum_Interface)

    def retranslate_ui(self, ManUS_ludum_Interface):
        """
        Fonction qui écrit le texte des différents composants de l'interface
        (fonction de QtDesigner)

        :param ManUS_ludum_Interface:
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        ManUS_ludum_Interface.setWindowTitle(_translate("ManUS_ludum_Interface", "ManUS ludum Interface"))
        self.boutonLancementJeux.setText(_translate("ManUS_ludum_Interface", "Commencer la partie"))
        self.titre.setText(_translate("ManUS_ludum_Interface", "ManUS ludum"))
        self.boutonInfo.setText(_translate("ManUS_ludum_Interface", "i"))
        self.titreContMain.setText(_translate("ManUS_ludum_Interface", "Contrôle de la main"))
        self.boutonRobotRoche.setText(_translate("ManUS_ludum_Interface", "Roche"))
        self.boutonRobotPapier.setText(_translate("ManUS_ludum_Interface", "Papier"))
        self.boutonRobotCiseaux.setText(_translate("ManUS_ludum_Interface", "Ciseaux"))
        self.boutonHumainRoche.setText(_translate("ManUS_ludum_Interface", "Roche"))
        self.titreContHum.setText(_translate("ManUS_ludum_Interface", "Correction de votre coup"))
        self.boutonHumainCiseaux.setText(_translate("ManUS_ludum_Interface", "Ciseaux"))
        self.boutonHumainPapier.setText(_translate("ManUS_ludum_Interface", "Papier"))
        self.boutonStatsReset.setText(_translate("ManUS_ludum_Interface", "Réinitialisation"))
        self.titreStats.setText(_translate("ManUS_ludum_Interface", "Statistiques de jeux"))
        self.statsAIwin.setText(_translate("ManUS_ludum_Interface", "Nombre de partie gagnée par ManUS :"))
        self.statsHumWin.setText(_translate("ManUS_ludum_Interface", "Nombre de partie que vous avez gagnée :"))
        self.statsRoche.setText(_translate("ManUS_ludum_Interface", "% Roche"))
        self.statsPapier.setText(_translate("ManUS_ludum_Interface", "% Papier"))
        self.statsCiseaux.setText(_translate("ManUS_ludum_Interface", "% Ciseaux"))
        self.txtDecompte.setText(_translate("ManUS_ludum_Interface", "En Attente"))

    @staticmethod
    def show_popup():
        """
        Fonction qui affiche le popup d'information du jeux

        :return:
        """
        msg = QMessageBox()
        msg.setWindowTitle("Comment jouer?")
        msg.setText("   Pour lancer la partie cliquez sur 'Commencer la partie' .\n"
                    "   Fiez-vous ensuite au décompte en-bas à droite\n   et jouez votre coup sur 'Ciseaux' .\n")
        msg.setIcon(QMessageBox.Question)

        msg.exec_()

    def countdown(self):

        _translate = QtCore.QCoreApplication.translate

        if self.start:
            if self.count < 1:
                self.txtDecompte.setText(_translate("ManUS_ludum_Interface", "En Attente"))
                self.count = self.nbDecompte
                self.start = False
            elif self.count == 5:
                self.txtDecompte.setText(_translate("ManUS_ludum_Interface", "Prêt?"))
                self.count = self.count - 1
            elif self.count == 4:
                self.txtDecompte.setText(_translate("ManUS_ludum_Interface", "C'est parti!"))
                self.count = self.count - 1
            elif self.count == 3:
                self.txtDecompte.setText(_translate("ManUS_ludum_Interface", "Roche"))
                self.count = self.count - 1
            elif self.count == 2:
                self.txtDecompte.setText(_translate("ManUS_ludum_Interface", "Papier"))
                self.count = self.count - 1
            elif self.count == 1:
                self.txtDecompte.setText(_translate("ManUS_ludum_Interface", "Ciseaux"))
                self.count = self.count - 1

    def decompte(self):
        self.start = True
        self.count = self.nbDecompte

    def select_camera(self, i):

        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)

        # setting capture mode to the camera
        self.camera.setCaptureMode(QCamera.CaptureVideo)

        # start the camera
        self.camera.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ManUS_ludum_Interface = QtWidgets.QMainWindow()
    ui = UiManUSludumInterface()
    ui.setup_ui(ManUS_ludum_Interface)
    ManUS_ludum_Interface.show()

    # Timer pour le décompte
    timer = QTimer()
    timer.timeout.connect(ui.countdown)
    timer.start(1000)

    sys.exit(app.exec_())