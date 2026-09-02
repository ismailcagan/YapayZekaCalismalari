# 1) Aşağıdaki kodun çıktısı ne olacaktır?
x = 5
y = 3
z = 6
x > y and z > x

# cevap --> True

# 2) Aynı değerlerle kod şu şekilde değiştilirse çıktı ne olacaktır?
x < y or z > y 

# cevap --> True 

# 3) Aşağıdaki kodun çıktısı ne olacaktır?
'''
yas = 20

if yas < 18:
    print("18 yaşından küçüksünüz")
elif yas >= 18 and yas < 30:
    print("18 ile 30 yaş arasında bir gençsiniz")
elif yas >= 30 and yas < 40:
    print("30 ve 40 arasına gelmişsiniz")
else:
    print("40 yaşından daha büyüksünüz")
'''
'\nyas = 20\n\nif yas < 18:\n    print("18 yaşından küçüksünüz")\nelif yas >= 18 and yas < 30:\n    print("18 ile 30 yaş arasında bir gençsiniz")\nelif yas >= 30 and yas < 40:\n    print("30 ve 40 arasına gelmişsiniz")\nelse:\n    print("40 yaşından daha büyüksünüz")\n'
# cevap --> "18 ile 30 yaş arasında bir gençsiniz"

#4) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}

for key,value in my_dictionary.items():
    if(value == "c"):
        print("c harfi geçiyor")


#5) Aşağıdaki sözlükte, anahtarlar içinde a harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}

for key,value in my_other_dictionary.items():
    if key == "a":
        print("a harfi geçiyor")


#6) Aşağıdaki listedeki sayılardan sadece çift sayı olanları yazdıran bir kod yazınız.
my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]

for i in my_numbers:
    if i%2==0:
        print(i)

#7) Aşağıdaki listedeki sayılar bir dairenin yarı çapını vermektedir. 
#Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.
r_list = [3,2,5,8,4,6,9,12]

cevreListe = []
pi = 3.14
for i in r_list:
    cevre = i*pi*2
    cevreListe.append(cevre)
print(cevreListe)

#8) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur.
# Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.
age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
yas = []
for i in age_name_list:
    adi,yasi = i
    yas.append(yasi)
print(yas)


#9) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız
metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]

import random
rasgele = random.randint(0,len(metal_list)-1)
grup = metal_list[rasgele]
print(grup)

#10) Aşağıdaki kodun çıktısı ne olacaktır?
number_list = [5,7,18,21,20,10,405,24]
[num % 2 == 0 for num in number_list]

# cevap -> [False, False, True, False, True, True, False, True]