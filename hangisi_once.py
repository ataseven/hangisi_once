
import os, sys, os.path
import itertools, random

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton, QLineEdit, QComboBox, QLabel, QRadioButton
from PyQt5.QtWidgets import QAction , QApplication, QMainWindow, QGridLayout, QWidget, QSizePolicy
from PyQt5.QtCore import QCoreApplication, Qt

from datetime import date

#from PyQt4 import *

class hasta():
    def __init__(self):
        self.text = ''
        self.yas = -1;
        self.id  = -1;
        self.cinsiyet = ''
        self.tarihler = []
        self.dosya_isimleri = []
    
    def extract_id(self,text):
        # takes a string and reads until the first underscore "_" character, then converts it to number
        pass
    
    # hem hasta bilgisini gunceller, hem de yeni kayit tarihi ekler. Bu demektir ki,
    # hasta id'si ayni olan imajlar içinde, alfabetik sırada son sırada olan dosyada yazan hasta bilgisi kullanılır.
    def goruntu_ekle(self,text):
        groups = text.split('_')
#        print(groups)
        self.id = int( groups[0] )
        self.yas = int( groups[1] )
        gun = int( groups[2][0:2] )
        ay  = int( groups[2][2:4] )
        yil = int( groups[2][4:8] )       
        self.cinsiyet = groups[3].split('.')[0]
        
        self.tarihler.append([yil, ay, gun])
        self.dosya_isimleri.append(text)
        
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
        
    def getFileNames(self):
        return self.dosya_isimleri
        
