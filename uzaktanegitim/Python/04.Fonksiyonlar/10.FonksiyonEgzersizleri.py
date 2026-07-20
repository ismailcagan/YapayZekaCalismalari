# 1.Bir liste alan ve ilk listenin benzersiz öğelerini içeren yeni bir liste döndüren bir python programlama fonksiyonu yazınız


def Fonk(liste):
    yeniListe = []
    for eleman in liste:
        if eleman not in yeniListe:
            yeniListe.append(eleman)
    return yeniListe


print(Fonk([1, 1, 1, 2, 3, 4, 5, 5, 6, 6, 7]))  # [1, 2, 3, 4, 5, 6, 7]


# farklı yöntem
def Fonk(liste):
    yeniListe = []
    for eleman in liste:
        if eleman in yeniListe:
            continue
        else:
            yeniListe.append(eleman)
    return yeniListe


print(Fonk([1, 1, 1, 2, 3, 4, 5, 5, 6, 6, 7]))  # [1, 2, 3, 4, 5, 6, 7]


# 2. Girilen sayıyı yazıyla çıktı veren python programını fonksiyon olarak yazınız
"9,652,412"
"Dokuz milyon altıyüz elli iki milyon dört yüz elli iki"
metin = "9,652,412"
def YazıyaCevir(sayi):
    birler = {"0": "","1": "Bir","2": "iki","3": "Üç","4": "Dört","5": "Beş","6": "Altı","7": "Yedi","8": "Sekiz","9": "Dokuz",}
    onlar = {"0": "","1": "On","2": "Yirmi","3": "Otuz","4": "Kırk","5": "Elli","6": "Atmış","7": "Yetmiş","8": "Seksen","9": "Doksan",}
    basamak = {"1": "","2": "Bin","3": "Milyon","4": "Milyar","5": "Trilyon","6": "Katirilyon",}
    metin = sayi.replace(".", "").replace(",", "")
    while len(metin) % 3 > 0:
        metin = "0" + metin
    print(metin)  # 009652412

    liste = []
    buyuksonuc = ""
    for i in range(len(metin)//3):
        liste.append(metin[i * 3 : i * 3 + 3])
    print(liste)  # ['009', '652', '412']

    for i in range(len(metin) // 3):
        # metni 3 böler bölüm kadar döner # ilk indiste 009 var # ikinci indiste 652 var # üçüncü indiste 412 var
        print(liste[i])
        """
        009
        652
        412
        """
        sonuc = ""
        sayi = liste[i]
        if sayi[0] != "0":
            if sayi[0] != "1":
                sonuc = birler[sayi[0]] + "Yüz"
            else:
                sonuc = "Yüz"
        sonuc = sonuc + onlar[sayi[1]] + " "
        sonuc = sonuc + birler[sayi[2]] + " "
        sonuc = sonuc + basamak[str((len(metin) // 3) - i)] + " "
        buyuksonuc += sonuc
    return buyuksonuc
print(YazıyaCevir("9,652,412"))

# 3. Verilen Sayının Polindrom Olup Olmadığını Bulun
def Palindrom(metin):
    if len(metin)<=1:
        return True
    else:
        return metin[0] == metin[-1] and Palindrom(metin[1:-1])

def GirisAll():
    metin = input("Metni Giriniz")
    return Palindrom(metin.replace(" ","").replace(".","").replace(",","").lower())
print(GirisAll())
#At, sahibi gibi hasta

# 4.IBAN NUMARASININ DOĞRU OLUP OLMADIĞINI KONTROL ETME
def IBANDogrulama(IBAN):
    IBAN_1 = str(ord(IBAN[0])-55) + str(ord(IBAN[1])-55) + IBAN[2:]
    print(IBAN_1) #2927000000100100000350930001
    IBAN_1 = IBAN_1[6:] + IBAN_1[:6]
    print(IBAN_1) # 0000100100000350930001292700
    sayi1 = int(IBAN_1[:9]) %97
    print(sayi1) # 19
    sayi2 = int(str(sayi1)+IBAN_1[9:18]) %97
    print(sayi2) # 43
    sayi3 = int(str(sayi2) +IBAN_1[18:28]) %97
    print(sayi3) # 1
    if sayi3 == 1:
        return True
    else:
        return False

IBAN = "TR470000100100000350930001"
print(IBANDogrulama(IBAN)) #True















