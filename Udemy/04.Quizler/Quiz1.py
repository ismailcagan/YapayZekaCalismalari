
# 1) Asagidaki string'in 5. harfini bir degiskene atayiniz
my_string = "Python Ogreniyorum"
degisken = my_string[4]
print(degisken)

# 2) Asagidaki String'in 5. ve 8. karakteri arasindaki tum harflerini yazdiriniz (5 ve 8 dahil)
my_new_string = "ProgramlamayaMerhabaDedik"
degisken = my_new_string[4:8]
print(degisken)

# 3) Asagidaki String'i kod ile tersten yazin
my_last_string = "Afyonkarahisarlilastiramadiklarimizdanmisiniz"
degisken = my_last_string[::-1]
print(degisken)

# 4) Asagidaki islemin sonucu hangi veri tipinde olacaktir?
4 + 12.2 + 48
print(4+12.2+48)
print(type(4+12.2+48))  # float veri tipinde olacaktır
# 5) Asagidaki islemin sonucu kactir?
5 + 7 * 12
print(5+7*12) # 89

# 6) Bu listeyi en az 2 farkli yoldan olusturunuz: [1,3,"a"]

list1 = [1,2,"a"]
list2 = []
list2.append(1)
list2.append(2)
list2.append("a")
print(list2)

# 7) Asagidaki "b"'yi tek satirda aliniz:
my_list = [3.14,4,[2,3,"b"],True]
new_list = my_list[2][2]
print(new_list)

# 8) Asagidaki "a"'yi tek satirda aliniz:
my_dictionary = {"key1":20.25, "kk2":[40,{"k21":"a"}]}
new_dictionary = my_dictionary["kk2"][1]["k21"]
print(new_dictionary)


# 9) Asagidaki liste set'e cevirilince hangi degerler icinde kalacaktir?
my_list_to_be_set = [3,4,9,3,21,22,4,3,9,10,21,22]
setList = set(my_list_to_be_set)
print(setList) # {3, 4, 9, 10, 21, 22} değerler içinde kalır


# 10) Asagidaki ifadenin sonucu ne olacaktir?
x = 30 * 5 + 3
y = 108 - 2 * 4
x > y
print(x>y) # True

 