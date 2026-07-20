class A():
    def __init__(self):
        self.a = "A sınıfına ait örnek özellik"

class B(A):
    def __init__(self):
        self.b = "B Sınıfına ait örnek özellik"

bSinifi = B()
bSinifi.a # AttributeError: 'B' object has no attribute 'a'
# hata alınır çünkü a özelliği A sınıfının constructırında yer alır
#-----------------------------------------------------------

class A():
    def __init__(self):
        self.a = "A sınıfına ait örnek özellik"
        
    def SoyleA(self):
        print("Soyle A çalisti")

class B(A):
    def __init__(self):
        self.b = "B Sınıfına ait örnek özellik"
    
bSinifi = B()
bSinifi.SoyleA() # Soyle A çalisti
#çalışır kalıtım alındı A sınıfında sadece metot erişildi
#-------------------------------------------------------------

class A():
    def __init__(self):
        self.a = "A sınıfına ait örnek özellik"
        
    def SoyleA(self):
        print("Soyle A çalisti")

class B(A):
    def __init__(self):
        super().__init__()
        print(self.a)
        self.b = "B Sınıfına ait örnek özellik"
        
bSinifi = B()
bSinifi.a # A sınıfına ait örnek özellik
bSinifi.b # 'B Sınıfına ait örnek özellik'

# çalışır çünkü kalıtım alınan sınıfa 
# super() metodu ile üst sınıfın constructırına erişim sağlanır
#---------------------------------------------------------------

class A():
    def __init__(self):
        self.a = "A sınıfına ait özellik"

class B():
    def __init__(self):
        self.b = "B Sınıfına ait özellik"

class C(A,B):
    def __init__(self):
        super().__init__()
        self.a
        self.c = "C Sınıfına ait özellik"

cSinifi = C()
print(cSinifi.a) # A sınıfına ait özellik
cSinifi.c # 'C Sınıfına ait özellik'

# C sınıfına 2 tane kalıtım alındı, burada dikkat edilmesi gereken konu;
# super() metodu ile kalıtım alınan sınıfın Constructor ulaşıldığında
# C Sınıfı tanımlanırken parantesine ilk yazılan sınıfın Constructorına ulaşılabilir
# Peki diğer sınıflara ulaşmak için ne yapmamız gerekiyor Super() metodu yerine
# sınıfların adını yazmamız gerekiyor
#--------------------------------------------------------------------
class A():
    def __init__(self):
        self.a = "A sınıfına ait özellik"

class B():
    def __init__(self):
        self.b = "B Sınıfına ait özellik"

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.a
        self.b
        self.c = "C Sınıfına ait özellik"

cSinifi = C()
print(cSinifi.a) # A sınıfına ait özellik
print(cSinifi.b) # B sınıfına ait özellik
print(cSinifi.c) # C sınıfına ait özellik
# çalıştı sınıfların adlarını yazdık
#-----------------------------------------------------------------------------

class A():
    def __init__(self):
        self.a = "A sınıfına ait özellik"

class B():
    def __init__(self):
        self.b = "B Sınıfına ait özellik"

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.a
        self.b
        self.c = "C Sınıfına ait özellik"

class D(C):
    def __init__(self):
        super().__init__()

dSinifi = D()
print(dSinifi.a) # A sınıfına ait özellik
print(dSinifi.b) # B sınıfına ait özellik
print(dSinifi.c) # C sınıfına ait özellik
# D sınıfı C sinifinda kalıtım alıyor C sınıfıda A ve B sınıfından 
# kalıtım aldığı için D sınıfında A,B ve C sınıflarına erişim sağlayabilirim
#-----------------------------------------------------------------------

class A():
    def __init__(self):
        self.a = "A sınıfına ait özellik"

class B():
    def __init__(self):
        self.b = "B Sınıfına ait özellik"

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.a
        self.b
        self.c = "C Sınıfına ait özellik"

class D(C):
    def __init__(self):
        super().__init__()

aSinifi = A()
bSinifi = B()
cSinifi = C()
dSinifi = D()

print(isinstance(dSinifi,A)) # True (D sınıfı A sınıfına Erişim Sağlıyormu)

print(issubclass(C,A)) # True (C sınıfı A sınıfının Alt nesnesimi)




















