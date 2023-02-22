from PyQt5.QtCore import QThread, pyqtSignal
import serial as pyserial
import time


class CommWorker(QThread):
    textReceived = pyqtSignal(str)
    startMarker = '<'
    endMarker = '>'
    dataStarted = False
    dataBuf = ""
    messageComplete = False
    connected = True

    def __init__(self, comPort:str = "COM1", baudRate:int = 115200):
        QThread.__init__(self)

        try:
            self.serial = pyserial.Serial(comPort,baudRate,timeout=0, rtscts=True)
            print("Serial port " + comPort + " opened  Baudrate " + str(baudRate))
            #self.waitForArduino()
        except:
            self.connected = False




    def run(self):

        while True:
            if self.connected:
                arduinoReply = self.recvLikeArduino()
                if not (arduinoReply == 'XXX'):
                    self.textReceived.emit(f'arduinoreply : {arduinoReply}')



    def kill(self):
        self.terminate()


    def sendToArduino(self,stringToSend):
        # this adds the start- and end-markers before sending

        print(stringToSend)
        stringWithMarkers = (self.startMarker)
        stringWithMarkers += stringToSend
        stringWithMarkers += (self.endMarker)

        self.serial.write(stringWithMarkers.encode('utf-8'))  # encode needed for Python3


    # ==================

    def recvLikeArduino(self):

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

    # ==================


    def waitForArduino(self):
        # wait until the Arduino sends 'Arduino is ready' - allows time for Arduino reset
        # it also ensures that any bytes left over from a previous message are discarded

        print("Waiting for Arduino to reset")

        msg = ""
        while msg.find("Arduino is ready") == -1:
            msg = self.recvLikeArduino()
            if not (msg == 'XXX'):
                print(msg)


# ====================
# ====================
# the program


