
def dosyaAc(adres):
    import os # Klasör ve Dosya Kontrol İşlemleri İçin bu kütüphane gerekir
    if os.path.exists(adres): # içine yazılan dosya yolunda bir dosyanın olup olmadığını kontrol eder
        return open(adres,"r+",encoding="utf-8") # dosya varsa içinde okuma ve yazma yapabiliriz
    else: # eğer beliritlen dosya yolunda dosya yoksa 
        return open(adres,"w+",encoding="utf-8") # dosya oluşturur ve içinde okuma yazma yapabiliriz

dosya = dosyaAc("Defter1.txt")

dosya.write("\nProgramdan Geldi")
dosya.writelines(["\n İsmail","ÇAĞAN"," ORDU"])
dosya.close()
dosya.seek(0)
dosya.read()