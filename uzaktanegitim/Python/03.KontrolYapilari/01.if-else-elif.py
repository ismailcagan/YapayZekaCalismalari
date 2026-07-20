Not = int(input("Notu Girin"))
if Not and Not > 0:  # Boş değer veya sıfır değeri kontrol eder
    # Burada Not sıfırdan farklıysa anlamı kattık
    if Not <= 49:
        print("FF")
    elif Not <= 69:
        print("CC")
    elif Not <= 79:
        print("BB")
    elif Not <= 100:
        print("AA")
    else:
        print("Geçerli Not Girin")
else:
    print("Anlamlı değer girin")

# in Kullanımı
liste = [2, 3, 5, 7, 9, 11, 13, 17]
sayi = int(input("Sayi Girin"))
if sayi in liste:
    print(f"{sayi} sayısı listenin içinde")
else:
    liste.append(sayi)
    print(f"{sayi} sayisini listeye ekledim")
print(liste)

metin = "Python öğreniyorum"
if "P" in metin:
    print("P harfi metinin içinde")
else:
    print("belirtilen harf metinde yok")

sozluk = {"book": "kitap", "pencil": "Kalem"}
if "book" in sozluk.keys():
    print("sozlukte var")

# is Kullanımı
# karşılaştırma yaparken değerine ve türüne bakar
a = float("3")
b = 3
if a == b:
    print("a eşittir b")  # a eşittir b
else:
    print("a eşit değil b")

if a is b:
    print("a eşit b")
else:
    print("a eşit değil b")  # a eşit değil b
    

