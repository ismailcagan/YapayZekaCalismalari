def DecoratFonk(fonk):
    
    def icFonk():
        print("Fonksiyon calismadan önce")
        fonk()
        print()
        print("Fonksiyon Calistiktan Sonra")
        
    return icFonk

def Deneme():
    print("Fonksiyon içinde çalıştı")
    
FonkCagir = DecoratFonk(Deneme)
FonkCagir()
        
import time
import math

def hesapZaman(fonk):
    def icFOnk(*args,**kwargs):
        begin = time.time()
        fonk(*args,**kwargs)
        end = time.time()
        print("Bu islem yapılırken gecen zaman:",fonk.__name__,end-begin)
    return icFOnk

def Faktoriyel(param):
    print(math.factorial(param))
Deneme = hesapZaman(Faktoriyel)
Deneme(5)
