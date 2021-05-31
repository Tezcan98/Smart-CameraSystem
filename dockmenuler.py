from PyQt5 import QtCore, QtGui, QtWidgets

style = "border-style: outset;\nborder-width: 2px;\nborder-radius: 10px;\nborder-color: beige;\nfont: bold 14px;\npadding: 6px;"

class Dock_menu: 
    def __init__(self,MainWindow, ikon_url, base):
        self.dock_menu = QtWidgets.QDockWidget(MainWindow)
        self.dock_menu.setMinimumSize(QtCore.QSize(95, 100))
        self.dock_menu.setMaximumSize(QtCore.QSize(600, 800)) 
        self.dock_menu.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.dock_menu_icerik = QtWidgets.QWidget() 
        self.dock_menu.setWidget(self.dock_menu_icerik)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(base), self.dock_menu)
    
        self.ikon_ayarlari(ikon_url) 
        self.boyut=[0, 0]
        self.durum = False
        self.boyut_ayarla()
 
    def ikon_ayarlari(self, ikon_url):
       
        self.button = QtWidgets.QPushButton(self.dock_menu_icerik)
        self.button.setGeometry(QtCore.QRect(0, 0, 80, 70))  
        self.button.setBaseSize(QtCore.QSize(100, 0))
        self.button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button.setStyleSheet(style + "background-color:rgb(222, 234, 238)")
        self.button.clicked.connect(self.on_click)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ikon_url), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button.setIcon(icon)
        self.button.setIconSize(QtCore.QSize(60, 60))

    def boyut_ayarla(self): 
        if self.durum:
            self.boyut = [500, 300]
            self.button.setStyleSheet(style + "background-color:rgb(188, 212, 220)")
        else:
            self.boyut = [75, 100]
            self.button.setStyleSheet(style + "background-color:rgb(222, 234, 238)")
        self.dock_menu.setFixedSize(QtCore.QSize(self.boyut[0], self.boyut[1]))   
    
    def on_click(self): 
        self.durum = bool(self.durum ^ 1 ) 
        self.boyut_ayarla()