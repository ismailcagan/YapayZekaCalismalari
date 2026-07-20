# String Değişknler
var1 = "www.uzaktanegitim.com"
var2 = "www.uzaktanegitim.com"
var3 = """
        Uzaktan Eğitimin
        Adresi
       """
print(var1) # www.uzaktanegitim.com
print(var2) # www.uzaktanegitim.com
# uzaktan eğitim
# Adresi
print(var3)

# String Değişknler İmmutable Değişkenlerdir
## string değişkenler oluşturulduktan sonra üzerinde değişiklik yapılamaz
var4 = "uzaktanegitim"
var4[1] = "h"  # hata
print(var4) #uzaktanegitim

# String Veri Tipleri Fonksiyonlar
var5 = "www.uzaktanegitim.com"
 # harfin handi indisde olduğunu söyler
print(var5.index("w")) #0

##1.Format Fonksiyonu
## format fonksiyonu ile daha önceden belirlenen aralıklara değişiken yerleştirme işlemi yapılır
metin = "Merhaba Hoşgeldiniz {}"
metin2 = "Vektöre"
print(metin.format(metin2)) #Merhaba Hoşgeldiniz Vektöre

metin3 = "Merhaba Hoşgeldiniz Adı :{} Soyadı :{} Telefon :{}"
Adi = "İsmail"
Soyadi = "ÇAĞAN"
telefon = 5393995115
metin3 = metin3.format(Adi, Soyadi, telefon)
print(metin3) #Merhaba Hoşgeldiniz Vektöre

# 2.Split Fonksiyonu
## Belirlediğimiz değişkene göre Metni Böler
metin3 = "www.uzaktanegitim.com"
metin3 = metin3.split(".")
print(metin3) # ['www', 'uzaktanegitim', 'com']

# 3.Strip Fonksiyonu
## Belirlediğimiz ifadeleri metinden atar
var6 = "            uzaktanegitim"
var6 = var6.strip()
print(var6) # uzaktanegitim

var6 = "_______  ______uzaktanegitim__  ___"
# var6 = var6.strip("_")
# print(var6)
for i in var6:
    if i == "_" or i == " ":
        i.strip("_")
        i.strip()
    else:
        print(i,end="") #uzaktanegitim
        
# 4.replace Fonksiyonu
## metin içerisinde karakter veya metin değişimi yapar
metin = "Teşekkürler Süpermen"
metin = metin.replace("e","i").replace("ü","i")
print(metin) #Tişikkirlir Sipirmin

# 5.capitalize Fonksiyonu
## Değişken içerisinde bulunan metnin ilk harfini büyük harfe dönüştürür
metin = "Şermin ve faruk"
metin = metin.capitalize()
print(metin) #Şermin ve faruk

# 6.Index Fonksiyonu
## belirtilen hardin kaçıcı indisde olduğunu söyler
metin = "python programlama dili"
# soldan sağa doğru arar
print(metin.index("p")) #0
# sağdan sola doğru arar
print(metin.rindex("d")) #19

# 7.lower Fonksiyonu (küçük harfe çeviri )
metin = "UZAKTAN EGİTİM"
print(metin.lower()) # uzaktan egi̇ti̇m

# 8. upper fonksiyonu (büyük harfe çevirir)
metin = "uzaktan egitim"
print(metin.upper()) #UZAKTAN EGITIM

# 9. Is ile başlayan fonksiyon
# ıs ile başlayan fonksiyonlar kontrol amaçlı kullanılır. 
# true veya false döner
# genellikle if koşuluyla bereber kullanılır.

# alfabetik ifadeden mi oluşuyor
print("uzaktanegitim.com".isalpha()) # false çünkü nokta işi bozuyor
# alfanumerikmi
print("uzaktanegitimcom".isalnum()) # false çünkü nokta işi bozuyor
# numaramı
print("1120363".isdigit()) # true
print("1120363".isnumeric()) # true
# internet adreslerini başlarında hangi ifadeyle başlıyor onu gösterir
print("www.uzaktanegitim.com".startswith("www")) # true
# internet adreslerini sonları hangi ifadeyle başlıyor onu bitiyor
print("www.uzaktanegitim.com".endswith("com")) # true

# 9. str veri tiplerine erişim
## str veri tipleri dizi olarak tutulur
var1 = "Yaşamak"
# metnin uzunluğunu verir
print(len(var1)) #7
# metnin belirtilen indisdeki harfi verir
print(var1[6]) #k
# 0. indisten 4 indisde dahil içeriği verir
print(var1[0:4]) #Yaşa
# baştan beliritlen isdise kadar değer verir
print(var1[:4]) # Yaşa
# 2. indisten sona kadar içeriği verir
print(var1[2:]) #şamak
# içeriğin tamamını verir
print(var1[:]) # Yaşamak
# içeriği tersten yazdırır
print(var1[::-1]) #kamaşaY
# sondan başlayarak 2 indise kadar tersten yazdırır 
# not:tersten azdırmalarda ilk indis 2.indisten daima büyük olmalıdır
print(var1[6:2:-1]) #kama
print(var1[len(var1)::-1]) #kamaşaY
print(var1[2:4:-1]) # çalışmaz

# içeriği baştan başla sona kadar 2 şer adımla ilerle
print(var1[::2])
# içerik içinde kaç tane a harfi var
print(var1.count("a"))

# 10. escape sequences (kaçış karakteri)
metin = 'Ankara \'da '
print(metin) #Ankara 'da
 
metin = "ismail \n ÇAĞAN"
#ismail 
#ÇAĞAN
print(metin)

metin = "ismail \t ÇAĞAN"
print(metin) #"ismail   ÇAĞAN"

metin = "\t \t Ankara \t \t da"
print(metin.strip()) # Ankara 	 	 da

# 11.raw string
## bir metin kaçış karakteri barındırıyorsa ve bunu dikkate almasını istemiyorsak
## r harfini kullanmalıyız

var1 = "c:\newFolder"
#c:
#ewFolder
print(var1)

var1 = r"c:\newFolder" 
print(var1) #"c:\newFolder"
























