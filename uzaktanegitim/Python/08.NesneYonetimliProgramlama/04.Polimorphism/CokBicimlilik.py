"""
miras alan sınıfın, miras alığı sınıfın özelliklerini değiştirerek kullanmasına polimorfisim denir.
"""
# builtin polymorphic function
metin = "python egitimi"
print(len(metin)) # 14
liste = ["1",1,2,3]
print(len(liste)) # 4

# user defined polymorphic function
def fonk(a,b,c=0):
    return a+b+c
print(fonk(1,2)) # 3
print(fonk(1,2,3)) # 6

# Polymorphism with class methods
class Ulke1():
    def yer(self):
        print("Ulke1 Asya Kıtasındadır")
    def nufus(self):
        print("Ulke1 Nufus 200 Milyon")
    
    def type(self):
        print("Federal Cumhuriyet")

class Ulke2():
    def yer(self):
        print("Ulke2 Avrupa Kıtasındadır")
    def nufus(self):
        print("Ulke2 Nufus 50 Milyon")
    def type(self):
        print("Cumhuriyet")

liste = [Ulke1(),Ulke2()]
for item in liste:
    item.yer()
    item.nufus()
    item.type()
"""
Ulke1 Asya Kıtasındadır
Ulke1 Nufus 200 Milyon
Federal Cumhuriyet
Ulke2 Avrupa Kıtasındadır
Ulke2 Nufus 50 Milyon
Cumhuriyet
"""

# Polymorphism with Inheritance
class A:
    def fonk1(self):
        print("A üzerinde calisti")

class B(A):
    def fonk1(self):
        print("B üzerinde calisti")

class C(B):
    def fonk1(self):
        print("C üzerinde calisti")
  
for item in (A(),B(),C()):
    item.fonk1()
"""
A üzerinde calisti
B üzerinde calisti
C üzerinde calisti
"""