class mainWindow(QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()

        width  = QApplication.desktop().screen().rect().width()-300
        height = QApplication.desktop().screen().rect().height()-300
        self.setGeometry(50, 50, width, height)                
        self.setMinimumSize(400,400)
        self.setWindowTitle('Hangisi önce?')                                                           
        
        
        self.pic1 = QLabel()
        self.pic1.setScaledContents(True) # MUST HAVE!!        
        
#        self.pic1.setGeometry(30, 20, 900, 800)
        #use full ABSOLUTE path to the image, not relative
#        imageName1 = "/home/yoldas/Pictures/rengarenk_agac_cropped.jpg"
        self.image1 = QPixmap(100,100)        

        self.pic1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pic1.setMinimumSize(100, 100)        
#        self.pic1.setPixmap(self.image1.scaledToWidth(self.pic1.width()))

        self.radio1 = QRadioButton('Goruntu 1',self)
        self.radio1.clicked.connect(self.mark1st)
#        self.radio1.move(450,850)         
        
        self.pic2 = QLabel()
        self.pic2.setScaledContents(True)  # MUST HAVE!!        
        
#        self.pic2.setGeometry(970, 20, 900, 800)
        #use full ABSOLUTE path to the image, not relative
#        imageName2 = "/home/yoldas/Pictures/rengarenk_agac_cropped.jpg"
        self.image2 = QPixmap(100,100)
#        self.pic2.setPixmap(self.image2)
#        self.pic2.setPixmap(self.image2.scaledToWidth(self.pic2.width()))

        self.pic2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pic2.setMinimumSize(100, 100)
        
        self.radio2 = QRadioButton('Goruntu 2',self)
#        self.radio2.move(1400,850)
        self.radio2.clicked.connect(self.mark2nd)

        self.infoBox = QMessageBox() ##Message Box that doesn't run

        self.infoBox.setIcon(QMessageBox.Information)
#        self.infoBox.setText("Bu klasör tamam")
        self.infoBox.setText("Bu klasördeki bütün verileri oyladınız.")
#        self.infoBox.setInformativeText("Bu klasordeki bütün verileri oyladınız.")        
        self.infoBox.setWindowTitle("Tamamlandı")
#        self.infoBox.setDetailedText("Daha ne detay vereyim, anlattım işte...")
        self.infoBox.setStandardButtons(QMessageBox.Ok)        
        self.infoBox.setEscapeButton(QMessageBox.Close)   


        self.raporBox = QMessageBox()        
        self.raporBox.setIcon(QMessageBox.Information)
#        self.infoBox.setText("Bu klasör tamam")
        self.raporBox.setText("Rapor hazırlandı ve Sonuclar.txt dosyasına yazıldı.")
#        self.infoBox.setInformativeText("Bu klasordeki bütün verileri oyladınız.")        
        self.raporBox.setWindowTitle("Raporlandı")
#        self.infoBox.setDetailedText("Daha ne detay vereyim, anlattım işte...")
        self.raporBox.setStandardButtons(QMessageBox.Ok)        
        self.raporBox.setEscapeButton(QMessageBox.Close)

        self.errBox = QMessageBox()        
        self.errBox.setIcon(QMessageBox.Information)
#        self.infoBox.setText("Bu klasör tamam")
        self.errBox.setText("Kullanıcıların bilgisine ulaşılamadı. users.txt dosyası bulunamadı.")
#        self.infoBox.setInformativeText("Bu klasordeki bütün verileri oyladınız.")        
        self.errBox.setWindowTitle("Raporlama hatası")
#        self.infoBox.setDetailedText("Daha ne detay vereyim, anlattım işte...")
        self.errBox.setStandardButtons(QMessageBox.Ok)
        self.errBox.setEscapeButton(QMessageBox.Close)
        
        
        
        grid = QGridLayout()   
#        grid.setSpacing(10) 
        grid.setRowStretch(0,100)
        grid.setRowStretch(1,1)

#        grid.addWidget(self.button_iptal,0,1,Qt.AlignCenter)        
        grid.addWidget(self.pic1,0,0,Qt.AlignCenter)
        grid.addWidget(self.radio1,1,0,Qt.AlignCenter)
        grid.addWidget(self.pic2,0,1,Qt.AlignCenter)
        grid.addWidget(self.radio2,1,1,Qt.AlignCenter)

        self.setLayout(grid)      

        self.button_iptal1 = QPushButton('1. görüntüyü sil', self)        
        self.button_iptal1.clicked.connect(self.goruntu1_iptal)
        self.button_iptal1.setEnabled(True)
        self.button_iptal1.setGeometry(int(width/4-45),int(20),90,30)
        
        self.button_iptal2 = QPushButton('2. görüntüyü sil', self)        
        self.button_iptal2.clicked.connect(self.goruntu2_iptal)
        self.button_iptal2.setEnabled(True)
        self.button_iptal2.setGeometry(int(width*3/4-45),int(20),90,30)        

        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())


        
        self.hastalar = []
        self.calisma_klasoru = '';
        self.username = ''
        self.current_pair_index = -1
        self.ikililer = []
        self.ikililer_iptal = []
        self.ikililer_iptal_index = -1  # an index that points to the ikililer_iptal array
        self.user_file =''
        
        self.left_img_filename =''
        self.right_img_filename =''        

    def home(self):
        self.show()
        
    def goruntu1_iptal(self):        
        
        if os.path.exists(self.ikili_iptal_filename):
            ikili_iptal_file = open(self.ikili_iptal_filename, 'a')            
        else:
            ikili_iptal_file = open(self.ikili_iptal_filename, 'w')
            
        canceled_filename  = self.ikililer[self.current_pair_index].split(' ')[0]
        print('canceled: ' + canceled_filename)
        hasta_id = int(self.right_img_filename.split('_')[0])

        print('hasta id: ' + str(hasta_id))
        ayni_hasta = True
        pair_check_idx = self.current_pair_index
        
        while ayni_hasta and pair_check_idx < len(self.ikililer):
            
            left_imgname = self.ikililer[pair_check_idx].split(' ')[0]
            right_imgname = self.ikililer[pair_check_idx].split(' ')[1]
            print('left: ' + left_imgname + ' right: ' + right_imgname)
            checked_hasta_id = int(left_imgname.split('_')[0])

            print('checked pair:' + str(pair_check_idx) + ' checked id:' + str(checked_hasta_id))
            
            if checked_hasta_id == hasta_id:
                print('hastanin id tuttu')
                if left_imgname == canceled_filename or right_imgname == canceled_filename:
                    print('ikililerden birisi iptal edilenlerden, ikili iptal ediliyor')
                    
                    ikili_iptal_file.write(str(pair_check_idx) + '\n')
                    self.ikililer_iptal.append(pair_check_idx)
                    self.ikililer_iptal = sorted(list(set(self.ikililer_iptal))) # olmaz ama, olası duplikelerin önlemi olarak böyle bi şey yaptım.                
            else:
                ayni_hasta = False

            pair_check_idx = pair_check_idx + 1
            
        ikili_iptal_file.close()

        self.ikililer_iptal_index = self.ikililer_iptal_index + 1
        if self.ikililer_iptal_index < len(self.ikililer_iptal)-1:
            self.ikililer_iptal_index = self.ikililer_iptal_index + 1
            
        self.mark_sil(-1)
        self.set_calisma_klasoru(self.calisma_klasoru)
        self.set_user(self.username)
        
        if self.current_pair_index < len(self.ikililer)-1:
            self.show_next_pair()
        else:            
            self.radio1.setEnabled(False)
            self.radio2.setEnabled(False)
            self.button_iptal1.setEnabled(False)
            self.button_iptal2.setEnabled(False)
            self.infoBox.exec_()
            
            
    def goruntu2_iptal(self):
        
        if os.path.exists(self.ikili_iptal_filename):
            ikili_iptal_file = open(self.ikili_iptal_filename, 'a')            
        else:
            ikili_iptal_file = open(self.ikili_iptal_filename, 'w')
            
        canceled_filename  = self.ikililer[self.current_pair_index].split(' ')[1]
        print('canceled: ' + canceled_filename)
        hasta_id = int(self.right_img_filename.split('_')[0])

        print('hasta id: ' + str(hasta_id))
        ayni_hasta = True
        pair_check_idx = self.current_pair_index
        
        while ayni_hasta and pair_check_idx < len(self.ikililer):
            
            left_imgname = self.ikililer[pair_check_idx].split(' ')[0]
            right_imgname = self.ikililer[pair_check_idx].split(' ')[1]
            print('left: ' + left_imgname + ' right: ' + right_imgname)
            checked_hasta_id = int(left_imgname.split('_')[0])

            print('checked pair:' + str(pair_check_idx) + ' checked id:' + str(checked_hasta_id))
            
            if checked_hasta_id == hasta_id:
                print('hastanin id tuttu')
                if left_imgname == canceled_filename or right_imgname == canceled_filename:
                    print('ikililerden birisi iptal edilenlerden, ikili iptal ediliyor\n')
                    
                    ikili_iptal_file.write(str(pair_check_idx) + '\n')
                    self.ikililer_iptal.append(pair_check_idx)
                    self.ikililer_iptal = sorted(list(set(self.ikililer_iptal))) # olası duplikelerin önlemi olarak böyle bi şey yaptım.
            else:
                ayni_hasta = False

            pair_check_idx = pair_check_idx + 1
            
        ikili_iptal_file.close()

        self.ikililer_iptal_index = self.ikililer_iptal_index + 1
        if self.ikililer_iptal_index < len(self.ikililer_iptal)-1:
            self.ikililer_iptal_index = self.ikililer_iptal_index + 1

        self.mark_sil(-2)
        self.set_calisma_klasoru(self.calisma_klasoru)
        self.set_user(self.username)
        
        if self.current_pair_index < len(self.ikililer)-1:
            self.show_next_pair()
        else:            
            self.radio1.setEnabled(False)
            self.radio2.setEnabled(False)
            self.button_iptal1.setEnabled(False)
            self.button_iptal2.setEnabled(False)
            self.infoBox.exec_()        

        
        
