""" Lambda -> tek satırda fonksiyon oluşturmak için kullanırız karmaşık işlemleri yapamayızGenelde tek satırda yapılacak işlemleri hallederiz """
def Topla(x, y):
    return x + y

print(Topla(2, 3))  # 5

Fonk = lambda x: x + x
print(Fonk(2))  # 4

Fonk1 = lambda x, y: x + y
print(Fonk1(2, 3))  # 5

Fonk2 = lambda x, y, z: x + y + z
print(Fonk2(2, 3, 4))  # 9

Fonk3 = lambda x, y, z=5: x + y + z
print(Fonk3(2, 3))  # 10

sonuc = (lambda x, y, z=3: x + y + z)(1, 2)
print(sonuc)  # 6

Toplam = lambda *args: sum(args)
print(Toplam(1, 2, 3, 4))  # 10

Toplam = lambda **kwargs: sum(kwargs.values())
print(Toplam(a=1, b=2, c=3))  # 6

liste = ["Ahmet","Mehmet","Veli","Çiğdem","Işıl","Şermin"]
liste.sort()
print(liste) # ['Ahmet', 'Işıl', 'Mehmet', 'Veli', 'Çiğdem', 'Şermin']

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
cevrim = {alfabe[i]:i for i in range(len(alfabe))}
print(cevrim)
#cevrim1 = {item:alfabe.index(item) for item in alfabe}
sorted(liste,key=lambda x:cevrim.get(x[0].lower())) # ['Ahmet', 'Çiğdem', 'Işıl', 'Mehmet', 'Şermin', 'Veli']


def Fonk(a,b):
    c = 3
    return (lambda a,b,c:a+b+c)(a,b,c)
Fonk(1,2) # 6
