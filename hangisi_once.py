
import os, sys, os.path
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog, QPushButton, QLineEdit, QComboBox, QLabel, QRadioButton
from PyQt5.QtWidgets import QAction , QApplication, QMainWindow, QGridLayout, QWidget, QSizePolicy
from PyQt5.QtCore import QCoreApplication, Qt

from datetime import date

#from PyQt4 import *

class hasta():
    def __init__(self):
        self.text = ''
        self.yas = 0;
        self.id  = 0;
        self.tarihler = []
        self.cinsiyet = ''
    
    def extract_id(self,text):
        # takes a string and reads until the first underscore "_" character, then converts it to number
        pass
    
    def kayit_ekle(self,text):
        groups = text.split('_')
        self.id = int( groups[0] )
        self.yas = int( groups[1] )
        gun = int( groups[2][0:2] )
        ay  = int( groups[2][2:4] )
        yil = int( groups[2][4:6] )       
        self.cinsiyet = int( groups[3] )
        
        self.tarihler.append[yil, ay, gun]
        
    def compute_days(self,year1, month1, day1, year2, month2, day2):        
        d0 = date(year1, month1, day1)
        d1 = date(year2,month2, day2)
        if d0 > d1:
            delta = d0 - d1            
        elif d1 > d0:
            delta = d1 - d0
        else:
            delta = 0

        return delta.days
        
        
class mainWindow(QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()

        width  = QApplication.desktop().screen().rect().width()-300
        height = QApplication.desktop().screen().rect().height()-300
        self.setGeometry(50, 50, width, height)                
        
        self.setWindowTitle('Hangisi önce?')                                                           
        
        
        self.pic1 = QLabel()
        self.pic1.setScaledContents(True) # MUST HAVE!!        
        
#        self.pic1.setGeometry(30, 20, 900, 800)
        #use full ABSOLUTE path to the image, not relative
        imageName1 = "/home/yoldas/Pictures/rengarenk_agac_cropped.jpg"
        self.image1 = QPixmap(imageName1)        

        self.pic1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pic1.setMinimumSize(100, 100)        
        self.pic1.setPixmap(self.image1.scaledToWidth(self.pic1.width()))

        self.radio1 = QRadioButton('Goruntu 1',self)
        self.radio1.clicked.connect(self.mark1st)
#        self.radio1.move(450,850)         
        
        self.pic2 = QLabel()
        self.pic2.setScaledContents(True)  # MUST HAVE!!        
        
#        self.pic2.setGeometry(970, 20, 900, 800)
        #use full ABSOLUTE path to the image, not relative
        imageName2 = "/home/yoldas/Pictures/rengarenk_agac_cropped.jpg"
        self.image2 = QPixmap(imageName2)
#        self.pic2.setPixmap(self.image2)
        self.pic2.setPixmap(self.image2.scaledToWidth(self.pic2.width()))

        self.pic2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pic2.setMinimumSize(100, 100)
        
        self.radio2 = QRadioButton('Goruntu 2',self)
#        self.radio2.move(1400,850)
        self.radio2.clicked.connect(self.mark2nd)

        
        grid = QGridLayout()   
#        grid.setSpacing(10) 
#        grid.setRowStretch(0,100)        

        grid.addWidget(self.pic1,0,0,Qt.AlignCenter)        
        grid.addWidget(self.radio1,1,0,Qt.AlignCenter)
        grid.addWidget(self.pic2,0,1,Qt.AlignCenter)
        grid.addWidget(self.radio2,1,1,Qt.AlignCenter)

        self.setLayout(grid)      
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())

    def home(self):
        self.show()
        
    def mark1st(self):
        pass
#        print('Birinci secildi') 
    
    def mark2nd(self):
        pass
#        print('İkinci secildi') 
        
    def resizeEvent(self,event):
        width  = QApplication.desktop().screen().rect().width()-30
        height = QApplication.desktop().screen().rect().height()-30
        
        self.pic1.setGeometry(10, 10, width/2, height/2)
        self.pic2.setGeometry(width/2+20, height/2+20, width/2, height/2 )
        
        self.image1.scaledToHeight(self.pic1.height())
        self.image2.scaledToHeight(self.pic2.height())
        
        w1 = self.pic1.width();
        h1 = self.pic1.height();
        w2 = self.pic2.width();
        h2 = self.pic2.height();
        self.pic1.setPixmap(self.image1.scaled(w1, h1, Qt.KeepAspectRatio, Qt.SmoothTransformation ))
        self.pic2.setPixmap(self.image2.scaled(w2, h2, Qt.KeepAspectRatio, Qt.SmoothTransformation ))
        
#        print('scaled')
        

        return super(mainWindow, self).resizeEvent(event)


class loginWindow(QMainWindow):
    def __init__(self):
        super(loginWindow, self).__init__()
        self.setGeometry(500, 500, 400, 500)
        self.setWindowTitle('Kullanıcı seçin')