#    Kullanıcı "soldaki görüntü önce" derse yapılacaklar
    def mark1st(self):
        file = open(self.user_file, 'a')
        tmp_hasta = hasta()
        
        tmp_hasta.goruntu_ekle(self.left_img_filename)
        tmp_hasta.goruntu_ekle(self.right_img_filename)
        
#        soldaki görüntünün tarihi
        yil1 = tmp_hasta.tarihler[0][0]
        ay1 = tmp_hasta.tarihler[0][1]
        gun1 = tmp_hasta.tarihler[0][2]
        
        yil2 = tmp_hasta.tarihler[1][0]
        ay2 = tmp_hasta.tarihler[1][1]
        gun2 = tmp_hasta.tarihler[1][2]
        
        d0 = date(yil1, ay1, gun1)
#        print(d0)
#       sağdaki görüntünün tarihi
        d1 = date(yil2, ay2, gun2)
#        print(d1)
        
        if d0 > d1:  # doğru cevap : "sağdaki önce" ama kullanıcı "soldaki önce" demiş ki şu an içinde bulunduğumuz fonksiyona girmişiz
            delta = d1 - d0
            tahmin = 0  # Kullanıcı hatalı tahminde bulundu
        elif d1 > d0:  # doğru cevap : "soldaki önce". Kullanıcı da "soldaki önce" demiş ki şu an içinde bulunduğumuz fonksiyona girmişiz
            delta = d1 - d0
            tahmin = 1  # Kullanıcı doğru tahminde bulundu
        else:
            delta = d1 - d0
            tahmin = 1 # Aynı günde iki farklı görüntü varsa kullanıcı doğru bilmiş sayılıyor.

        zaman_farki = delta.days
        
        file.write(str(tmp_hasta.id) + ',' + str(tmp_hasta.yas) + ',' + tmp_hasta.cinsiyet + ',' + str(zaman_farki) + ',' + str(tahmin) + '\n' )
        file.close()
        
        if self.current_pair_index < len(self.ikililer)-1:
            self.show_next_pair()
        else:            
            self.radio1.setEnabled(False)
            self.radio2.setEnabled(False)
            self.button_iptal1.setEnabled(False)
            self.button_iptal2.setEnabled(False)
            self.infoBox.exec_()
        
        self.radio1.setChecked(False)
    
