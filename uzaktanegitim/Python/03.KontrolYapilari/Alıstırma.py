# 1. Girilen Saının Asal Olup Olmadığını Bulun

sayi = int(input("Sayı Girin"))
for i in range(2, sayi):
    if sayi % i == 0:
        print(sayi, "Sayısı Asal Değildir")
        break
else:
    print("sayı asaldır")

# 2. Sayı Tahmin Oyunu
import random

sayi = random.randint(1, 100)
print("Sayi :", format(sayi))
hak = 5
while hak > 0:
    tahmin = int(input("Tahmininizi Girin:"))
    if tahmin > sayi:
        print("Daha Küçük Sayı Tahmin edin")
        hak -= 1
        print(f"Kalan Hak :{hak}")
    elif tahmin < sayi:
        print("Daha Büyük Sayı Tahmin Edin")
        hak -= 1
        print(f"Kalan Hak :{hak}")
    else:
        print("Sayıyı Doğru Tahmin Etttiniz")
        print(f"Kalan Hak :{hak}")
        break

# 3. Rakamları Yazıya Çevirme
sayi = "5,324,342"
sayi = sayi.replace(",", "").replace(".", "")
print(sayi)
birler = {"0": "", "1": "Bir", "2": "iki", "3": "üç", "4": "dört", "5": "beş"}
onlar = {"0": "", "1": "on", "2": "yirmi", "3": "otuz", "4": "kırk", "5": "elli"}
Basamak = {"0": "", "1": "Bin", "2": "Milyon"}

while len(sayi) % 3 != 0:
    sayi = "0" + sayi  # başına sıfır eklendi

liste = []
basamak = len(sayi) // 3 - 1
for i in range(0, len(sayi) // 3):
    liste.append(sayi[i * 3 : (i * 3) + 3])

sonuc = ""
for item in liste:
    metin = ""
    if item[0] != "0":
        if item[0] != "1":
            metin = birler[item[0]] + "Yüz"
        else:
            metin = "Yüz"
    metin += onlar[item[1]] + " "
    metin += birler[item[2]] + " "
    liste.index(item)
    sonuc += metin + Basamak[str(basamak)] + " "
    basamak -= 1
print(sonuc)
