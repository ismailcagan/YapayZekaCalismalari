import numpy as np

# 1-) DİZİLER
my_list = [10, 20, 30]
print(type(my_list))  # <class 'list'>

my_numpy_array = np.array(my_list)
print(my_numpy_array)  # [10 20 30]
print(type(my_numpy_array))  # <class 'numpy.ndarray'>

np_max = my_numpy_array.max()  # dizide max elemanı bulur
print(np_max)  # 30

print(np.ones(5))  # [1. 1. 1. 1. 1.]
print(np.zeros(5))  # [0. 0. 0. 0. 0.]
print(np.random.random(5))  # [0.91648711 0.15416318 0.40989828 0.90765993 0.03075442]

# 2-) DİZİ ARİTMETİĞİ

my_list1 = [1, 2]
my_list2 = [2, 3]
print(my_list1 + my_list2)  # [1, 2, 2, 3]

my_numpy_array1 = np.array(my_list1)
my_numpy_array2 = np.array(my_list2)
print(my_numpy_array1 + my_numpy_array2)  # [3 5]
print(my_numpy_array1 * my_numpy_array2)  # [2 6]
print(my_numpy_array1 - my_numpy_array2)  # [-1 -1]
print(my_numpy_array1 / my_numpy_array2)  # [0.5  0.66666667]

print(my_list1 * 5)  # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(my_numpy_array1 * 5)  # [ 5 10]

other_array = np.array([10, 20, 30, 40, 50])
print(other_array.max())  # 50
print(other_array.min())  # 10
print(other_array.sum())  # 150


# 3-) INDEX İŞLEMLERİ
print(list(range(0, 10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(np.arange(0, 10))  # [0 1 2 3 4 5 6 7 8 9]
print(np.arange(0, 20, 2))  # [ 0  2  4  6  8 10 12 14 16 18]

np_array = np.arange(0, 10)
print(np_array)  # [0 1 2 3 4 5 6 7 8 9]
print(np_array[0])  # 0
print(np_array[-1])  # 9
print(np_array[1:4:])  # [1 2 3]
print(np_array[::-1])  # [9 8 7 6 5 4 3 2 1 0]

# random
print(np.random.randint(1, 300, 5))  # [134  56 146  58 257]
print(np.random.randn(4, 4))  # belirtilen sayı kadar matriks üretir
"""
[[-0.10881343  0.25834733 -0.37997495 -2.35123927]
 [-1.72823413 -0.72086322 -0.63216979 -1.10521336]
 [-0.75322783  0.10235678  1.12254232 -0.55425105]
 [ 0.34459514 -1.19239492  1.71925785 -1.37068431]]
"""

# 4-) MATRİXLER
my_matriks = [[5, 10], [15, 20]]
print(my_matriks)  # [[5, 10], [15, 20]]
print(my_matriks[0])  # [5, 10]
print(my_matriks[0][0])  # 5

# Matriksler row ve column
numpy_matriks = np.array([[5, 10], [15, 20]])
print(numpy_matriks)
"""
[[ 5 10]
 [15 20]]
"""
print(numpy_matriks[1, 0])  # 15
print(numpy_matriks.sum())  # 50
print(np.ones((4, 3)))
"""
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
"""
print(np.zeros((3, 3)))
"""
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
"""
print(np.random.random((4, 2)))
"""
[[0.05819298 0.41941407]
 [0.92132472 0.99869461]
 [0.94130392 0.43034968]
 [0.54620414 0.24421435]]
"""

# 5-) MATRİX ARİTMETİĞİ
first_array = np.array([[10, 20], [30, 40]])
second_array = np.array([[5, 15], [25, 35]])
print(first_array + second_array)
"""
[[15 35]
 [55 75]]
"""
third_array = np.array([[50, 60]])
print(second_array + third_array)
"""
[[55 75]
 [75 95]]
"""

fourth_array = np.array([[10, 20, 30, 40, 50]])
print(second_array + fourth_array)  # hata

print(first_array.shape)  # (2, 2)
print(second_array.shape)  # (2, 2)
print(third_array.shape)  # (1, 2)
print(fourth_array.shape)  # (1, 5)

# 6-) MATRİX ÇARPIMLARI
first_array = np.array([[10, 20], [30, 40]])
second_array = np.array([[5, 15], [25, 35]])
print(first_array * second_array)

# dot product
# dot product yapabilmek için brinci matisin sütunu ile ikinci
# satırın kolonu eşit olmak zorundadır
first_array = np.array([[10, 20, 30]])
second_array = np.array([[2, 3], [4, 5], [6, 7]])
print(first_array.shape)  # (1, 3)
print(second_array.shape)  # (3, 2)

dotCarpim = first_array.dot(second_array)
print(dotCarpim)  # [[280 340]]
print(dotCarpim.shape)  # (1, 2)

# 7-) örnekler

new_array = np.random.randint(1, 100, 20)
print(new_array)  # [62 35 14 22 12 68 47 12 18 64 47 38 48 42  6 18 72 99 33 99]

print(new_array > 25)
"""
[ True  True False False False  True  True False False  True  True  True
  True  True False False  True  True  True  True]
"""
print(new_array[new_array > 25])  # [62 35 68 47 64 47 38 48 42 72 99 33 99]

# transpoze & reshape

matrix_array = np.array([[10, 20], [30, 40], [50, 60]])
print(matrix_array)
"""
[[10 20]
 [30 40]
 [50 60]]
"""
print(matrix_array.shape)  # (3, 2)

transpoz_matrix = matrix_array.transpose()
print(transpoz_matrix)
"""
[[10 30 50]
 [20 40 60]]
"""
print(transpoz_matrix.shape)  # (2, 3)

random_array = np.random.random((6, 1))
print(random_array)
"""
[[0.09329765]
 [0.30257626]
 [0.79489067]
 [0.26702176]
 [0.3197102 ]
 [0.04130694]]
"""
print(random_array.shape)  # (6, 1)
print(random_array.reshape(2, 3))
"""
[[0.09329765 0.30257626 0.79489067]
 [0.26702176 0.3197102  0.04130694]]
"""

# z-score hesaplama

data = np.array([10, 12, 13, 15, 18, 25, 100, 105])

# outlier
mean = np.mean(data)  # ortalama hesaplar
print(mean)  # 37.25

std = np.std(data)  # standart sapmayı hesaplar
print(std)  # 37.9333296719389

z_score = (data - mean) / std
print(z_score)
"""
[-0.71836562 -0.66564154 -0.6392795  -0.58655542 -0.50746929 -0.322935
  1.65421809  1.78602829]
"""
print(
    z_score[z_score > 1]
)  # [1.65421809 1.78602829] -> z scorunda 1 den büyük olanları getir
print(
    data[z_score > 1]
)  # [100 105] -> data nın içinde z-score 1 den büyük olanları getir

# math equations

# 2x + 3y = 8 and 5x + 7y = 19

# coefficient
A = np.array([[2,3],[5,7]])
# constant
B = np.array([8,19])

solution = np.linalg.solve(A,B)
print(solution) # [1. 2.]
"""
x => 1 
y => 2
"""














