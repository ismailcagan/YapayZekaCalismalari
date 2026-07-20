# Gömülü FOnksiyonlar -> Hazır Fonksiyonlar

# 1.map() Fonksiyonu
"""
Python'da map() fonksiyonu, bir listedeki 
(veya herhangi bir döngüsel verideki) tüm elemanlara 
belirli bir fonksiyonu tek tek uygulamak için kullanılır.
"""
def karesi(x):
    return x * x

liste = [1, 2, 3, 4, 5]

def KaresiSonuc():
    sonuc=[]
    #sonuc =[none] * len(liste)
    for i in range(len(liste)):
        sonuc.append(karesi(liste[i]))
        #sonuc[i]=(karesi(liste[i]))
    print(sonuc) 
KaresiSonuc() # [1, 4, 9, 16, 25]
    
list(map(karesi,liste)) #[1, 4, 9, 16, 25]
for i in map(karesi,liste):
    print(i)
"""
1
4
9
16
25
"""

# 2.Zip Fonksiyonu
"""
Python'da zip() fonksiyonu, birden fazla listeyi 
(veya döngüsel veriyi) aynı indeksteki elemanlarına göre 
eşleştirerek bir araya getirmek (fermuar gibi birleştirmek) 
için kullanılır.Tıpkı bir montun fermuarını çektiğinizde iki 
tarafın dişlerinin sırayla birbirine geçmesi gibi, zip() de 
listelerin elemanlarını sırasıyla 
(1. elemanları bir arada, 2. elemanları bir arada olacak şekilde) 
eşleştirir.
Girdi olarak verdiğiniz listeleri alır ve her adımdaki 
elemanları tuple (demet) yapısı içinde birleştirir.
"""

liste = [1,2,3,4,5,7]
liste2 = ["a","b","c","d","e","f"]
list(zip(liste,liste2))
for i,j in zip(liste,liste2):
    print(i,j)
"""
1 a
2 b
3 c
4 d
5 e
7 f
"""

# 3.len() Fonksiyonu
"""
Python'da len() fonksiyonu, bir nesnenin içindeki eleman sayısını (uzunluğunu) bulmak için kullanılır. 
İngilizcedeki "length" (uzunluk) kelimesinin kısaltmasıdır.
"""
sozluk ={str(i):i for i in range(5)}
print(sozluk) # {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}
print(len(sozluk)) # 5

metin ="123"
print(len(metin)) #3

# 4.All() Fonksiyonu
"""
Python'da all() fonksiyonu, bir listenin (veya döngüsel herhangi bir verinin) içindeki tüm elemanların 
"Doğru" (True) olup olmadığını kontrol etmek için kullanılır.Mantıksal kapılardaki VE (AND) işlemine benzer. 
Sadece ve sadece tüm elemanlar True ise True sonucunu verir; 
araya tek bir tane bile "Yanlış" (False) değer karışırsa anında False döndürür.
all() Nasıl Çalışır? (Python'daki True/False Mantığı)Python'da sadece True kelimesi değil, 
sıfırdan farklı sayılar ve içi dolu listeler/metinler de mantıksal olarak True kabul edilir.
Buna karşılık; 0, None, boş metin "" veya boş liste [] gibi değerler False kabul edilir.
"""
liste = [0,1,2,3,4,5]
print(all(liste)) #False -> listede sıfır olduğu için

liste = [1,1,2,3,4,5] 
print(all(liste)) # True -> listede 0 olmadığı için
#Not -> eksili sayılarıda True kabul eder

liste = ["Ordu","Samsun",""]
print(all(list)) # False -> Listede Boş Eleman olduğu için

liste = ["Ordu","Samsun","Giresun"]
print(all(list)) # True -> Listedeki elemanların hepsi dolu olduğu için

# 5.any() Fonksiyonu
"""
Python'da any() fonksiyonu, bir listenin (veya döngüsel herhangi bir verinin) 
içinde en az bir tane bile "Doğru" (True) eleman olup olmadığını 
kontrol etmek için kullanılır.Mantıksal kapılardaki VEYA (OR) işlemine benzer. 
Listenin içinde tek bir tane bile True değer bulursa anında 
True sonucunu döndürür. Sadece ve sadece tüm elemanlar 
False ise False sonucunu verir.Kısacası: all() fonksiyonu "Herkes uymalı" 
derken, any() fonksiyonu "Bir kişinin uyması bile yeterli" der
"""
liste = [0,1,2,3,4,5]
print(any(liste)) #True

