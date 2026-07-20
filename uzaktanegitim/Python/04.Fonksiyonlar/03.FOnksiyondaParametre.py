# PARAMETRELİ FONKSİYONLAR

# 1.Fonksi. yona Değer Atama
def Fonk(param1):
    print("Merhaba", param1)

Fonk("Python")  # Merhaba Python


# 2. Fonksiyona Birden Fazla Değer Atama
def Fonk1(param1, param2):
    sonuc = param1 + param2
    return sonuc

print(Fonk1(2, 3))  # 5


# 3. Fonksiyonda Parametreye Varsayılan Değer Atama
#Not-> eğer param1'e değer verirsek mecburen param2'ye değer
# vermemiz gerekiyor yoksa syntax hatası alırız
def Fonk2(param1, param2=4):
    sonuc = param1 - param2
    return sonuc

print(Fonk2(5)) #5

# 4.Tanımlandığından FArklı Sıra Parametreye Değer Verme
def Fonk3(param1,param2):
    sonuc = param1*param2
    return sonuc

print(Fonk3(param2=2,param1=4)) # 8
