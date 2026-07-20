# WHILE DONGUSU

liste = ["ordu", "samsun", "giresun", "trabzon"]
say = 0
while say < len(liste):
    print(liste[say])
    say += 1

anahtar = 1
while anahtar == 1:
    giris = int(input("işlem numarası girin"))
    print(giris)
    if giris == 5:
        anahtar = 0
print("işlem bitti")

# sayı tahmin oyunu
import random
sayi = random.randint(1, 100)
tahmin = 0
while tahmin != sayi:
    tahmin = int(input("Tahmininizi Girin"))
    print(tahmin)
    if tahmin < sayi:
        print("Daha Büyük sayi girin")
    elif tahmin > sayi:
        print("Daha Küçük Sayi Girin")
    else:
        print("Doğru Tahmin")
print("Oyun Bitti")
