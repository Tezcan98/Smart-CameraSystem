from PyQt5 import QtCore, QtGui, QtWidgets 


style = "border-style: outset;\nborder-width: 2px;\nborder-radius: 10px;\nborder-color: beige;\nfont: bold 14px;\npadding: 6px;"

class Kameralar: 
    def __init__(self,Window):
        self.tabWidget = QtWidgets.QTabWidget(Window)
        self.tabWidget.setGeometry(QtCore.QRect(100, 10, 400, 400))
   
        self.Ayarlar = QtWidgets.QWidget()  
        self.Kameralar_Listesi = QtWidgets.QWidget() 
        
        self.tabWidget.addTab(self.Ayarlar, "Kamera Seçenekleri")
        self.tabWidget.addTab(self.Kameralar_Listesi, "Kamera Listesi")
        

    def Toggle_dissable(self, target):
        state = target.isEnabled() 
        target.setEnabled(bool(state ^ 1 )) # toggled

    def checkBox(self, parent, geo, text = "", enabled = True, checked= False):
        checkBox = QtWidgets.QCheckBox(parent)
        checkBox.setEnabled(enabled)
        checkBox.setChecked(checked)
        checkBox.setText(text)
        checkBox.setGeometry(geo)
        return checkBox