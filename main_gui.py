# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from dockmenuler import Dock_menu
from options_window import Options
from camera_window import Kameralar
from orta_goruntuler import Goruntuler

icons = {"setting": "icons/settings.png", "camera" :"icons/camera.ico","history": "icons/history.ico" }

class Ui_MainWindow(object):
 
    def UstMenuler(self, MainWindow):
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menuGorunum = QtWidgets.QMenu(self.menubar) 
        self.menuAracCubugu = QtWidgets.QMenu(self.menuGorunum) 
        self.menuAyarlar = QtWidgets.QMenu(self.menubar) 
        self.menuHakkinda = QtWidgets.QMenu(self.menubar) 
        self.menuYakala = QtWidgets.QMenu(self.menubar) 
        self.menuGecmis = QtWidgets.QMenu(self.menubar) 
        _translate = QtCore.QCoreApplication.translate

        self.actionMesajlar_Penceresi = QtWidgets.QAction(MainWindow)
        self.actionMesajlar_Penceresi.setCheckable(True)
        self.actionMesajlar_Penceresi.setChecked(True) 
        self.actionYakala = QtWidgets.QAction(MainWindow) 
        self.actionGoruntuTekrarlariniizle = QtWidgets.QAction(MainWindow) 
        self.actionYakalanan_Goruntuler = QtWidgets.QAction(MainWindow) 
        self.actionAyalar = QtWidgets.QAction(MainWindow)
        self.actionAyalar.setCheckable(True)
        self.actionAyalar.setChecked(True) 
        self.actionGecmis = QtWidgets.QAction(MainWindow)  
        self.actionMesaj_Penceresi = QtWidgets.QAction(MainWindow)
        self.actionMesaj_Penceresi.setCheckable(True)
        self.actionMesaj_Penceresi.setChecked(True) 
        self.actionAyarlar = QtWidgets.QAction(MainWindow)
        self.actionAyarlar.setCheckable(True)
        self.actionAyarlar.setChecked(True) 
        self.actionGecmis_2 = QtWidgets.QAction(MainWindow)
        self.actionGecmis_2.setCheckable(True)
        self.actionGecmis_2.setChecked(True) 
        self.menuAracCubugu.addAction(self.actionMesaj_Penceresi)
        self.menuAracCubugu.addAction(self.actionAyarlar)
        self.menuAracCubugu.addAction(self.actionGecmis_2)
        self.menuGorunum.addAction(self.menuAracCubugu.menuAction())
        self.menuGecmis.addAction(self.actionGoruntuTekrarlariniizle)
        self.menuGecmis.addAction(self.actionYakalanan_Goruntuler)
        self.menubar.addAction(self.menuAyarlar.menuAction())
        self.menubar.addAction(self.menuGorunum.menuAction())
        self.menubar.addAction(self.menuYakala.menuAction())
        self.menubar.addAction(self.menuGecmis.menuAction())
        self.menubar.addAction(self.menuHakkinda.menuAction())

        self.menuGorunum.setTitle(_translate("MainWindow", "Görünüm"))
        self.menuAracCubugu.setTitle(_translate("MainWindow", "Araç Çubuğu"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.menuHakkinda.setTitle(_translate("MainWindow", "Hakkında"))
        self.menuYakala.setTitle(_translate("MainWindow", "Yakala"))
        self.menuGecmis.setTitle(_translate("MainWindow", "Geçmiş"))
        self.actionMesajlar_Penceresi.setText(_translate("MainWindow", "Mesajlar Penceresi"))
        self.actionYakala.setText(_translate("MainWindow", "Yakala"))
        self.actionYakala.setShortcut(_translate("MainWindow", "F2"))
        self.actionGoruntuTekrarlariniizle.setText(_translate("MainWindow", "Görüntü Tekrarlarını izle"))
        self.actionYakalanan_Goruntuler.setText(_translate("MainWindow", "Yakalanan Görüntüler"))
        self.actionAyalar.setText(_translate("MainWindow", "Ayalar"))
        self.actionGecmis.setText(_translate("MainWindow", "Geçmiş"))
        self.actionMesaj_Penceresi.setText(_translate("MainWindow", "Mesaj Penceresi"))
        self.actionAyarlar.setText(_translate("MainWindow", "Ayarlar"))
        self.actionGecmis_2.setText(_translate("MainWindow", "Geçmiş"))
 
    def dock_menu_tiklamasi(self,menu):

        menu.setFixedSize(QtCore.QSize(600, 800))  
     

    def setupUi(self, MainWindow): 
        # MainWindow 
        MainWindow.resize(1920, 1080)  
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/icons/camera.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon) 
        MainWindow.setStyleSheet("background-color: rgb(238, 244, 246);")
        MainWindow.setWindowTitle( "Kamera Takip Uygulaması") 
        # Kamera Görüntüleri
        Goruntuler(MainWindow) 

        self.UstMenuler(MainWindow) 
        MainWindow.setMenuBar(self.menubar) 

        self.dockmenuler= {} 
        #TODO Ekranda kaç görüntü gösterilsin, Bağlanan Kamera Listesi 
        # scroolviewde kameralar olacak, her satırda nesne tespiti, nesne sayacı, fps isim gösterilsin mi butonları aktif deaktif edilecek   
        self.dockmenuler["Kamera_ayarlari"] = Dock_menu(MainWindow,icons["camera"],2)
        
        #TODO Hareket dökümü listesi   # loglar  
        self.dockmenuler["History"] = Dock_menu(MainWindow, icons["history"],1)
        self.dockmenuler["Ayarlar"] = Dock_menu(MainWindow, icons["setting"],1)
        
        ayarlar_icerik = self.dockmenuler["Ayarlar"].dock_menu_icerik
        Options(ayarlar_icerik)
         
        kameralar_icerik = self.dockmenuler["Kamera_ayarlari"].dock_menu_icerik
        Kameralar(kameralar_icerik) 
     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
