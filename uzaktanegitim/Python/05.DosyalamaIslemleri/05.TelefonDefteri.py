def Listele(liste):
    for i in range(len(liste)):
            isim, soyisim, telefon = liste[i].split(";")
            metin = f"{i+1}-{isim} {soyisim} {telefon}"
            print(metin)
    print("--------------------------------------------")
    
def KayitAl():
    isim = input("İsim Girin :")    
    soyisim = input("Soyisim Girin :")
    telefon = input("Telefon Girin :")
    veri = isim + ";" + soyisim + ";" + telefon + "\n"
    return veri

def DosyaAc(adres):
    import os
    if os.path.exists(adres):
        return open(adres, "r+", encoding="utf-8")
    else:
        return open(adres, "w+", encoding="utf-8")
    
dosya = DosyaAc("Defter.csv")
menu = """  1.Listele   2.EKle  3.Sil   4.Güncelle  5.Çıkış     İşlemSeçiniz :  """
liste = dosya.readlines()
anahtar = 1
while anahtar == 1:
    islem = int(input(menu))
    if islem == 1:  Listele(liste)
    elif islem == 2:    
        veri = KayitAl()    
        liste.append(veri)
    elif islem == 3:
        Listele(liste)
        kayitNum = int(input("Silmekİstediğiniz Kaydı Seçiniz"))
        liste.pop(kayitNum - 1)
        print("--------------------------------------------")
        Listele(liste)
    elif islem == 4:
        Listele(liste)
        kayitNum = int(input("Güncellemek İstediğiniz Kaydı Seçiniz"))
        veri = KayitAl()
        liste[kayitNum - 1] = veri
        print("--------------------------------------------")
        Listele(liste)
    elif islem == 5:
        anahtar = 0
else:
    dosya.seek(0)
    dosya.truncate()  # imleçten sonrasını siler
    dosya.writelines(liste)
    dosya.close()
