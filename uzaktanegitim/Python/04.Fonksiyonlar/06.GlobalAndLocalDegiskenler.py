def Fonk():
    a = 5
    print(a)

Fonk()  # 5
print(a)  # hata alırız çünkü fonksiyonun içinde tanımlandı
# buna local değişken diyoruz
a = 5

def Fonk1():
    print(a)

Fonk1()  # 5
print(a)  # 5 burada çalışır çünkü pragramın genel akışında tanımlandı
# buna global değişkenler denir.

a = 5
def Fonk2():
    a = 4
    print(a)

Fonk2()  # 4
print(a)  # 5

# Dışardaki Değişkeni FOnksiyon İçinde Değiştirme
a = 5
def Fonk3():
    global a
    a = 3
    print(a)
Fonk3() # 3
print(a) # 3

a = 5
def Fonk(a):
    global a # hata sebebi global değişkenler parametre olarak kullanılmaz
    a = a
    print(a)
Fonk3(3)
print(a)

