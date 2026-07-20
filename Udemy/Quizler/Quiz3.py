
#1) Aşağıdaki kodun çıktısı ne olacaktır?
def toplama(a,b):
    print(a,b)
'''
x = toplama(3,4)
print(x)
'''
'\nx = toplama(3,4)\nprint(x)\n'

# cevap --> 3,4 None

#2) Aşağıdaki kodun çıktısı ne olacaktır?
def usselIslem(x=5,y=3):
    print(x ** y)
usselIslem(2,4)
# cevap --> 16 

#3) Aynı fonksiyonu aşağıdaki gibi çağırırsak çıktı ne olur?
usselIslem()
# cevap --> 125

#4) Aşağıdaki kodun çıktısı ne olacaktır?
def myLoop(*args):
    for element in args:
        print(element / 2)
myLoop(3,2,1,5,3,4)
# cevap --> 1.5 - 1.0 - 0.5 - 2.5 - 1.5 - 2.0

#5) Aşağıdaki dizide belirtilen rakamları, myFunction fonksiyonuna tabi tutup, yeni bir dizi oluşturunuz
def myFunc(num):
    return num ** 3
myList = [2,3,4,5,6]

new_dizi =[]
for i in myList:
    new_dizi.append(myFunc(i))
print(new_dizi)


#6) Aşağıdaki string dizisinde, içinde sadece XYZ geçen barkodları gösterecek yeni bir liste oluşturunuz
barkodDizisi = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]

def XYZ(Bdizi):
    new_dizi =[]
    for i in barkodDizisi:
        if "XYZ" in i:
            new_dizi.append(i)
    return new_dizi

print(XYZ(barkodDizisi))


#7) Aşağıdaki kodu okursanız, ornekFonksiyon çalıştırıldığında en altta yazdırılan print size neyi yazdıracaktır?
myVar = "Atil Samancioglu"

def ornekFonksiyon():
    myVar = "Atil"
    
    def digerFonksiyon():
        print(myVar)
    
    digerFonksiyon()
#ornekFonksiyon()
# cevap --> Atil


#8) Aşağıda yazdırılan sınıfı incelediğinizde kedim.yasiCarp() kodunun çıktısı ne olacaktır?
class Kedi():
        
    def __init__(self,isim,yas=5):
        self.isim = isim
        self.yas = yas
        
    def yasiCarp(self):
        return self.yas * 3
kedim = Kedi("Tonton")

#kedim.yasiCarp()
# cevap --> 15


#9) Aşağıdaki kodun çıktısı ne olacaktır?
class Ogrenci():
    
    def __init__(self,isim,sinavNotu):
        self.isim = isim
        self.__sinavNotu = sinavNotu
    
    def notuGoster(self):
        print(f"{self.isim} sınav notu: {self.__sinavNotu}")
ogrenci = Ogrenci("Mehmet",85)
ogrenci.__sinavNotu = 75
#ogrenci.notuGoster()
# cevap --> Mehmet sınav notu: 85


#10) Soyut sınıflar ve methodlar oluşturmamıza olanak tanıyan, kodlarımızı daha planlı şekilde yazmamızı mümkün kılan
# aynı zamanda büyük projelerde bize yapısal olarak fayda sağlayabilecek OOP prensibinin adı nedir?
# cevap --> Soyutlama Prensibi
 