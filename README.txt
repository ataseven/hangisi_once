Hangisi_once.py
Yoldaş Ataseven

PROGRAMI ÇALIŞTIRMA:

1) Python 3.6 kur ve çalışıp çalışmadığını kontrol et: Komut satırından (windows: windows tuşu->cmd, linux: terminal)

python3.6
>>>

2) pip3 ile pyqt5 kur:
Komut satırından 

pip3 install pyqt5

3) github'dan hangisi_once dosyalarını indir:
https://github.com/ataseven/hangisi_once
clone or download tuşu ile "Download ZIP" diyerek dosyaların bulunduğu zip dosyasını indir


4) İndirdiğin zip dosyasını aç. Örnek olarak, Windows için D:\hangisi_once\ klasörünün içine açıldığını varsayacağız (Doğrudan D:\ 'ye "extract zip" denirse D:\hangisi_once-master\ klasörü oluşur, bunu rename et). Bu klasörün içi şu şekilde olacak:

hangisi_once\
hangisi_once.py
os
sys
users.txt


5) Komut satırından D:\hangisi_once\ satırına git. Windows için:

d:
cd d:\hangisi_once


6) hangisi_once.py dosyasını çalıştır:

python3.6 hangisi_once.py

7) Kullanıcı arayüzündeki listeden seçerek daha önce tanımlanmış kullanıcılardan birisini seç ya da "Yeni kullanıcı" butonuna basarak yeni kullanıcı adını yaz ve "Ekle" (yeni eklenen kullanıcı otomatik olarak listeye eklenir ve seçili kullanıcı olarak işaretlenir).

8) "Klasör Seç" tuşuyla çalışma klasörünü seç. Açılış ekranı kapanır ve çalışma ekranına geçilir. Çalışma ekranına geçildiğinde, o kullanıcı tarafından o ana kadar işaretlenmiş ikililer geçilerek, işaretlenmemiş ilk ikili ekranda gösterilir.

9) Kullanıcının her işaretlemesinde, kullanıcı dosyası (Örn: "Ahmet Yılmaz.txt") açılır, bu bilgi kullanıcı dosyasına yeni bir satır olarak eklenir, kullanıcı dosyası kapatılır ve bir sonraki ikili gösterilir. Dolayısıyla, yazılım çökse ya da kullanıcı tarafından herhangi bir anda yanlışlıkla kapatılsa dahi kullanıcının o ana kadar yaptığı işaretlemeler kaybolmaz.

10) Herhangi bir anda, kullanıcı arayüzü kapatıldığında, kullanıcıya "Emin misin?" diye sorulmaz. Çünkü zaten her şey kaydedilmiştir.


PROGRAM AYAR VE VERİ DOSYALARI:
1) Ana klasörün (D:\hangisi_once\) içindeki 

users.txt 

dosyasında kullanıcı isimleri yazılıdır. Program her çalıştırıldığında bu dosyada yazan kullanıcı isimlerini okuyarak açılış ekranındaki drop-down menü (combo box) listesine koyar. Kullanıcının hatasız kullanımında bu dosyayı elle düzeltmek gerekmez. Elle düzeltmek gerekirse: Her satırda tek bir kullanıcı adı yazılı olmalıdır ve satır başlarında boşluk olmamalıdır (boşluk olsa da düzgün çalışma ihtimali var, denemedim). Yine, kullanıcı isimleri arasında boş satır olmamalıdır.

Yeni kullanıcı seçeneği ile yeni kullanıcı ismi yazılıp "Ekle" butonuna basıldığında Users.txt dosyasına bu kullanıcı adı eklenir. Ancak burada hatalı ya da mükerrer giriş yapıldığında kullanıcı arayüzünden hatalı/mükerrer kaydı silme imkanı yoktur. Bu kullanıcı isimlerini elle silmek gererkir.

Mükerrer kullanıcı adı olması durumu: Örneğin, "Ahmet Yılmaz" ismiyle iki kez aynı kullanıcı ismi "Ekle"nirse, yazılım bu mükerrerliği tespit edemez ve açılıştaki listede iki tane "Ahmet Yılmaz" görünür. Ancak bu durum görsel kirlilik dışında sıkıntı çıkarmaz.