liste1= [1,1,2,3,4,5] 
print(any(liste1)) # True

liste2 = ["Ordu","Samsun",""]
print(any(liste2)) # True

liste3 = ["Ordu","Samsun","Giresun"]
print(any(liste3))

liste4 = []
print(any(liste4)) # False

liste5 = ["Ordu","Samsun","Giresun"]
sozluk = dict.fromkeys(liste,"")
print(any(sozluk)) 
# True -> sözlükte gömülü fonksiyonlara ulaşmaya çalışıldığında key ulaşır
#           keyde dolu olduğu için True döndü

# 6. eval() Fonksiyonu
"""
Python'da eval() fonksiyonu, metin (string) formatında yazılmış olan Python kodlarını dinamik olarak 
çalıştırmak ve sonucunu döndürmek için kullanılır. İngilizcedeki "evaluate" (değerlendirmek/hesaplamak) 
kelimesinden gelir.Normalde Python bir metni sadece yazı olarak görür. Ancak eval() fonksiyonunun içine o metni 
yazarsanız, Python onu canlı bir kod satırı gibi algılar ve işleme alır.
"""
islem = input("Yapmak istediğiniz işlemi Yazınız")  #5+4
print(eval(islem)) # 9 -> direk işlemi yapar

# 7. exec() Fonksiyonu
"""
Python'da exec() fonksiyonu, metin (string) formatında yazılmış olan çok satırlı, karmaşık Python kod bloklarını 
dinamik olarak çalıştırmak için kullanılır. İngilizcedeki "execute" (çalıştırmak/yürütmek) kelimesinden gelir.
"""
kod_blogu = """
toplam = 0
for i in range(1, 6):
    toplam += i
print('Döngü içi toplam:', toplam)
"""
exec(kod_blogu) # Döngü içi toplam: 15

# 8. globals() Fonksiyonu
"""
Python'da globals() fonksiyonu, kodunuzun o anki küresel (global) alanında tanımlı olan tüm değişkenleri, 
fonksiyonları ve kütüphaneleri bir sözlük (dictionary) olarak döndürür.Küresel alan, kodun en dış seviyesidir 
(yani herhangi bir fonksiyonun veya sınıfın içinde olmayan, her yerden erişilebilen alandır).globals() 
fonksiyonunu çağırdığınızda dönen bu sözlükte, anahtarlar (keys) değişkenlerin isimlerini metin (string) olarak, 
değerler (values) ise o değişkenlerin o anki içeriklerini gösterir.
"""
yas = 25
isim = "Ahmet"

# 9.globals() sözlüğünü alıyoruz
kuresel_hafiza = globals()

# Değişken isimleriyle değerlerine sözlük mantığıyla erişebiliriz:
print(kuresel_hafiza["isim"])  # Çıktı: Ahmet
print(kuresel_hafiza["yas"])   # Çıktı: 25

# 'yeni_degisken' adında bir global değişken oluşturuyoruz
globals()["yeni_degisken"] = "Ben dinamik oluştum!"
# Artık bu değişkeni normal bir şekilde çağırabiliriz:
print(yeni_degisken)  # Çıktı: Ben dinamik oluştum!


tehlikeli_kod = "print(yas)" # normalde globaldeki 'yas' değişkenine erişebilir
yas = 25
# Kendi izole alanımızı yaratıyoruz (Gerçek globals() yerine boş sözlük veriyoruz)
izole_alan = {}
# exec sadece izole_alan içindeki değişkenleri görebilir, bilgisayardaki 'yas'ı göremez
exec(tehlikeli_kod, izole_alan)  # NameError: name 'yas' is not defined hatası verir ve sistemi korur!

# 10.locals() Fonksiyonu
"""
Python'da locals() fonksiyonu, o an bulunulan yerel (local) 
kapsamdaki (örneğin bir fonksiyonun içindeki) tüm değişkenleri ve 
parametreleri bir sözlük (dictionary) olarak döndürür.
Küresel alandaki globals() fonksiyonunun aksine, locals() 
sadece çağrıldığı fonksiyonun sınırları içerisindeki dünyayı görür. 
Fonksiyon çalışmayı bitirdiğinde bu yerel hafıza da tamamen silinir.
"""
# Burası küresel (global) alan
x = "Ben globalim"
# Bir fonksiyon tanımlıyoruz
def ornek_fonksiyon(parametre_a):
    y = "Ben yerelim"
    z = 100
    
    # Sadece bu fonksiyonun içindeki değişkenleri yazdırıyoruz
    print(locals())

