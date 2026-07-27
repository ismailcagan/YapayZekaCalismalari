try:
    sayi1 = int(input("1.sayiyi Giriniz"))
    sayi2 = int(input("2.Sayiyi Giriniz"))
    sonuc = sayi1 / sayi2
    print(sonuc)
except BaseException:
    print("Housten We have a problem")

except ZeroDivisionError:
    print("İkinci Değer için Sıfır Girdiniz")

except ValueError:
    print("Sayi Girmeniz Gerekirdi")

except:
    print("Genel Hata")

# ---------------------------------------------------
try:
    sayi1 = int(input("1.sayiyi Giriniz"))
    sayi2 = int(input("2.Sayiyi Giriniz"))

except BaseException:
    print("Housten We have a problem")

except ValueError:
    print("Sayi Girmeniz Gerekirdi")

except:
    print("Genel Hata")

else:
    try:
        sonuc = sayi1 / sayi2
        print(sonuc)

    except ZeroDivisionError:
        print("İkinci Değer için Sıfır Girdiniz")

# ---------------------------------------------------
try:
    sayi1 = int(input("1.sayiyi Giriniz"))
    sayi2 = int(input("2.Sayiyi Giriniz"))

    if sayi2 < 0:
        raise BaseException

except BaseException:
    print("Housten We have a problem")

except ValueError:
    print("Sayi Girmeniz Gerekirdi")

except:
    print("Genel Hata")

else:
    try:
        sonuc = sayi1 / sayi2
        print(sonuc)

    except ZeroDivisionError:
        print("İkinci Değer için Sıfır Girdiniz")
