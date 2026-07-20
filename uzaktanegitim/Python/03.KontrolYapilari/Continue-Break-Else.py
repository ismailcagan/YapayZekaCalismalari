# break -> DÖngüyü durdur
while True:
    sayi = int(input("Sayi Girin"))
    print(sayi)
    if sayi == 5:
        break
    print("DÖngü Devam Ediyor")
print("Program Devam Ediyor")


# Countinue -> Altındaki kodları çalıştırma
sayi = 0
while sayi < 6:
    if sayi == 3:
        sayi += 1
        continue
    else:
        print(sayi)
        sayi += 1


while True:
    sayi = int(input("Sayi Girin :"))
    if sayi == 3:
        continue
    elif sayi == 5:
        break
    print(sayi)

# else ->
sayi = 0
while sayi < 6:
    sayi += 1
    print(sayi)
else:
    print("İşlem Bitti")
print("Program Devam Ediyor")

sayi = 0
while sayi < 3:
    sayi += 1
    print(sayi)
else:
    print("Döngü break olmadan, başarıyla tamamlandı!")
""" 
1
2
3
Döngü break olmadan, başarıyla tamamlandı!
"""

sayi = 0
while sayi < 3:
    sayi += 1
    if sayi == 2:
        print("Döngü yarıda kesildi!")
        break  # Döngüyü aniden bitirir
    print(sayi)
else:
    print("Bu yazı asla görünmeyecek.")
"""
1
Döngü yarıda kesildi!
"""

for i in range(0,7):
    print(i)
else:
    print("İşlem Bitti")
print("Program Bitti!")