from PyQt5 import QtCore, QtGui, QtWidgets

style = "border-style: outset;\nborder-width: 2px;\nborder-radius: 10px;\nborder-color: beige;\nfont: bold 14px;\npadding: 6px;"

class Options: 
    def __init__(self,Window):
        self.tabWidget = QtWidgets.QTabWidget(Window)
        self.tabWidget.setGeometry(QtCore.QRect(100, 10, 400, 400))
  
        self.main_tab = QtWidgets.QWidget() 
        self.Kaydetme_tab = QtWidgets.QWidget() 
        self.Nesne_Tespiti_tab = QtWidgets.QWidget() 
        self.Hareket_algilama_tab = QtWidgets.QWidget() 

        self.kaydetme_secenekleri()
        self.yakalama_secenekleri() 
        self.nesne_tespiti_seçenekleri() 
        self.hareket_algilama_secenekleri() 

        self.tabWidget.addTab(self.main_tab, "Yakalama Seçenekleri") 
        self.tabWidget.addTab(self.Kaydetme_tab, "Kaydetme Seçenekleri")
        self.tabWidget.addTab(self.Hareket_algilama_tab, "Hareket Tespiti Seçenekleri")
        self.tabWidget.addTab(self.Nesne_Tespiti_tab, "Cisim Tespit Seçenekleri")

    def kaydetme_secenekleri(self):
        self.KaydetmeBox = QtWidgets.QGroupBox(self.Kaydetme_tab)
        self.KaydetmeBox.setTitle("Kaydetme Konumu")
        self.KaydetmeBox.setGeometry(QtCore.QRect(10, 10, 600, 201)) 

        self.label = QtWidgets.QLabel(self.KaydetmeBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 100, 35)) 
        self.label.setText("Video Kayıt")
         
        self.pathText1 = QtWidgets.QLineEdit(self.KaydetmeBox)
        self.pathText1.setGeometry(QtCore.QRect(100, 50, 201, 35)) 

        self.pathText2 = QtWidgets.QLineEdit(self.KaydetmeBox)
        self.pathText2.setGeometry(QtCore.QRect(100, 100, 201, 35))
        
        self.label2 = QtWidgets.QLabel(self.KaydetmeBox)
        self.label2.setGeometry(QtCore.QRect(10, 100, 100, 35))
        self.label2.setText("Yakalama Kayıt")
        
        #self.Gozat2 = QtWidgets.QPushButton(self.KaydetmeBox)
        #self.Gozat2.setGeometry(QtCore.QRect(150, 150, 75, 30)) 

        # TODO
        self.Gozat1 = QtWidgets.QPushButton(self.KaydetmeBox)
        self.Gozat1.setGeometry(QtCore.QRect(10, 120, 50, 50)) 
        self.Gozat1.setText("Gözat")
        self.Gozat2 = QtWidgets.QPushButton(self.KaydetmeBox)
        self.Gozat2.setGeometry(QtCore.QRect(10, 120, 50, 50)) 
        self.Gozat2.setText("Gözat")
        #self.Gozat2.clicked.connect(self.prn)

    def yakalama_secenekleri(self):
        self.GrupBox = QtWidgets.QGroupBox(self.main_tab)
        self.GrupBox.setGeometry(QtCore.QRect(10, 10, 400, 151)) 
        #self.GrupBox.setTitle("Yakalama Hassasiyeti")
        self.Video_kayit_aktif = self.checkBox(self.GrupBox, QtCore.QRect(10, 10, 150, 50), text= "Video Kayıt Aktif", checked= True)
        self.Hareket_tespiti_aktif = self.checkBox(self.GrupBox, QtCore.QRect(10, 60, 150, 50), text= "Hareket Tespiti Aktif", checked= True)
        self.Nesne_tespiti_aktif = self.checkBox(self.GrupBox, QtCore.QRect(10, 110, 150, 50), text= "Nesne Tespiti Aktif", checked= True)
        
        self.Video_kayit_aktif.stateChanged.connect(lambda:self.Toggle_dissable(self.Kaydetme_tab))
        self.Hareket_tespiti_aktif.stateChanged.connect(lambda:self.Toggle_dissable(self.Hareket_algilama_tab))
        self.Nesne_tespiti_aktif.stateChanged.connect(lambda:self.Toggle_dissable(self.Nesne_Tespiti_tab))

    #TODO Hangi nesneler tespit edilsin, görüntü üzerinde kare olsun mu, Tespit Anında Alarm (Saat aralığı), 
    # Nesne tespitinde her x saniyede bir kaydet 
    def nesne_tespiti_seçenekleri(self):
        print("fd")
        
    #TODO Hareket Algılama hassasiyeti, Hareket Anında Alarm (Saat aralığı), 
    # hareket algılamada her x saniyede bir kaydet
    def hareket_algilama_secenekleri(self):
        print("fd")

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