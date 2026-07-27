
# encapsulation (Kapsülleme ve Erişim Beliteçleri)

class A:
    def __init__(self):
        self.a = "A Class Public"
        self._b = "A Class Protected (Semi private)"
        self.__c = "A Class Private"

class B(A):
    def __init__(self):
        self.d ="B Class public"
        self._e = "B Class Protected (Semi private)"
        self.__f = "B Class Private"
        A.__init__(self)
        
    __f = "Yeni Değiken" # Çalışır Private sadece kendi sınıfı içinde çalışır
    
    print(__f)
Nesne = B()

print(Nesne._e) # B Class Protected
print(Nesne.__f) # hata private değişkenler sadece sınıf içinde çalışır

print(Nesne.a) # A Class Public
print(Nesne._b) # A Class Protected
print(Nesne.__c) # hata çünkü korumalı değişken
print(Nesne.d) # B Class public
