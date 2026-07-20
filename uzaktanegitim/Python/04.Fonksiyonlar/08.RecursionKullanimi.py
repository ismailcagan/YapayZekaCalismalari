"""
Recursion FOnksiyon (Özyinelemeli Fonksiyonlar)
"""
def Fonk(metin):
    if len(metin) == 1:
        print(metin)
    else:
        print(metin)
        Fonk(metin[1:])

Fonk("Python")
"""
Python
ython
thon
hon
on
n
"""

def Fonk(metin):
    if len(metin) == 1:
        print(metin)
    else:
        Fonk(metin[1:])
        print(metin)

Fonk("Python")
"""
n
on
hon
thon
ython
Python
"""


# Factoriyel Hesaplama
def Factoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    print(sonuc)
Factoriyel(5)  # 120


def Factoriyel(sayi):
    if sayi == 1:
        return sayi
    else:
        return sayi * Factoriyel(sayi - 1)
print(Factoriyel(5))  # 120


# Girilen Sayıya Kadar Toplama
def Toplama(sayi):
    toplam = 0
    for i in range(1, sayi + 1):
        toplam += i
    print(toplam)
Toplama(11)  # 66


def Toplama(sayi, mevcut, limit):
    if sayi == limit + 1:
        return mevcut
    else:
        print(f"sayi :{sayi},mevcut :{mevcut},sayi + mevcut :{sayi+mevcut}")
        return Toplama(sayi + 1, mevcut + sayi, limit)
print(Toplama(1, 0, 11))  # 66


# Fibonacci Serisi
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def FibonacciYaz(sayi):
    for i in range(1,sayi+1):
        print(i,Fibonacci(i))
        
FibonacciYaz(15)
"""
1 1
2 1
3 2
4 3
5 5
6 8
7 13
8 21
9 34
10 55
11 89
12 144
13 233
14 377
15 610
"""

import sys
print(sys.getrecursionlimit()) # 3000 fonksiyonu içiçeçağırabiliriz


