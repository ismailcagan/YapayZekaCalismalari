from abc import abstractmethod

class Cokgen:
    
    @abstractmethod
    def KenarSayisi(self):
        pass
    
class Kare(Cokgen):
    def KenarSayisi(self):
        print("4 Kenarım Var")

class Ucgen(Cokgen):
    def KenarSayisi(self):
        print("3 Kenarım Var")

class Besgen(Cokgen):
    def KenarSayisi(self):
        print("5 Kenarım Var")

sekil1 = Kare()
sekil2 = Ucgen()
sekil3 = Besgen()
sekil1.KenarSayisi() # 4 Kenarım Var
sekil2.KenarSayisi() # 3 Kenarım Var
sekil3.KenarSayisi() # 5 Kenarım Var
