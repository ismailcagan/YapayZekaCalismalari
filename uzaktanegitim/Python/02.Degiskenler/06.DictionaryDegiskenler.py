
# SOZLUK TANIMLAMA
sozluk = {1:"Bir",2:"iki",3:"üç"}
print(type(sozluk)) # <class 'dict'>

## Not -> key kısmında immutable veri tipleri yada sayısal veri tipleri kullanılabilir
sozluk = {[1,2]:"1"}
print(sozluk) # hata

sozluk = {"[1,2]":"1"}
print(sozluk) # {'[1,2]': '1'}

sozluk = {(1,2):"1"}
print(sozluk) # {(1, 2): '1'}

## Not -> value kısmında bütün veri tiplerini kullanabiliriz
sozluk = {"1":[1,2]}
print(sozluk) # {'1': [1, 2]}

# DİCT İÇERİSİNDE ELEMANLARA ERİŞME
sozluk = {1:"Bir",2:"iki",3:"üç"}
# key verdik value aldık
print(sozluk[(1)]) #'Bir'

# DICT İÇERİSİNE YENİ ELEMAN EKLEME
sozluk = {1:"Bir",2:"iki",3:"üç"}
sozluk[4] ="dort"
print(sozluk)

# DICT İÇERİSİNDE ELEMAN SİLMEK
sozluk = {1:"Bir",2:"iki",3:"üç"}
del sozluk[3]
print(sozluk) # {1: 'Bir', 2: 'iki'}

# DICT İÇERİSİNDEN DICT ERİŞİM
sozluk = {1:"bir",2:"iki",3:"üç","alfabe":{"a":"b","c":"d"}}
print(sozluk[3][1]) # ç
print(sozluk["alfabe"]["a"]) # b

# UPDATE FONKSİYONU
sozluk = {1:"Bir",2:"iki",3:"üç"}
sozluk.update({3:"üççç"})
print(sozluk) #{1: 'Bir', 2: 'iki', 3: 'üççç'}

#COPY FONKSİYONU
sozluk = {1:"Bir",2:"iki",3:"üç"}
sozluk2 = sozluk.copy() # birbirinden farklı değişkenler oluşur
print(sozluk2) # {1: 'Bir', 2: 'iki', 3: 'üç'}

#CLEAR FONKSİYONU
sozluk = {1:"Bir",2:"iki",3:"üç"}
sozluk.clear()
print(sozluk) # {}

# ITEMS FONKSİYONU -> sözlüğün içerisindeki verileri key value olarak tuple şeklinde döndürür
sozluk = {1:"Bir",2:"iki",3:"üç"}
print(sozluk.items()) #sozluk = {1:"Bir",2:"iki",3:"üç"}

# KEYS METODU -> Sözlüğün içerisinde sadece keyleri list şek. döndürür
sozluk = {1:"Bir",2:"iki",3:"üç"}
print(sozluk.keys()) #dict_keys([1, 2, 3])

# VALUES METODU -> Sözlüğün içerisinde sadece valueları list şek. döndürür
sozluk = {1:"Bir",2:"iki",3:"üç"}
print(sozluk.values()) #dict_values(['Bir', 'iki', 'üç'])
print(type(sozluk.values())) #<class 'dict_values'>

# POP FONKSİYONU -> belirtilen keye göre silme yapar
sozluk = {1:"Bir",2:"iki",3:"üç"}
sozluk.pop(3)
print(sozluk) #{1: 'Bir', 2: 'iki'}

# POP ITEM FONKSİYONU -> son eleman silinir
sozluk = {1:"Bir",2:"iki",3:"üç"}
sozluk.popitem()
print(sozluk) #{1: 'Bir', 2: 'iki'}

# SET DEFAULT FONKSİYONU -> sonuna değer ekler
sozluk = {1:"Bir",2:"iki",3:"üç"}
sozluk.setdefault(4)
print(sozluk) # {1: 'Bir', 2: 'iki', 3: 'üç', 4: None}

sozluk = {1:"Bir",2:"iki",3:"üç"}
sozluk.setdefault(4,"Dört")
print(sozluk) #{1: 'Bir', 2: 'iki', 3: 'üç', 4: 'Dört'}

# GET FONKSİYONU ->
sozluk = {1:"Bir",2:"iki",3:"üç"}
print(sozluk.get(4)) #None
 
