#    Kullanıcı "sağdaki görüntü önce" derse yapılacaklar
    def mark2nd(self):
        file = open(self.user_file, 'a')
        tmp_hasta = hasta()
        
        tmp_hasta.goruntu_ekle(self.left_img_filename)
        tmp_hasta.goruntu_ekle(self.right_img_filename)
        
#        soldaki görüntünün tarihi
        yil1 = tmp_hasta.tarihler[0][0]
        ay1 = tmp_hasta.tarihler[0][1]
        gun1 = tmp_hasta.tarihler[0][2]
        
        yil2 = tmp_hasta.tarihler[1][0]
        ay2 = tmp_hasta.tarihler[1][1]
        gun2 = tmp_hasta.tarihler[1][2]
        
        d0 = date(yil1, ay1, gun1)
#        print(d0)
        
#       sağdaki görüntünün tarihi
        d1 = date(yil2, ay2, gun2)
#        print(d1)

#        print(' \n')
        
        if d0 > d1:  # doğru cevap : "sağdaki önce". Kullanıcı da "sağdaki önce" demiş ki şu an içinde bulunduğumuz fonksiyona girmişiz
            delta = d1 - d0
            tahmin = 1  # Kullanıcı doğru tahminde bulundu
        elif d1 > d0:  # doğru cevap : "sağdaki önce" ama kullanıcı "soldaki önce" demiş ki şu an içinde bulunduğumuz fonksiyona girmişiz
            delta = d1 - d0
            tahmin = 0  # Kullanıcı yanlış tahminde bulundu
        else:
            delta = d1 - d0
            tahmin = 1 # Aynı günde iki farklı görüntü varsa kullanıcı doğru bilmiş sayılıyor.

        zaman_farki = delta.days
        
        
        file.write(str(tmp_hasta.id) + ',' + str(tmp_hasta.yas) + ',' + tmp_hasta.cinsiyet + ',' + str(zaman_farki) + ',' + str(tahmin) + '\n' )
        
        file.close()
        
        if self.current_pair_index < len(self.ikililer)-1:
            self.show_next_pair()
        else:            
            self.radio1.setEnabled(False)
            self.radio2.setEnabled(False)
            self.button_iptal1.setEnabled(False)
            self.button_iptal2.setEnabled(False)
            self.infoBox.exec_()
            
        self.radio2.setChecked(False)
#        print('İkinci secildi') 

#    Kullanıcı "soldaki görüntü önce" derse yapılacaklar
    def mark_sil(self,silinen_idx):
        file = open(self.user_file, 'a')
        tmp_hasta = hasta()
        
        tmp_hasta.goruntu_ekle(self.left_img_filename)
        tmp_hasta.goruntu_ekle(self.right_img_filename)
        
#        soldaki görüntünün tarihi
        yil1 = tmp_hasta.tarihler[0][0]
        ay1 = tmp_hasta.tarihler[0][1]
        gun1 = tmp_hasta.tarihler[0][2]
        
        yil2 = tmp_hasta.tarihler[1][0]
        ay2 = tmp_hasta.tarihler[1][1]
        gun2 = tmp_hasta.tarihler[1][2]
        
        d0 = date(yil1, ay1, gun1)
