# FOR DÖNGÜSÜ

# 1. str Veri Tipi
metin = "python"
for i in metin:
    print(i, end=",")  # p,y,t,h,o,n,

# 2. list Veri Tipi
liste = ["ordu", "samsun", "trabzon"]
for i in liste:
    print(i, end="-")  # ordu-samsun-trabzon-

# 3. dict Veri Tipi
sozluk = {1: "Bir", 2: "iki", 3: "üç"}
for i in sozluk.keys():
    print(i, end="-")  # 1-2-3-
print("\n")
for i in sozluk.values():
    print(i, end="-")  # Bir-iki-üç-
print("\n")
for i in sozluk.keys(), sozluk.values():
    print(i, end="--")  # dict_keys([1, 2, 3])--dict_values(['Bir', 'iki', 'üç'])--
print("\n")
print(sozluk.items())  # dict_items([(1, 'Bir'), (2, 'iki'), (3, 'üç')])
for key, value in sozluk.items():
    print(key, value, end=",")  # 1 Bir,2 iki,3 üç,

# 4.tuple Veri Tipi
demet = {1, 2, 3, 4, 5, 6}
for item in demet:
    print(item, end=",")  # 1,2,3,4,5,6,

# 5.range Fonksiyonu
for i in range(10):
    print(i, end=",")  # 0,1,2,3,4,5,6,7,8,9
print("\n")
for i in range(0, 11, 2):
    print(i, end="-")  # 0-2-4-6-8-10-

# ÖRNEKLER
# 1.girilen sayıya kadar tekmi çiftmi belirtin
sayi = int(input("sayi girin"))
for i in range(sayi + 1):
    if i % 2 == 0:
        print(i, "Çift Sayidir")
    else:
        print(i, "Tek Sayidir")

# 2.Fibonacci Serisi (Kendinden önceki 2 sayının toplamı kendi değerini verir)
a = 1
b = 1
# a = b = 1 # kısaltma
for i in range(0, 10):
    c = a + b
    print(c, end=",")  # 2,3,5,8,13,21,34,55,89,144
    a = b
    b = c
    # a,b = b,c -> kısaltma

# 3. Asal Sayilar Bulma
sayi = int(input("Sayiyi Gir"))
for i in range(2, sayi):
    if sayi % i == 0:
        print("sayi asal değildir")

# 4.Factoriyel Hesaplama
sayi = int(input("Sayiyi Gir"))
fac = 1
for i in range(1, sayi + 1):
    fac *= i
print(fac)
