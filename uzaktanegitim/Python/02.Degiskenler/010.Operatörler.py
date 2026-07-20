# OPERATÖRLER

# 1.Aritmetik Operatörler (Dört işlem)
a = 1
b = 2
print(a + b)  # 3  # topla
print(a - b)  # -1  # çıkar
print(a * b)  # 2  # çarp
print(a / b)  # 0.5  # böl
print(a // b)  # 0  # bölüm
print(a % b)  # 1  # mod yada kalan
print(a**b)  # 1  # exponent yada kuvvet

# 2.Karşılaştırma Operatörleri
a = 5
b = 2
print(a == b)  # False  # eşitmi
print(a != b)  # True  # eşit değil mi
print(a < b)  # False  # a küçük b mi
print(a > b)  # True  # a büyük b mi
print(a <= b)  # False  # a küçük eşit b mi
print(a >= b)  # True  # a büyük eşit b mi

# 3.AssignmentOperatörler
a = 4
a += 1
print(a)  # 5
a -= 1
print(a)  # 4
a *= 1
print(a)  # 4
a /= 1
print(a)  # 4.0
a %= 1
print(a)  # 0.0
a //= 1
print(a)  # 0.0
a **= 1
print(a)  # 0.0

# 4.Bitwise Operatörleri
a = 8  # 1000
b = 2  # 0010
print(a & b)  # 0 and
print(a | b)  # 10 or
print(a ^ b)  # 10 xor
print(a << 2)  # 32 sonuna 2 sıfır ekler
print(a >> 2)  # 2 başına 2sıfır ekler sonundaki 2 sıfırı siler
print(~a)  # -9 sonundaki sıfırı bir ile değiştirdi ve eksiyle çarptı

# 5.Logical Operatörleri
a = True
b = False
print(a and b)  # False
print(a or b)  # True
print(not a)  # False

# 6. Identity Operators
a = 2
b = 2.0
print(a == b)  # True
print(a is b)  # False
print(a is not b)  # True

# 7.Membership Operator
liste = [1, 2, 3, 4, 5]
a = 2
print(a in liste)  # True
print(a not in liste)  # False