#        print(d0)
#       sağdaki görüntünün tarihi
        d1 = date(yil2, ay2, gun2)
#        print(d1)
        
        if d0 > d1:  # doğru cevap : "sağdaki önce" ama kullanıcı "soldaki önce" demiş ki şu an içinde bulunduğumuz fonksiyona girmişiz
            delta = d1 - d0            
        elif d1 > d0:  # doğru cevap : "soldaki önce". Kullanıcı da "soldaki önce" demiş ki şu an içinde bulunduğumuz fonksiyona girmişiz
            delta = d1 - d0
        else:
            delta = d1 - d0

        tahmin = silinen_idx

        zaman_farki = delta.days
        
        file.write(str(tmp_hasta.id) + ',' + str(tmp_hasta.yas) + ',' + tmp_hasta.cinsiyet + ',' + str(zaman_farki) + ',' + str(tahmin) + '\n' )
        file.close()
        
        
    def set_calisma_klasoru(self, text):
        self.calisma_klasoru = text;
        current_hasta_id = -1
        self.ikili_filename = self.calisma_klasoru +'/.ikililer.txt'
        if self.calisma_klasoru !='':
#            print(self.calisma_klasoru +" :")  # for debugging
            
            if os.path.exists(self.ikili_filename):
                pass
            
            else:
                files = sorted(os.listdir( self.calisma_klasoru ))
                ikili_file = open(self.calisma_klasoru +'/.ikililer.txt', 'w')

                # This would print all the files and directories
                for filename in files:
                    extension = filename[-4:len(filename)]
                    
                    if  extension == '.jpg' or extension == '.JPG' or extension =='.bmp' or extension =='.BMP' or extension =='.png' or extension == 'PNG':
                        groups = filename.split('_')
                        ID = int(groups[0])
                        
                        # eğer bu hastanın daha önce bir dosyası işlendiyse, o hasta ile ilgili yeni tarih ve dosya ismi ekle
                        if current_hasta_id == ID and current_hasta_id >= 0: 
                            self.hastalar[-1].goruntu_ekle(filename)
                        
                        else: 

                            # bir önceki hastanın ikililerini belirle ve ikililer.txt dosyasına yaz.        
                            if current_hasta_id >= 0:  # ilk hastadan öncesi yok. ilk hastaya özel muamele yapılıyo.
                                for pair in itertools.combinations( self.hastalar[-1].getFileNames() , 2):
                                    idx  = random.randint(0,1)
                                    ikili_file.write( pair[idx] + ' ' + pair[1-idx] + '\n' )
                            
                            # yeni hasta bilgilerini oluşturmaya başla
                            yeni_hasta = hasta()
                            yeni_hasta.goruntu_ekle(filename)
                            self.hastalar.append(yeni_hasta)
                            current_hasta_id = ID
                            
                        if filename == files[-1]:   # son hastadan sonra hasta gelmediği için bunun da handle edilmesi lazım.
                            for pair in itertools.combinations( yeni_hasta.getFileNames() , 2):
                                idx  = random.randint(0,1)
                                ikili_file.write( pair[idx] + ' ' + pair[1-idx] + '\n' )
                            
                
                ikili_file.close()
                
            ikili_file = open(self.ikili_filename , 'r')
            file_content = ikili_file.read()
            ikili_file.close()
            
            lines = file_content.split('\n')    # dosya satırlarını bir array haline getir.
            self.ikililer = lines[:-1]          # yazma şeklim yüzünden fazladan bir satır geliyor, onu çıkar
                            
            self.ikili_iptal_filename = self.calisma_klasoru +'/.silinen_ikililer.txt'
        
            if os.path.exists(self.ikili_iptal_filename):
                ikili_iptal_file = open(self.ikili_iptal_filename, 'r')
                file_content = ikili_iptal_file.read()
                ikili_iptal_file.close()
                
                tmp = file_content.split('\n')
                tmp = tmp[:-1]
                self.ikililer_iptal = [int(i) for i in tmp]
                    
                tmp = sorted(list(set(self.ikililer_iptal))) # remove any duplicates
                
                # there are duplicated entries of the silinen_ikililer.txt file, remove them and rewrite the file
                if len(tmp) != self.ikililer_iptal:
                    ikili_iptal_file = open(self.ikili_iptal_filename, 'w')

                    for i in tmp:                    
                        ikili_iptal_file.write(str(i)+'\n')
                    ikili_iptal_file.close()
                    
                    self.ikililer_iptal = tmp
                