#        self.setWindowIcon(QIcon('pic.png'))

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Uygulamayı kapat')
        exitAction.triggered.connect(self.close_application)


        self.btnEkle = QPushButton('Ekle', self)
        self.btnEkle.move(150, 225)
        self.btnEkle.clicked.connect(self.ekle)
        self.btnEkle.setEnabled(False)
        
        self.btnKlasor = QPushButton('Klasör Seç', self)
        self.btnKlasor.move(150, 325)
        self.btnKlasor.clicked.connect(self.klasor_sec)
        self.btnKlasor.setEnabled(False)
        
        
        self.statusBar()
        
        self.txtKullanici = QLabel('Yeni kullanıcı ismi', self)
        self.txtKullanici.setGeometry(150,150,200,30) 
        self.txtKullanici.setEnabled(False)
        
        self.textEdit = QLineEdit(self)
        self.textEdit.setGeometry(100,185,200,30)   
        self.textEdit.setAlignment(Qt.AlignCenter)
        self.textEdit.setEnabled(False)

        exitAction = QAction(QIcon('pic.png'), 'flee the scene', self)
        exitAction.triggered.connect(self.close_application)

        self.radioVarolan = QRadioButton('Varolan kullanıcı',self)
#        self.radio2.move(1400,850)
        self.radioVarolan.clicked.connect(self.markVarolan)
        self.radioVarolan.setGeometry(50,30,200,30)
        self.radioVarolan.setChecked(True)

        self.radioYeni = QRadioButton('Yeni kullanıcı',self)
#        self.radio2.move(1400,850)
        self.radioYeni.clicked.connect(self.markYeni)
        self.radioYeni.setGeometry(50,120,200,30)        
        
        self.username = 'None'
        
        self.comboBox = QComboBox(self)
        self.comboBox.addItem('Seciniz')

        users_file = open(os.getcwd()+"/users.txt","r")        

        for line in users_file.readlines():
            self.comboBox.addItem(line)
        
        users_file.close()
        

        self.comboBox.setGeometry(100,65,200,30)         
        self.comboBox.activated[str].connect(self.select_user)
        
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        
        self.home()
        
        self.mainGui = mainWindow()

    def editor(self):
        pass
    
    def markVarolan(self):
        self.textEdit.setEnabled(False)
        self.btnEkle.setEnabled(False)
        self.txtKullanici.setEnabled(False)
        self.comboBox.setEnabled(True)
        self.radioYeni.setChecked(False)
        
    def markYeni(self):
        self.textEdit.setEnabled(True)
        self.btnEkle.setEnabled(True)
        self.txtKullanici.setEnabled(True)
        self.comboBox.setEnabled(False)
        self.radioVarolan.setChecked(False)        

    def klasor_sec(self):
        # need to make name an tupple otherwise i had an error and app crashed
#        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
        path = QFileDialog.getExistingDirectory(self, "Klasör Seç",'',   QFileDialog.ShowDirsOnly )
        if path !='':
            print(path +" :")  # for debugging
            files = sorted(os.listdir( path ))

            # This would print all the files and directories
            for file in files:
                extension = file[-4:len(file)]
                if  extension == '.jpg' or extension == '.JPG' or extension =='.bmp' or extension =='.BMP' or extension =='.png' or extension == 'PNG':
                    print(file)
            
            self.hide()        
#            self.mainGui.show()
            self.mainGui.showMaximized()  

            user_file = path +"/" + self.username+'.txt'
            if os.path.exists(user_file):
                print(user_file +' exists.')
                file = open(user_file, 'r')
                text = file.read()
                print(text)
                
            else:
                print(user_file +' did not exist. Newly created.\n')
                file = open(user_file, 'w')
                text = self.username + ' in tahminleri'
                file.write(text)
                file.close
        
#            file = open(name, 'r')
#            print('na het inlezen gelukt') # for debugging
        

#            with file:
#               text = file.read()
#               self.textEdit.setText(text)

    def file_save(self):
        name, _ = QFileDialog.getSaveFileName(self,'Save File', options=QFileDialog.DontUseNativeDialog)
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()


    def home(self):       

#        checkBox = QCheckBox('Enlarge window', self)
#        # checkBox.toggle()  # if you want to be checked in in the begin
#        checkBox.move(0, 50)
#        checkBox.stateChanged.connect(self.enlarge_window)

#        self.btnEkle = QPushButton('Klasor Sec', self)
#        self.btnEkle.move(1200, 950)
#        self.btnEkle.clicked.connect(self.next_pair)
#        self.btnEkle.resize(btnEkle.sizeHint())
#        self.btnEkle.move(0, 100)


        self.show()        

    def ekle(self):
        kullanici_adi = self.textEdit.text()
        self.comboBox.addItem(kullanici_adi)
        
        self.username = kullanici_adi
        self.comboBox.setCurrentIndex(self.comboBox.count()-1)    

        users_file = open(os.getcwd()+"/users.txt","a")
        users_file.write(self.username +'\n')
        users_file.close()

        self.textEdit.clear()
        self.textEdit.setEnabled(False)
        self.comboBox.setEnabled(True)
        self.radioVarolan.setChecked(True)
        self.radioYeni.setChecked(False)
        self.btnEkle.setEnabled(False)
        
        self.select_user(self.username)
        

    
    def select_user(self,text):        
        
        if text == 'Seciniz':
            self.btnKlasor.setEnabled(False)            
        else:
            self.btnKlasor.setEnabled(True)
            self.username = text
        
        

    def close_application(self):
        sys.exit()        



if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        loginGui = loginWindow()
        sys.exit(app.exec_())

run()



