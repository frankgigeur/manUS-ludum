from PyQt5.QtCore import QThread, pyqtSignal
import serial as pyserial


class CommWorker(QThread):
    textReceived = pyqtSignal(str)
    startMarker = '<'
    endMarker = '>'
    dataStarted = False
    dataBuf = ""
    messageComplete = False
    connected = True

    def __init__(self, comPort:str = "COM1", baudRate:int = 115200):
        """
        Initialisation de la communication sérielle et du fil d'exécution

        :param comPort:
        :param baudRate:
        """
        QThread.__init__(self)

        try:
            self.serial = pyserial.Serial(comPort,baudRate, timeout=0, rtscts=True)
            print("Serial port " + comPort + " opened  Baudrate " + str(baudRate))
        except:
            self.connected = False

    def run(self):
        """
        Boucle du fil, s'exécute en continu
        Ici on lit les messages reçu de l'arduino et on notifie l'interface lors d'un changement

        :return:
        """

        while True:
            if self.connected:
                arduinoReply = self.recvLikeArduino()
                if not (arduinoReply == 'XXX'):
                    self.textReceived.emit(f'arduinoreply : {arduinoReply}')

    def kill(self):
        """
        Fonction qui met fin au fil

        :return:
        """
        self.terminate()

    def sendToArduino(self,stringToSend):
        """
        Ajoute des marqueurs de début et de fin et envoit le message à l'arduino

        :param stringToSend:
        :return:
        """

        print(stringToSend)
        stringWithMarkers = (self.startMarker)
        stringWithMarkers += stringToSend
        stringWithMarkers += (self.endMarker)

        self.serial.write(stringWithMarkers.encode('utf-8'))  # encode needed for Python3

    def recvLikeArduino(self):
        """
        Fonction permettant de lire la réponse de l'arduino

        :return:
        """

        if self.serial.inWaiting() > 0 and self.messageComplete == False:
            x = self.serial.read().decode("utf-8")  # decode needed for Python3

            if self.dataStarted == True:
                if x != self.endMarker:
                    self.dataBuf = self.dataBuf + x
                else:
                    self.dataStarted = False
                    self.messageComplete = True
            elif x == self.startMarker:
                self.dataBuf = ''
                self.dataStarted = True

        if (self.messageComplete == True):
            self.messageComplete = False
            return self.dataBuf
        else:
            return "XXX"



