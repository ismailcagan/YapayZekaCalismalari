def DosyaAc(adres):
    import os
    if os.path.exists(adres):
        return open(adres, "r+", encoding="utf-8")
    else:
        return open(adres, "w+", encoding="utf-8")

def Listele():
    #dosya.seek(0)
    if len(liste) == 0:
        print("Liste Boş")
        print("-------------------------------------------")
    else:
        for i in range(len(liste)):
            Adi, Soyadi, Telefon = liste[i].split(";")
            satir = f"{i+1}-{Adi} {Soyadi} {Telefon}"
            print(satir)
        print("-------------------------------------------")
        
def GirisYap():
    adi = input("Adini Giriniz")
    soyadi = input("Soyadini Giriniz")
    telefon = input("Telefon Giriniz")
    kayit = f"{adi};{soyadi};{telefon}\n"
    return kayit
        
def KayitListele():
    Listele()

def KayitEkle():
    kayit = GirisYap()
    liste.append(kayit)

def KayitDüzelt():
    if not liste or len(liste) == 0:
        print("Liste Boş")
    else:
        for i in range(len(liste)):
            Adi, Soyadi, Telefon = liste[i].split(";")
            satir = f"{i+1}-{Adi} {Soyadi} {Telefon}"
            print(satir)
    kayitNum = int(input("Güncellemek İstediğiniz NUmarayı Giriniz"))
    kayit = GirisYap()
    liste[kayitNum - 1] = kayit

def KayitSil():
    if not liste or len(liste) == 0:
        print("Liste Boş")
    else:
        for i in range(len(liste)):
            Adi, Soyadi, Telefon = liste[i].split(";")
            satir = f"{i+1}-{Adi} {Soyadi} {Telefon}"
            print(satir)
    kayitNum = int(input("Silmek İstediğiniz NUmarayı Giriniz"))
    del liste[kayitNum - 1]

def Menu():
    Menu = """
        1-)Listele
        2-)Ekleme
        3-)Güncelleme
        4-)Silme
        5-)Çıkış
        İşlem Seçiniz
    """
    anahtar = 1
    while anahtar == 1:
        islem = input(Menu)
        if islem == "5":
            anahtar = 0
        elif islem == "1":
            KayitListele()
        elif islem == "2":
            KayitEkle()
        elif islem == "3":
            KayitDüzelt()
        elif islem == "4":
            KayitSil()
    else:
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
        dosya.close()
adres = "defter.csv"
dosya = DosyaAc(adres)
liste = dosya.readlines()