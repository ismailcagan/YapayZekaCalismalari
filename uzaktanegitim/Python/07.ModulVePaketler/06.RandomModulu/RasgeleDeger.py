
import random as rnd

for i in range(5):
    print(rnd.random()) # 0 ile 1 arasında değer üretir
    

for i in range(5):
    print(rnd.randint(1,10)) # 1 ile 10 arasında sayı üretir

for i in range(5):
    print(rnd.randrange(1,11)) # 1 ile 10 arasında değer üretir
    
liste = [rnd.randrange(10) for i in range(5)]
print(liste)


listeSira = [1,2,3,4,5,6,7,8,9,10]
rasgeleListedenElemanSec = rnd.choice(listeSira) # listeden rasgele eleman seçer
print(rasgeleListedenElemanSec)

listeEleman = ["a","b","c","d","e","f"]
rasgeleEleman = rnd.choice(listeEleman)
print(rasgeleEleman)

birdenFazlaElemanSecme = rnd.sample(listeEleman,4) # farklı eleman seçer
print(birdenFazlaElemanSecme)

print(rnd.choices(listeEleman,k=3)) # aynı eleman seçme olasılığı var

