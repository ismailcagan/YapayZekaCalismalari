
liste = []
print(type(liste))  # <class 'list'>

liste = [1, 2, "3", (1, 2), [1, 2, 3, 4]]
print(type(liste))  # <class 'list'>
print(len(liste))  # 5


liste = [[1, 2, 3], [4, 5, 6]]  # 2 boyutlu liste
liste2 = [[[1, 2], [3, 4]], [5, 6], [7, 8]]  # 3 boyutlu liste

# bütün veri tiplerini listede tutabiliriz
liste = [1, 1.5, 1.5j, [1, 3], (1, 2), {1: "a"}]
print(liste)  # [1, 1.5, 1.5j, [1, 3], (1, 2), {1: 'a'}]

# listenin indislerine erişme
liste = [1, 2, 3, 4, 5, 6, 7]
metin = "1,2,3,4,5,6,7"
print(liste[3])  # 4
print(metin[5])  # ,

# listeye eleman ekleme
liste = []
# 1. Yöntem
liste.append("1")
liste.append("a")
liste.append(5)
# 2.Yöntem
liste += [1.5]
print(liste)  # ['1', 'a', 5, 1.5]

# 2 LİSTEYİ BİRLEŞTİRME
liste = [1, 2, 3, 4, 5, 6, 7]
liste2 = [8, 9, 10]

liste = liste + liste2
print(liste)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# LİSTEDEN ELEMAN SİLME
liste = [1, 2, 3, 4, 5, 6, 7]
del liste[2]
print(liste)  # [1, 2, 4, 5, 6, 7]


# LİSTE FONKSİYONLARI

# EKleme
liste = ["Elma", "Peynir", "Zeytin"]
liste.append("Sucuk")  # Sonuna Eleman Ekliyor
print(liste)  # ['Elma', 'Peynir', 'Zeytin', 'Sucuk']

liste.insert(0, "Ekmek")  # indisnumarasını belirtiyoruz
print(liste)  # ['Ekmek', 'Elma', 'Peynir', 'Zeytin', 'Sucuk']

# Silme
liste = ["Elma", "Peynir", "Zeytin"]
# print hangi elemanın silindiğini gösterir
# not -> pop() içine birşey yazmazsak sondan eleman çıkarır
print(liste.pop(1))  # Peynir
print(liste)  # ['Elma', 'Zeytin']

liste = [1, 2, 3, 4, 5, 1, 2, 3, 1, 1, 4, 5]
# değerin adı verilerek silme işlemi yapar
liste.remove(1)  # ilk bulduğu 1 değerini siler
liste.remove(1)  # 2. kez çalıştırıldığında yine ilkbulduğu 1 değerini siler
print(liste)  # [2, 3, 4, 5, 2, 3, 1, 1, 4, 5]

# Extend (Listeyi genişletme)
liste = [1, 2, 3]
liste2 = [4, 5, 6, 7, 8, 9]
liste.extend(liste2)
print(liste)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Sort (Sıralama)

liste = [4, 2, 9, 3, 7, 8, 10, 52, 68, 1, 43, 32, 100]
liste.sort()
print(liste)  # [1, 2, 3, 4, 7, 8, 9, 10, 32, 43, 52, 68, 100]

liste = ["Işınsu", "Ahmet", "Çağrı", "Çiğdem", "Hülagü", "Şirin", "Sevim"]
liste.sort()
print(liste)  # ['Ahmet', 'Hülagü', 'Işınsu', 'Sevim', 'Çağrı', 'Çiğdem', 'Şirin']
# burada dikkat edilmesi gereken string ifadelerde sıralama yaparken türkçe karakterler dikkate alınmaz ingilizce karakterler dikkate alınır

# Reverse (Diziyi ters çevirme)
liste = ["Işınsu", "Ahmet", "Çağrı", "Çiğdem", "Hülagü", "Şirin", "Sevim"]
liste.reverse()
print(liste)  # ['Sevim', 'Şirin', 'Hülagü', 'Çiğdem', 'Çağrı', 'Ahmet', 'Işınsu']

# Count (Belirtilen elemanın liste içinde kaç tane olduğunu söyler)
liste = ["Işınsu", "Ahmet", "Çağrı", "Çiğdem", "Hülagü", "Şirin", "Sevim", "Şirin"]
listeCount = liste.count("Şirin")
print(listeCount)  # 2

# Clear (listenin bütün elemanlarını siler)
liste = ["Işınsu", "Ahmet", "Çağrı", "Çiğdem", "Hülagü", "Şirin", "Sevim", "Şirin"]
liste.clear()
print(liste)  # []

# Index (Girlen değerin bulunduğu en düşük indes numarasını verir)
liste = ["Işınsu", "Ahmet", "Çağrı", "Çiğdem", "Hülagü", "Şirin", "Sevim", "Şirin"]
print(liste.index("Şirin"))  # 5

# Copy ()
liste = [1, 2, 3]
liste2 = liste
liste2[1] = 25
print(liste)  # [1, 25, 3]


liste = [1, 2, 3]
liste2 = liste.copy()
liste2[1] = 25
print(liste) #[1, 2, 3]