#            self.left_img_filename  = self.ikililer[self.current_pair_index].split(' ')[0]
#            self.right_img_filename = self.ikililer[self.current_pair_index].split(' ')[1]
#                        
#            
#            self.image1 = QPixmap(self.calisma_klasoru + '/' +self.left_img_filename)
##           self.pic1.setPixmap(self.image1)
#            self.pic1.setPixmap(self.image1.scaledToWidth(self.pic1.width()))
#
#            self.image2 = QPixmap(self.calisma_klasoru + '/' +self.right_img_filename)
##           self.pic2.setPixmap(self.image2)
#            self.pic2.setPixmap(self.image2.scaledToWidth(self.pic2.width()))
#            
            
    def set_user(self, username):
        self.username = username;

        self.user_file = self.calisma_klasoru + "/." + self.username + '.txt'        
                   
        
        if os.path.exists(self.user_file):
#            print(self.user_file +' exists.')
            file = open(self.user_file, 'r')
            file_content = file.read()
            file.close()
            
            lines = file_content.split('\n')   # dosya satırlarını bir array haline getir.
            lines = lines[:-1]  # yazma şeklim ve ilk satırdaki açıklama yüzünden fazladan iki satır geliyor, onu çıkar
            num_prev_entries = len(lines)
            self.current_pair_index = max(-1,num_prev_entries-2) # normalde num_prev_entries-1 olması lazım, ama bir sonraki ikilinin indeksini açılışta ayarlamayı tercih ettim.
            
#            text = file.read()
#            print(text)
            
        else:
#            print(self.user_file +' did not exist. Newly created.\n')
            file = open(self.user_file, 'w')
            text = self.username + ' in tahminleri. Sıralama: ID, yaş, cinsiyet, zaman farkı(gün), tahmin (1:doğru 0:yanlış)\n'
                        
            file.write(text)
            file.close                        
            
        # eğer kullanıcı tarafından daha önce işaretleme yapılmış ise, iptal edilenlerin pointer'ını kullanıcının ikili indeksinin olduğu yere getir.
        # ilk gösterilecek ikili için current_pair_index 1 artırılacak, dolayısıyla kıyaslamanın < değil <= şeklinde olması gerekiyor.
        if len(self.ikililer_iptal) > 0:
            self.ikililer_iptal_index = 0
#            print(self.ikililer_iptal)
#            print(self.ikililer_iptal_index)
#            print(self.current_pair_index)
            while self.ikililer_iptal[self.ikililer_iptal_index] <= self.current_pair_index:
                self.ikililer_iptal_index = min(len(self.ikililer_iptal)-1, self.ikililer_iptal_index + 1)
                if self.ikililer_iptal_index == len(self.ikililer_iptal)-1:
                    break
            
    def show_next_pair(self):
        self.current_pair_index = self.current_pair_index + 1
        
        if self.current_pair_index < len(self.ikililer):
            # Initialize filenames to avoid empty img filenames in case we come across a pair that is canceled by another user
            self.left_img_filename  = self.ikililer[self.current_pair_index].split(' ')[0]
            self.right_img_filename = self.ikililer[self.current_pair_index].split(' ')[1]
        else:
            self.radio1.setEnabled(False)
            self.radio2.setEnabled(False)
            self.button_iptal1.setEnabled(False)
            self.button_iptal2.setEnabled(False)
            self.infoBox.exec_()
            return
        
#        print('\npair idx:' + str(self.current_pair_index) + ' iptal idx:' + str(self.ikililer_iptal_index) )
#        print('len iptal:' + str(len(self.ikililer_iptal)))
#        if len(self.ikililer_iptal) > 0:
#            print('iptal:'+ str(self.ikililer_iptal[self.ikililer_iptal_index]))        
        
        if len(self.ikililer_iptal) > 0:
            while  self.ikililer_iptal[self.ikililer_iptal_index] == self.current_pair_index :