# Fonksiyonu çağırıyoruz
ornek_fonksiyon("Merhaba") # {'parametre_a': 'Merhaba', 'y': 'Ben yerelim', 'z': 100}

def kullanici_karti(ad, soyad, yas):
    meslek = "Yazılımcı"
    
    # locals() sayesinde değişkenleri tek tek eşleştirmekle uğraşmayız
    metin = "{ad} {soyad} ({yas}) - {meslek}".format(**locals())
    return metin

print(kullanici_karti("Can", "Yılmaz", 30))
# Çıktı: Can Yılmaz (30) - Yazılımcı

# 11.enumerate() Fonksiyonu
"""
Python'da enumerate() fonksiyonu, bir listenin (veya döngüsel bir verinin) 
elemanları üzerinde dönerken, her elemanın indeks (sıra) numarasını ve 
kendisini aynı anda takip etmek için kullanılır.Normalde bir for döngüsü 
yazdığınızda sadece elemanları alırsınız. Eğer o elemanların kaçıncı sırada o
lduğunu da bilmek istiyorsanız, dışarıda geçici bir sayaç değişkeni (sayac = 0) 
tanımlayıp her adımda artırmak yerine enumerate() kullanırsınız. 
Kodunuzu çok daha temiz ve profesyonel hale getirir.
"""
metin = "python"
print(list(enumerate(metin)))
# [(0, 'p'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
urunler = ["Laptop", "Telefon", "Kulaklık", "Klavye"]


for indeks, urun in enumerate(urunler):
    print(f"{indeks}. sıradaki ürün: {urun}")

# Çıktı:
# 0. sıradaki ürün: Laptop
# 1. sıradaki ürün: Telefon
# 2. sıradaki ürün: Kulaklık
# 3. sıradaki ürün: Klavye

urunler = ["Laptop", "Telefon", "Kulaklık"]

# Saymaya 1'den başla talimatı verdik
for sira, urun in enumerate(urunler, start=1):
    print(f"{sira}- {urun}")
# Çıktı:
# 1- Laptop
# 2- Telefon
# 3- Kulaklık

# 12.Sorted() Fonksiyonu
"""
Python'da sorted() fonksiyonu, bir listenin (veya döngüsel herhangi bir verinin) 
elemanlarını küçükten büyüğe (alfabetik veya sayısal olarak) sıralamak için kullanılır.
"""
# Sayıları küçükten büyüğe sıralar
sayilar = [5, 2, 9, 1, 7]
sirali_sayilar = sorted(sayilar)
print(sirali_sayilar)  # Çıktı: [1, 2, 5, 7, 9]
print(sayilar)         # Çıktı: [5, 2, 9, 1, 7] (Orijinal liste bozulmadı!)

# Metinleri alfabetik olarak sıralar
isimler = ["Veli", "Ali", "Can"]
print(sorted(isimler)) # Çıktı: ['Ali', 'Can', 'Veli']

import locale
#locale.setlocale(locale.LC_ALL,"Turkish_TURKEY.1254")
locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")
liste = ["Ayşe","Işıl","Sermin","Çiğdem","Hakkı","Soner"]
sorted(liste,key=locale.strxfrm)
print(liste)

# ALTERNATİF YOL
import locale
try:
    # Linux, macOS ve bulut ortamları için evrensel standart
    locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")
except locale.Error:
    try:
        # Windows işletim sistemi için alternatif genel tanım
        locale.setlocale(locale.LC_ALL, "Turkish")
    except locale.Error:
        # Eğer sistemde hiçbir Türkçe paketi yoksa hata vermemesi için güvenli geçiş
        print("Sistemde Türkçe dil paketi bulunamadı!")

liste = ["Ayşe", "Işıl", "Sermin", "Çiğdem", "Hakkı", "Soner"]

# DİKKAT: sorted() yeni liste döndürdüğü için 'sirali_liste' değişkenine atadık
sirali_liste = sorted(liste, key=locale.strxfrm)

print(sirali_liste)
# Doğru Çıktı: ['Ayşe', 'Çiğdem', 'Hakkı', 'Işıl', 'Sermin', 'Soner']