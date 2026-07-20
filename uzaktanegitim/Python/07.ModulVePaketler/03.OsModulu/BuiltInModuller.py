import os
print(os.name) # işletim sistemini veriyor (posix)
print(os.getcwd()) # klasör yolunun verir 
print(os.sep) # kalsör arasında kullanılan ayracı gösterir

yol = os.getcwd() + os.sep +"Defter.csv"  # belirtilen dosyanın yolunu tutar
print(yol)
dosya = open(yol) # belirtilen yoldaki dosyayı açar
print(*dosya.readlines())

os.chdir("/home/ares/Desktop/Yazilimlar/Yapayzeka") # pythonun 
print(os.getcwd())

print(os.curdir) # çalışmış olduğumuz klasörü gösterir tek noktayı ele alır

print(os.pardir) # üst klasörü ele alır iki nokta ile gösterilir

print(os.listdir()) # O an bulunulan klasörün içindeki tüm dosya ve klasörlerin isimlerini bir liste halinde verir.

klasör_isim = input("Lütfen klasör ismi giriniz")
os.mkdir(klasör_isim) # Kullanıcının girdiği isimde tek bir yeni klasör oluşturur. Klasör zaten varsa hata verir.

klasör_isim = "calisma1/calisma2/calisma3"
os.makedirs(klasör_isim) # ç içe geçmiş birden fazla klasörü (zincirleme) tek seferde oluşturur.

for dosya in os.walk(os.curdir): # Bulunduğunuz klasörün ve onun altındaki tüm klasörlerin içini adım adım tarar. Her adımda size 3 bilgi verir:
    print(f"Mevcut Yer :{dosya[0]}") # O an taranan mevcut klasörün yolu.
    print("Klasör Listesi :",*dosya[1]) # O klasörün içindeki alt klasörlerin listesi.
    print("Dosya Listesi :",*dosya[2]) # O klasörün içindeki dosyaların listesi.

print(os.path.exists(os.getcwd() + os.sep +"Defter.csv")) # Belirtilen yolda bir dosya veya klasörün var olup olmadığını kontrol eder (True veya False döner).
print(os.path.isfile(os.getcwd() + os.sep +"Defter.csv")) # Belirtilen yoldaki nesnenin bir dosya olup olmadığını kontrol eder.
print(os.path.isdir(os.getcwd() + os.sep +"Defter.csv")) # Belirtilen yoldaki nesnenin bir klasör (dizin) olup olmadığını kontrol eder.

