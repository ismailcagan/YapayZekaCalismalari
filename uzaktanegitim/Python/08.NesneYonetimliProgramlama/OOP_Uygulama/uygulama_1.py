class MarvelHero:

    def __init__(self, saglik, guc, isim):
        self.saglik = saglik
        self.guc = guc
        self.isim = isim

    def Vurus(self):
        return self.guc

    def Darbe(self, guc):
        self.saglik -= guc
        return self.saglik


class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__(500, 50, "DeadPool")
        self.super = 0

    def Darbe(self, guc):
        self.super += 1
        if self.super == 3:
            self.saglik += 100
        else:
            self.saglik -= guc
        return self.saglik


class Hulk(MarvelHero):
    def __init__(self):
        super().__init__(750, 100, "Hulk")
        self.super = 0

    def Vurus(self):
        self.super += 1
        if self.super == 5:
            self.super = 0
            return self.guc * 2
        else:
            return self.guc
        
class IronMan(MarvelHero):
    def __init__(self):
        super().__init__(750, 50, "Ironman")

class KaptanAmerika(MarvelHero):
    def __init__(self):
        super().__init__(500, 75, "KaptanAmerica")     


import random as rnd
import time
liste = [Hulk,DeadPool,IronMan,KaptanAmerika]
player1 = rnd.choice(liste)()
player2 = rnd.choice(liste)()
print(player1.isim)
print(player2.isim)

print(f"Player1 için {player1.isim} Seçildi \nPlayer2 için {player2.isim}")

while player1.saglik > 0 and player2.saglik > 0:
    time.sleep(1)    
    player2.Darbe(player1.Vurus())
    print(f"{player1.isim} ==> {player2.isim} vurdu ==> {player1.isim}:{player1.saglik} ve {player2.isim}:{player2.saglik}")
    time.sleep(1)
    player1.Darbe(player2.Vurus())
    print(f"{player2.isim} ==> {player1.isim} vurdu ==> {player1.isim}:{player1.saglik} ve {player2.isim}:{player2.saglik}")
else:
    if player1.saglik>player2.saglik:
        print(player1.isim,"Kazandı")
    else:
        print(player2.isim,"Kazandı")
    print("Oyun Bitti")