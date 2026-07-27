"""
ikinci sayının sıfır gelme durumu ve bir string gelme 
durumunda hata mesajlarını gördük
"""


try:
    adim = "1A"
    sayi1 = int(input("1.Sayiyi Giriniz :"))
    adim = "2A"
    sayi2 = int(input("1.Sayiyi Giriniz :"))
    adim = "3A"
    sonuc = sayi1/sayi2
    adim = "4A"
    print(sonuc)
except Exception as hata:
    print("Hata Mesajı",hata,"Adim :",adim)
    
finally:
    print("Blog Bitti")
    
print("Devam Ediyor")

"""
finaly her zamana çalışıyormu onu gördük
"""

def Bolme():
    try:
        adim = "1A"
        sayi1 = int(input("1.Sayiyi Giriniz :"))
        adim = "2A"
        sayi2 = int(input("1.Sayiyi Giriniz :"))
        adim = "3A"
        sonuc = sayi1/sayi2
        adim = "4A"
        return sonuc
    except Exception as hata:
        return "Hata Mesajı",str(hata),"Adim :",adim

    finally:
        print("Blog Bitti")

print(Bolme())

print("Devam Ediyor")