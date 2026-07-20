# Degisken Tipi Öğrenme
sayi = 1
print(type(sayi))

# Tam sayı
a = 2
b = 3
c = a + b
print(c)

# Ondalıklı sayı
sayi2 = 1.5
print(type(sayi2))
print(sayi2)

d = a/b
print(type(d))
print(d)

# Complex Sayilar (Veri analizinde kullanılır)
sayi3 = 3j
print(type(sayi3))
print(sayi3)

# Metinsel İfadeler
metin = "Ankara"
print(type(metin))
print(metin)

#Farklı Metinsel İfadeleri Tanımlama

metin = r"Ankara'da"
print(metin)

#Hata
metin = "Ankara "Sağuk"

metin = 'Ankara "Soguk"'
print(type(metin))
print(metin)

# Hata
metin = 'Ankara'da "Soguk"

metin = """Ankara'da "soguk" """
print(type(metin))
print(metin)

# Liste
liste =[1,2,3,"a","b","ismail","true",[4,5],(6,7),{1:"Bir"}]
print(liste)
print(liste[9][1]) #Bir

#Tuple
demet = (1,)
print(type(demet)) # tuple

#Sözlük
sozluk = {"book":"kitab","pencil":"kalem"}
print(type(sozluk)) #dict

#Özet
var1 = 1 #int
var2= 1.5 #float
var3 = 1.4j #Komplex
var4 = "Vektörel"
var5 = [1,2,3,4,5] #liste
var6 = (1,2,3,4,5,6) #tıple
var7 = {1:"Bir"} #Sözlük


