# DEĞER DÖNÜŞÜMLERİ

# 1.Kapalı Değer Dönüşümü
print("Sayı :", 4)  # Sayı : 4

a = 5
b = 3.4
print(a + b)  # 8.4

# 2.Açık Değer Dönüşümleri
# 2.1. int Dönüştürme
var1 = int("5")
print(type(var1))  # <class 'int'>

var1 = int(input("Sayıyı Giriniz :"))
print(type(var1))  # <class 'int'>

# 2.2. float Dönüştürme
var1 = "5.5"
var2 = 5
print(float(var1))  # 5.5
print(float(var2))  # 5.0
print(int(var1))

# 2.3. Complex Değere Dönüştürme
var1 = complex("2")
print(var1)  # (2+0j)
print(type(var1))  # <class 'complex'>

# 2.4. Str değerine Dönüştürme
var1 = str(5) + "a"
print(var1)  # 5a
print(type(var1))  # <class 'str'>

# 2.5 repr(a) Dönüştürme
print(repr([1, 2, 3, 4]))  # [1, 2, 3, 4]

# 2.6 eval(str) Dönüştürme
print(eval("5" + "2"))  # 7

# 2.7. set(a) Dönüştürme
liste = [1, 2, 3, 4]
setDonusturme = set(liste)
print(setDonusturme)  # {1, 2, 3, 4}
print(type(setDonusturme))  # <class 'set'>

# 2.8. tuple(a) Dönüştürme
metin = "python"
demet = tuple(metin)
print(type(demet))  # <class 'tuple'>
print(demet)  # ('p', 'y', 't', 'h', 'o', 'n')

# 2.9 list(a) Dönüştürme
metin = "python"
liste = list(metin)
print(type(liste))  # <class 'list'>
print(liste)  # ['p', 'y', 't', 'h', 'o', 'n']

# 2.10.dict(d) Dönüştürme
liste = [(1, "Bir"), (2, "İki")]
dictt = dict(liste)
print(type(dictt))  # <class 'dict'>
print(dictt)  # {1: 'Bir', 2: 'İki'}

# 2.11. frozenset(s) Dönüştürme
sozluk = {1: "Bir", 2: "İki"}
frozen = frozenset(sozluk)
print(type(frozen))  # <class 'frozenset'>
print(frozen)  # frozenset({1, 2})

# 2.12. chr(x) Dönüştürme
a = 65
print(type(a))  # <class 'int'>
print(chr(a))  # A

# 2.13. ord(x) Dönüştürme
metin = "A"
print(type(ord(metin)))  # <class 'int'>
print(ord(metin))  # 65

# 2.14. hex(x) Dönüştürme
sayi1 = 65
print(type(hex(sayi1)))  # <class 'str'>
print(hex(sayi1))  # 0x41

# 2.15. oct(x) Dönüştürme
sayi = 68
donus = oct(sayi)
print(donus)  # 0o104
donusum = int(donus, 8)  # 68
print(donusum)

# 2.16. Bin(x) Dönüştürme
sayi = 5
donus = bin(sayi)
print(donus)  # 0b101
donusum = int(donus, 2)
print(donusum)  # 5
