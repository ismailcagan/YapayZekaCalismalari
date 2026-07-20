"""
Toplam Ciro: Tüm siparişlerin toplam tutarı ne kadar?
Kategori Bazlı Analiz: Hangi kategoride (Elektronik, Tekstil vb.) toplam kaç TL'lik satış yapılmış?
En Değerli Müşteri (VIP): En çok harcama yapan MüşteriID hangisidir ve toplam ne kadar harcamıştır?

MüşteriID;ÜrünKategorisi;SiparişTutarı
"""
siparisler = [
    "101;Elektronik;5000",
    "102;Tekstil;1200",
    "101;Kozmetik;450",
    "103;Elektronik;2500",
    "102;Tekstil;800",
    "104;Kitap;150",
    "101;Elektronik;1200",
    "103;Tekstil;600"
]

def VIPId():
    idTotal = {}
    enbValue = 0
    enbKey = 0
    for i in siparisler:
        id,category,total = i.split(";")
        if id not in idTotal:
            idTotal[id] = int(total)
        else:
            idTotal[id] = idTotal[id] + int(total)
            
    for key,value in idTotal.items():
        if value>enbValue:
            enbValue = value
            enbKey = key
    print(f"{enbKey} - {enbValue}")
VIPId()
            
def CategoryAnalist():
    Categories = {}
    for i in siparisler:
        Id,Category,Total = i.split(";")
        CategoryTotal = int(Total)
        
        if Category in Categories:
            Categories[Category] = Categories[Category] + CategoryTotal
        else:
            Categories[Category] = CategoryTotal
            
    for key,value in Categories.items():
        print(f"{key} - {value}")
CategoryAnalist()

def AllTotal():
    totalCiro = 0
    for i in siparisler:
        Id,Category,Tutar =  i.split(";")
        totalCiro += int(Tutar)
    print(totalCiro)

if __name__ == "main":
    AllTotal()

"""
Elimizde bir hisse senedinin sırasıyla günlere göre fiyatlarını tutan bir liste var 
(0. gün, 1. gün, 2. gün...):
Maksimum Kâr Ne Kadar? Bu hisseden (önce düşük fiyattan alıp, sonra yüksek fiyattan satarak) 
        elde edilebilecek en yüksek kâr kaç TL'dir?
Hangi Gün Alıp Hangi Gün Satmalı? Bu maksimum kârı elde etmek için hisseyi kaçıncı gün alıp, 
        kaçıncı gün satmalıyız?

def Dict():
    GunFiyat = {}
    for i in range(len(fiyatlar)):
        GunFiyat[i] = fiyatlar[i]
    return GunFiyat
print(Dict())

fiyatlar = [70, 10, 50, 40, 80, 49, 100, 20]

def EnYuksekKar(dict):
    enbuyuk = 0
    kar = 0
    endusuk = dict[0]
    for i in range(len(list)):
        if 
      
EnYuksekKar(fiyatlar)
"""