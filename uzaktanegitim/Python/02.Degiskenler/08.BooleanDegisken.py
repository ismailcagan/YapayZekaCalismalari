
# < operatörü
a = 2
b = 3
print(type(a<b)) # <class 'bool'>
print(a<b) # True

# == operatörü
# == operatörü: Nesnelerin içeriğinin (değerinin) aynı olup olmadığına bakar.
a = 1
b = 1
print(a == b) # True

liste1 = [1, 2, 3]
liste2 = [1, 2, 3]
print(liste1 == liste2) #True


# is operatörü
# is operatörü: Nesnelerin kimliğinin (hafıza adresinin) aynı olup olduğuna bakar. 
# "Bu iki değişken tamamen aynı nesne mi?" sorusunu sorur.
a = 2
b = 2
print(a is b) # true

liste1 = [1, 2, 3]
liste2 = [1, 2, 3]
print(liste1 is liste2) # False

# is Operatörü Gerçek Hayatta En Çok Nerede Kullanılır?Python'da 
# is operatörünün en doğru ve en yaygın kullanım alanı None kontrolü yapmaktır. 
# Bir değişkenin boş veya tanımsız olup olmadığını kontrol ederken her zaman 
# is None veya is not None kalıbı kullanılır:

#kullanici_adi = None
#if kullanici_adi is None:
#    print("Lütfen bir kullanıcı adı girin.")


