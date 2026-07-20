
# SET VERİ TİPİ -> diğer veri tiplerini sırasız olarak tutmaya yarar
kume = {1, 2, 3, "a", "b", 4}
print(type(kume))  # <class 'set'>
print(kume)  # (1, 2, 3, 'a', 'b', 4)

kume = set()  # boş set tanımlama
print(type(kume))  # <class 'set'>

# NOT -> Set veri tipinde elemanlara erişlmez.
# Peki ne için kullanılır. birden fazla veriyi karşılaştırırken kullanabiliriz.
# örneğin aynı 2 csv dosyasından veriyi liste şeklinde çekildiğinde bunları birbiri ile
# karşılaştırma yapmak istediğimizde set veri tipini kullanırız

# ADD FONKSİYONU -> sonuna eleman ekler
kume = {1, 2, 3, "a", "b", 4}
kume.add(4.5)
print(kume)  # {1, 2, 3, 4, 'b', 'a', 4.5}

# CLEAR FONKSİYONU -> Set içinde eleman siler
kume = {1, 2, 3, "a", "b", 4}
kume.clear()
print(kume)  # set()

# COPY FONKSİYONU
kume = {1, 2, 3, "a", "b", 4}
kume2 = kume.copy()
print(kume2)  # {1, 2, 3, 4, 'b', 'a'}
kume.add("2+3j")
print(kume)  # {1, 2, 3, 4, 'b', 'a', '2+3j'}
print(kume2)  # {1, 2, 3, 4, 'b', 'a'}

# UPDATE FONKSİYONU
kume = {1, 2, 3, "a", "b", 4}
kume.update({5, 6})
print(kume)  # {1, 2, 3, 4, 'b', 'a', 5, 6}

kume = {1, 2, 3, "a", "b", 4}
kume2 = {7, 8, 9}
kume.update(kume2)
print(kume)  # {1, 2, 3, 4, 'a', 7, 8, 9, 'b'}


# REMOVE FONKSİYONU
kume = {1, 2, 3, 4, "a", 7, 8, 9, "b"}
kume.remove(9)  # tek değer siler
print(kume)  # {1, 2, 3, 4, 'a', 7, 8, 'b'}


# DİSCARD FONKSİYONU
kume = {1, 2, 3, 4, "a", 7, 8, 9, "b"}
print(kume.discard("i"))  # None
kume.discard(7)
print(kume)  # -> olmayan elemanı hata vermeden none şeklinde geri döner

# NOT -> discard fonksiyonunun remove fonksiyonundan farkı remove fonksiyonu
#       olmayan şeyi silerken hata verir discard    None değerini döner


# POP FONKSİYONU -> ilk elemanı siler
kume = {1, 2, 3, 4, "a", 7, 8, 9, "b"}
kume.pop()
print(kume)  # {2, 3, 4, 'a', 7, 8, 9, 'b'}


# UNION FONKSİYONU -> küme birleşimi
a = {"a", 1, 9, "b"}
b = {"b", 2, 8, "c"}
c = {"c", 3, 7, "d"}
print(a.union(b))  # {1, 2, 'c', 'a', 8, 9, 'b'}
# birden fazla küme birleştirme örneği
# not ->  aynı elemanları sadece bir tanesini alır
print(a.union(b).union(c))  # {1, 2, 'c', 3, 'a', 7, 8, 9, 'b', 'd'}
print(a.union(b.union(c)))  # {1, 'c', 2, 3, 'a', 7, 8, 9, 'b', 'd'}

# INSTERSECTION -> küme kesişimi
b = {"b", 2, 8, "c"}
c = {"c", 3, 7, "d"}
print(b.intersection(c))  # {'c'}

# INSTERSECTION-UPDATE FONKSİYONU
# metodu, iki veya daha fazla kümenin kesişimini (ortak elemanlarını) bulur
# ve sonucu ana kümenin üzerine yazar.
a = {"a", 1, 9, "b"}
b = {"b", 2, 8, "c", 1}
a.intersection_update(b)
print(a)  # {'b', 1}

# İSDİSJOİNT FONKSİYONU
# iki değişkenin ortak elemanı olma durumunu True yada False olarak döndürür
a = {"a", 1, 9, "b"}
b = {"b", 2, 8, "c", 1}
print(a.isdisjoint(b))  # ortak eleman olduğu için false döndü

a = {"a", 1, 9, "b"}
c = {"c", 3, 7, "d"}
print(a.isdisjoint(c))  # ortak eleman olmadığı için false döner

# DİFFERENCE FONKSİYONU -> Küme farkı
a = {"a", 1, 9, "b"}
b = {"b", 2, 8, "c", 1}
print(a.difference(b))  # {9, 'a'}
print(b.difference(a))  # {8, 'c', 2}

# DİFFERENCE-UPDATE -> farkını alır sonucu ana kümeye atar
a = {"a", 1, 9, "b"}
b = {"b", 2, 8, "c", 1}
b.difference_update(a)
print(b)  # {'c', 2, 8}

# İSSUBET -> alt küme
a = {"a", 1, 9, "b"}
b = {"a", 9}
# b anın alt kümesimi
print(b.issubset(a))  # true

# İSSUPERSET -> kapsar
a = {"a", 1, 9, "b"}
b = {"a", 9}
# a kümesi b kümesini kapsıyormu
print(a.issuperset(b))  # True

# FROZEN SET -> dondurulmuş küme
a = {"a", 1, 9, "b"}
FrozenA = frozenset(a)
print(type(FrozenA))  # <class 'frozenset'>
print(FrozenA)  # frozenset({'b', 1, 'a', 9})

# frozenset (Dondurulmuş Küme)Normal kümeler (set) değiştirilebilirdir.
# Yani istediğiniz zaman .add() ile eleman ekler, .remove() ile silersiniz.
# frozenset ise o kümenin üzerine beton dökmek gibidir.
# Küme oluşturulduğu an kilitlenir; artık içine yeni eleman eklenemez,
# var olan eleman silinemez. Sadece okunabilir (salt okunur) hale gelir.
# Neden İhtiyacımız Var?Güvenlik: Kodun ilerleyen kısımlarında yanlışlıkla
# değiştirilmesini istemediğiniz sabit verileri korur (Örn: Haftanın günleri,
# ülkenin şehirleri).Anahtar Yapabilme: Python'da bir sözlüğün (dict) içine anahtar (key)
# olarak normal küme koyamazsınız çünkü küme değişebilir. Ama dondurulmuş bir küme (frozenset)
# değişemediği için sözlüklerde anahtar olarak kullanılabilir.
