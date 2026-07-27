"""
Python'da Generators (Üreteçler), bellekte (RAM) yer kaplamadan sırayla veri üretmenizi 
sağlayan çok güçlü ve performans dostu yapılardır.Büyük veri setleriyle çalışırken 
bilgisayarınızın kilitlenmesini önlerler.Generator Nedir?Normal fonksiyonlar return ile 
tek bir değer döndürür ve biter. Generator fonksiyonları ise yield anahtar kelimesini kullanır. 
Değer döndürür ama kaldığı yeri unutmaz, çağrıldıkça sıradaki veriyi verir.
Generator Neden Kullanılır?Bellek (RAM) Dostudur: 1 milyon elemanlı bir liste bellekte devasa yer kaplarken, 
generator sadece sonraki elemanı üretecek formülü saklar.
Performans Artırır: Verilerin tamamının işlenmesini beklemezsiniz. 
İhtiyacınız olan eleman anında üretilir.
Sonsuz Döngüler: Teorik olarak sonsuza kadar giden veri akışları (örneğin sürekli akan bir sensör verisi) oluşturabilirsiniz.
"""
import math
def GeneratFonk(a):
    i = 0
    while i <= a:
        yield math.factorial(i)
        i += 1

for j in GeneratFonk(5):
    print(j)
"""
1
1
2
6
24
120
"""

#----------------------------------------------------------

import random as rnd
def GenerateFonk():
    liste = [i for i in range(1,51)]
    sonuc = rnd.sample(liste,6)
    for i in sonuc:
        yield i

for j in GenerateFonk():
    print(j)
"""
32
25
20
49
13
28
"""
#---------------------------------------------------------------

import random as rnd
def GenerateFonk():
    liste = [i for i in range(1,51)]
    sonuc = rnd.sample(liste,6)
    for i in sonuc:
        yield i

def LotoOyna(kolonSayisi=1):
    for i in range(kolonSayisi):
        liste=[]
        for j in GenerateFonk():
            liste.append(j)
        liste.sort()
        yield liste

for kolon in LotoOyna(5):
    print(kolon)
"""
[23, 27, 32, 45, 47, 50]
[10, 22, 30, 35, 36, 45]
[2, 5, 16, 19, 35, 48]
[25, 27, 28, 29, 39, 44]
[1, 3, 15, 42, 47, 48]
"""
#-------------------------------------------------------

def GenFonk():
    yield 1
    yield 2
    yield 3

x = GenFonk()
print(x.__next__())
print(x.__next__())
print(x.__next__())
"""
1
2
3
"""