#                print(self.ikililer_iptal[self.ikililer_iptal_index])
#                print(self.current_pair_index)
                self.mark_sil(-3)
                if self.ikililer_iptal_index < len(self.ikililer_iptal)-1:  # eğer iptal edilenler listesinin sonunda değilsen, listede bir ileri git
                    self.ikililer_iptal_index = self.ikililer_iptal_index + 1        
            
            
                if self.current_pair_index < len(self.ikililer)-1:   # eğer ikili listesinin sonunda değilsen, listede bir ileri git
                    self.current_pair_index = self.current_pair_index + 1
                else:                                                # ikililer listesinin sonundaysan, programı durdur
                    self.radio1.setEnabled(False)
                    self.radio2.setEnabled(False)
                    self.button_iptal1.setEnabled(False)
                    self.button_iptal2.setEnabled(False)
                    self.infoBox.exec_()
                    self.radio1.setChecked(False)                
                    self.radio2.setChecked(False)
                    return        

#        print('pair idx2:' + str(self.current_pair_index) + ' iptal idx2:' + str(self.ikililer_iptal_index) )
#        if len(self.ikililer_iptal) > 0:
#            print('iptal2:'+ str(self.ikililer_iptal[self.ikililer_iptal_index])+'\n\n')        
        
        self.left_img_filename  = self.ikililer[self.current_pair_index].split(' ')[0]
        self.right_img_filename = self.ikililer[self.current_pair_index].split(' ')[1]
                        
            
        self.image1 = QPixmap(self.calisma_klasoru + '/' + self.left_img_filename)
#       self.pic1.setPixmap(self.image1)
        self.pic1.setPixmap(self.image1.scaled(int(self.width()*0.45), int(self.height()*0.9), Qt.KeepAspectRatio))

        self.image2 = QPixmap(self.calisma_klasoru + '/' + self.right_img_filename)
#       self.pic2.setPixmap(self.image2)
        self.pic2.setPixmap(self.image2.scaled(int(self.width()*0.45), int(self.height()*0.9), Qt.KeepAspectRatio))
        
        self.radio1.setChecked(False)
        self.radio2.setChecked(False)
        
    def resizeEvent(self,event):
#        width  = QApplication.desktop().screen().rect().width()-30
#        height = QApplication.desktop().screen().rect().height()-30
        
#        self.pic1.setGeometry(10, 10, width/2, height/2)
#        self.pic2.setGeometry(width/2+20, height/2+20, width/2, height/2 )
#        
#        self.image1.scaledToHeight(self.pic1.height())
#        self.image2.scaledToHeight(self.pic2.height())
        
        w1 = int(self.width()*0.45);
        h1 = int(self.height()*0.9);
        w2 = int(self.width()*0.45);
        h2 = int(self.height()*0.9);
        self.pic1.setPixmap(self.image1.scaled(w1, h1, Qt.KeepAspectRatio, Qt.SmoothTransformation ))
        self.pic2.setPixmap(self.image2.scaled(w2, h2, Qt.KeepAspectRatio, Qt.SmoothTransformation ))
        
#        print('scaled')
        
        self.button_iptal1.setGeometry(int(self.width()/4-45),int(20),120,30)
        self.button_iptal2.setGeometry(int(self.width()*3/4-45),int(20),120,30)
        
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
        
        self.btnRapor = QPushButton('Raporla', self)
        self.btnRapor.move(150, 425)
        self.btnRapor.clicked.connect(self.raporla)
        self.btnRapor.setEnabled(True)
        
        self.statusBar()
        
        self.txtKullanici = QLabel('Yeni kullanıcı ismi', self)
        self.txtKullanici.setGeometry(150,150,200,30) 
        self.txtKullanici.setEnabled(False)
        
        self.textEdit = QLineEdit(self)
        self.textEdit.setGeometry(100,185,200,30)   
        self.textEdit.setAlignment(Qt.AlignCenter)
        self.textEdit.setEnabled(False)

