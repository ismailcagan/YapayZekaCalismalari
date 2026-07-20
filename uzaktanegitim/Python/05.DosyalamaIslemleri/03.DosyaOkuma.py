
def dosyaAc(adres):
    import os # Klasör ve Dosya Kontrol İşlemleri İçin bu kütüphane gerekir
    if os.path.exists(adres): # içine yazılan dosya yolunda bir dosyanın olup olmadığını kontrol eder
        return open(adres,"r+",encoding="utf-8") # dosya varsa içinde okuma ve yazma yapabiliriz
    else: # eğer beliritlen dosya yolunda dosya yoksa 
        return open(adres,"w+",encoding="utf-8") # dosya oluşturur ve içinde okuma yazma yapabiliriz

dosya = dosyaAc("Defter1.txt")

dosya.read() # Dosyanın Tamamını Okur
dosya.seek(0) # İmleci Başa Alır
dosya.read(50) # 50 bytlık veri okur

dosya.readline() # ilk satırı okur
dosya.readline(5) # ilk 5 harfi okur

liste = dosya.readlines() # dosyanın içindeki veriyi listeye veriri
print(liste)
dosya.seek(0)
print(*liste) # verileri alt alta yazar