Aynı kullanıcının farklı isimlerle eklenmesi durumu: Birbirinden faklı yazılmış her kullanıcı ismi başka bir kullanıcı olarak ele alınır. Yanlış yazılarak "Ekle"nen kullanıcı isimlerinin users.txt dosyasından silinmesi gerekir.

2) Çalışılan herhangi bir klasör içindeki

ikililer.txt 

dosyasında, bu klasörde çalışılırken kullanılacak olan ikililer yazılıdır. Eğer bir klasörde bu dosya yoksa, bu klasörde çalışmaya başlayan ilk kullanıcı klasörü seçtiği anda bütün klasör taranarak dosya listesi incelenir ve ikililer.txt dosyası oluşturulur. Aynı kullanıcı programı tekrar açlıştırıp bu klasörü tekrar seçtiğinde ya da başka kullanıcılar bu klasörü seçtiğinde yazılım "ikililer.txt" dosyasının olup olmadığı kontrol eder, dosyayının var olduğunu görür ve bunu kullanır (okur), tekrar oluşturmaz ya da dosyaya müdahale etmez. Böylece bütün kullanıcıların aynı ikililer üzerinde çalışması sağlanır.

Ne yaptığınızı bilmiyorsanız, ikiler.txt dosyasını silmeyiniz ya da değiştirmeyiniz. Bu dosya silindiği takdirde, kullanıcılar yeni işaretleme yaptığında sonuçlar (bazı hastalar için) bulanık olur, çünkü kullanıcı dosyalarında görüntü ikililerine dair doğrudan bilgi bulunmaz (dolaylı bilgi bulunur).

ikiler.txt dosyası oluştuktan sonra klasöre eklenen yeni görüntüler dikkate alınmaz. Bunların dikkate alınması için ikiler.txt dosyasının silinmesi ve yazılım tarafından tekrar oluşturulması gerekir, ancak bu durumda da, bazı kullanıcıların (bazı durumlarda), bazı ikileri hiç işaretlememe ihtimali doğar.

Özetle:
Bir klasör üzerinde yazılım ile çalışmaya başlandıktan sonra:
- Klasöre yeni görüntü eklemeyin
- Klasördeki ikililer.txt dosyasını değiştirmeyin ya da silmeyin. Bu dosya, yazılımın yönetmesi için hazırlanmış bir dosya.

3) Çalışılan herhangi bir klasör içindeki

<Kullanıcı ismi>.txt

dosyasında, bu kullanıcının yaptığı işaretlemelere dair bilgiler bulunur. Her satır ayrı bir görüntü ikilisine aittir. Bir satırdaki bilgi şu şekildedir:

ID, yaş, cinsiyet, zaman farkı(gün), tahmin (1:doğru 0:yanlış)

Bilgiler virgüllerle ayrılır ve virgüllerin önünde ya da arkasında boşluk bulunmaz.
Zaman farkı değeri olarak, ekranda sağda gösterilen görüntünün tarihinden solda gösterilen görüntünün tarihi çıkarıldığı zaman elde edilen sonuç gösterilir. Dolayısıyla, eğer sağdaki görüntü daha eski ise, zaman farkı negatif çıkar.

Bir kullanıcı ismi ve klasör seçildiği zaman, yazılım ilgili klasördeki <Kullanıcı ismi>.txt dosyasını açar, satır sayısını sayar ve ikililer.txt dosyasının hangi satırından itibaren devam etmesi gerektiğini bulur.

Kullanıcı, program arayüzünden yaptığı bir işaretlemeyi kullanıcı arayüzünü kullanarak değiştiremez/silemez. Bunun için <Kullanıcı ismi>.txt dosyasını elle değiştirmesi gerekir.

<Kullanıcı ismi>.txt dosyası elle düzeltilecekse, aradan satır silinmemelidir. Örneğin, sondan 5 önceki işaretlemede hata olduysa, bu hatanın düzeltilmesi için, bu satırın ve bundan sonraki satırların tamamının silinmesi gereklidir. Özetle, aradan satır silmeyin.