#        exitAction = QAction(QIcon('pic.png'), 'flee the scene', self)
#        exitAction.triggered.connect(self.close_application)

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
        # bunun altındaki üç satır sırf isimler ortada çıksın diye.
        self.comboBox.setEditable(True)
        self.comboBox.lineEdit().setReadOnly(True)
        self.comboBox.lineEdit().setAlignment(Qt.AlignCenter)        
        self.comboBox.addItem('Seciniz')

        if os.path.exists(os.getcwd()+"/users.txt"):
            users_file = open(os.getcwd()+"/users.txt","r")
            for line in users_file.readlines():
                self.comboBox.addItem(line)                            
        else:
            pass

        
        
        users_file.close()
        

        self.comboBox.setGeometry(100,65,200,40)         
        self.comboBox.activated[str].connect(self.select_user)
        
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        
        self.home()
        
        self.mainGui = mainWindow()

    
    # Var olan kullanıcı
    def markVarolan(self):
        self.textEdit.setEnabled(False)
        self.btnEkle.setEnabled(False)
        self.txtKullanici.setEnabled(False)
        self.comboBox.setEnabled(True)
        self.radioYeni.setChecked(False)
        
    #Yeni kullanıcı
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
        
        self.mainGui.set_calisma_klasoru(path)
        self.mainGui.set_user(self.username)     

        if path !='':
             
            if self.mainGui.current_pair_index < len(self.mainGui.ikililer)-1:
#                print([self.mainGui.current_pair_index, len(self.mainGui.ikililer)])
                
                self.hide()        
#               self.mainGui.show()
                self.mainGui.showMaximized() 
                self.mainGui.show_next_pair()
            else:
                self.mainGui.hide()
                self.show()                
                self.mainGui.infoBox.exec_()                   
                

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
            self.username = text.split('\n') # strip out the trailing '\n' in the file
            self.username = self.username[0] # the split function generates an empty entry to its right, we discard it.

    def raporla(self):
        path = QFileDialog.getExistingDirectory(self, "Klasör Seç",'',   QFileDialog.ShowDirsOnly )
        
        users_data=[]
        pairs = []
        num_max_user_data = 0
        write_pair = False

#        if os.path.exists(path +'/.ikililer.txt'):
#            f_ikililer = open(path +'/.ikililer.txt','r')
#            for line in f_ikililer.readlines():                
#                hasta_data = line.split('_')
#                print(hasta_data)
#                pairs.append(hasta_data)
#        else:
#            pass
            
        
        if os.path.exists(os.getcwd()+"/users.txt"):
            users_file = open(os.getcwd()+"/users.txt","r")
            output_file = open(path+'/Sonuclar.txt','w')
            output_file.write('Hasta ID,Hasta Yasi,Hasta Cinsiyeti,Gun Farki')
            
            for line in users_file.readlines():
                user_fname = path + '/.' + line.split('\n')[0] + '.txt'
#                print(user_fname)
                
                if os.path.exists(user_fname):
                    f_user = open(user_fname,'r')
                    data = [user_line.split('\n')[0] for user_line in f_user.readlines()]  # here, the data are taken as a string array
                    data = data[1:] # first line is info line, discard it.                    
#                    print(data)
                    users_data.append(data) # users_data is an array of string arrays, its length is "number of users", and in each entry, there is a list of strings that iterates on image pairs that each user has evaluated
                
                    num_max_user_data = max(num_max_user_data,len(data))
                else:
                    users_data.append([]) # this user has not made any evaluations on this folder yet
                
                output_file.write( ',' + line.split('\n')[0])
                
#            print(users_data)

            output_file.write('\n')
            
            num_users = len(users_data)

#            print('num_max_user_data = '+str(num_max_user_data) + 'num_users = ' + str(num_users))
            
            for i in range(num_max_user_data):                
                user_scores = ''
                write_pair = True
                for u in range(num_users):
                    if len(users_data[u])-1 < i:
                        user_scores = user_scores + ',-1';
                    else:
                        user_score = int(users_data[u][i].split(',')[4])                        
                        if user_score < 0:
                            write_pair = False
#                            print('dohtor!')
                        else:                            
                            hasta_info = users_data[u][i].split(',')[0]+ ',' + users_data[u][i].split(',')[1] + ',' + users_data[u][i].split(',')[2] + ',' + users_data[u][i].split(',')[3] 
                            user_scores = user_scores + ',' + str(user_score) 

                if write_pair:                
                    output_file.write(hasta_info  + user_scores + '\n')
            
            output_file.close()
            self.mainGui.raporBox.exec_()

        else:
            self.mainGui.errBox.exec_()

        self.textEdit.clear()
        self.textEdit.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.radioVarolan.setEnabled(False)
        self.radioYeni.setEnabled(False)
        self.btnEkle.setEnabled(False)
        self.btnRapor.setEnabled(False)
            

    def close_application(self):
        sys.exit()        



if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        loginGui = loginWindow()
        sys.exit(app.exec_())

run()



