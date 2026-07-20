# *args KULLANIMI -> FOnksiyona göndereceğimiz parametre sayısı belli değilse kullanırız
# args parametresi tuple veri tipi ile algılanır
# tuple veri tipine nasıl ulaşıyorsak aynı şekilde ulaşırız

liste = [1, 2, 3, 4, 5, 6]
print(liste)  # [1, 2, 3, 4, 5, 6]
print(*liste)  # 1 2 3 4 5 6 -> eleman teker teker ele alınır


def Fonk(sayilar):
    sonuc = 0
    for i in liste:
        sonuc += i
    return sonuc


print(Fonk([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 21


def Fonk1(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc


print(Fonk1(1, 2, 3, 4, 5))  # 15
print(Fonk1(1, 2, 3, 4, 5, 6, 7, 8, 9))  # 45
# Not -> değerler liste olarak tanımlamaya ihtiyaç olmadı
#       birde istediğimiz kadar farklı değer gönderebiliriz


def Fonk2(*args):
    liste = []
    for i in args:
        if i % 2 == 0:
            liste.append(i)
    return liste


print(Fonk2(1, 5, 21, 8, 7, 2, 6, 5, 12, 36, 85, 94, 13))  # [8, 2, 6, 12, 36, 94]

liste = ["isim", "soyisim", "il"]
sozluk = dict.fromkeys(liste, "")


def Fonk3(*args):
    for i in range(0, len(args)):
        if i == 0:
            sozluk["isim"] = args[i]
        elif i == 1:
            sozluk["soyisim"] = args[i]
        elif i == 2:
            sozluk["il"] = args[i]
    return sozluk
print(Fonk3("İsmail","ÇAĞAN","ORDU")) #{'isim': 'İsmail', 'soyisim': 'ÇAĞAN', 'il': 'ORDU'}

liste = ["isim", "soyisim", "il"]
sozluk = dict.fromkeys(liste, "")
