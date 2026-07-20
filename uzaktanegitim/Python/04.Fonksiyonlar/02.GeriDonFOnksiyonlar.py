# return and yield

"""
 return -> değer gönderirken birden fazla değer gönderebilir
            tek değer gönderirken kendi veri tipinde gönderir
            birden fazla değer gönderdiğinde tipi tupleolur
yield -> generite bir fonksiyondur,sıralı veri göndermek için kullanırız
"""

# 1.Fonksiyon Tanımlama
def Fonksiyon():
    print("merhaba")

Fonksiyon() #merhaba
print(type(Fonksiyon())) # <class 'NoneType'>

# 2.Geri Tek Değer Döndüren FOnksiyon
def Fonk2():
    sonuc = 2 + 5
    return sonuc

print(Fonk2()) # 7
print(type(Fonk2())) # <class 'int'>
sayi = Fonk2()
islem = sayi + 7
print(islem) # 14
print(type(islem)) #<class 'int'>

# 3.Geriye Birden Fazla Değer Gönderen Fonksiyon
def Fonk3():
    sonuc = 2+5
    return sonuc,"sonuc"
print(Fonk3()) # (7, 'sonuc')
print(type(Fonk3())) # <class 'tuple'>

# 4.Yield
def Fonk4():
    liste =[1,2,3,4,5,6,"Ordu","İsmail"]
    for i in liste:
        yield i

for i in Fonk4():
    print(i,end="-") # <class 'tuple'>
print(type(Fonk4())) # <class 'generator'>











