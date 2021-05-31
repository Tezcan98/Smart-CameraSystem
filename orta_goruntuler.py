from PyQt5 import QtCore, QtGui, QtWidgets
import math
 

class Goruntuler: 
    def __init__(self,MainWindow): 
        self.centralwidget = QtWidgets.QWidget(MainWindow)  
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1800, 900)) 
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)  
        MainWindow.setCentralWidget(self.centralwidget)

        self.goruntu_tablo_olustur(9)

        # self.Goruntuler = []
    
    def goruntu_tablo_olustur(self,times):
        # self.Goruntuler = []

        for i in range(times):  
            self.Kamera_Goruntusu = QtWidgets.QGroupBox(self.gridLayoutWidget)
            self.Kamera_Goruntusu.setStyleSheet("font: 25 10pt \"Bahnschrift\";") 
            self.graphicsView_8 = QtWidgets.QGraphicsView(self.Kamera_Goruntusu)
            self.graphicsView_8.setGeometry(QtCore.QRect(0, 20, 896, 431))
            self.graphicsView_8.setStyleSheet("border: 3px solid #a2b9bc;\n""border-radius: 16px;\n""background: rgba(250,250,250,0.96);") 
            self.gridLayout.addWidget(self.Kamera_Goruntusu, i%math.sqrt(times), i/math.sqrt(times), 1, 1)

    #def kameradan_al(self,component):


