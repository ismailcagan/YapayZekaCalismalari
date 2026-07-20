"""
*KWARGS KULLANIMI -> Farklı sayıdaparametre ve veri gönderebiliriz
                    dict veri tipiyle anılır
"""

sozluk = {1: "bir", 2: "iki"}
print("Anahtarlar", sozluk.keys())  # Anahtarlar dict_keys([1, 2])
print("Değerler", sozluk.values())  # Değerler dict_values(['bir', 'iki'])
print("Eleman", sozluk.items())  # Eleman dict_items([(1, 'bir'), (2, 'iki')])

for key, value in sozluk.items():
    print(key, value, end=",")  # 1 bir,2 iki,


def Fonk(**kwargs):
    for key, value in kwargs.items():
        if key == "yazdir":
            print(value)
        if key == "geridon":
            print(value)


Fonk(yazdir="KWARGS")  # 1 bir,2 iki,
Fonk(yazdir="kwargs", geridon="Geri Dönen KWARGS")  # kwargs-Geri Dönen KWARGS


liste = ["isim", "soyisim", "telefon"]
sozluk = dict.fromkeys(liste, "")
kayitListe = [i for i in range(6)]
kayit = dict.fromkeys(kayitListe, sozluk)
print(kayit)
"""
{
    0: {'isim': '', 'soyisim': '', 'telefon': ''}, 
    1: {'isim': '', 'soyisim': '', 'telefon': ''}, 
    2: {'isim': '', 'soyisim': '', 'telefon': ''}, 
    3: {'isim': '', 'soyisim': '', 'telefon': ''}, 
    4: {'isim': '', 'soyisim': '', 'telefon': ''}, 
    5: {'isim': '', 'soyisim': '', 'telefon': ''}
}
"""
def KayitGüncelle(**kwargs):
    id = isim = soyisim = telefon = 0
    for key, value in kwargs.items():
        if key == "id":
            id = value
        elif key == "isim":
            isim = value
        elif key == "soyisim":
            soyisim = value
        elif key == "telefon":
            telefon = value
    kayit[id] = SozlukGuncelle(isim=isim, soyisim=soyisim, telefon=telefon)

def SozlukGuncelle(**kwargs):
    sozluk = {}
    for key, value in kwargs.items():
        sozluk[key] = value
    return sozluk

isim = ["Ali", "Ayşe", "Fatma", "Ahmet", "Faruk", "Soner"]
soyisim = "Python"
telefon = "123456"

for i in range(6):
    KayitGüncelle(id=i, isim=isim[i], soyisim=soyisim, telefon=telefon)
print(kayit)

"""
{
    0: {'isim': 'Ali', 'soyisim': 'Python', 'telefon': '123456'}, 
    1: {'isim': 'Ayşe', 'soyisim': 'Python', 'telefon': '123456'}, 
    2: {'isim': 'Fatma', 'soyisim': 'Python', 'telefon': '123456'}, 
    3: {'isim': 'Ahmet', 'soyisim': 'Python', 'telefon': '123456'}, 
    4: {'isim': 'Faruk', 'soyisim': 'Python', 'telefon': '123456'}, 
    5: {'isim': 'Soner', 'soyisim': 'Python', 'telefon': '123456'}
}
"""
