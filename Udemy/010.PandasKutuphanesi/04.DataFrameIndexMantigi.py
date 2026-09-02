import numpy as np
import pandas as pd

data = np.random.randn(4, 3)
print(data)

data_frame = pd.DataFrame(data)
print(data_frame)

print(type(data_frame))  # <class 'pandas.DataFrame'>

print(type(data_frame[0]))  # <class 'pandas.Series'>

new_df = pd.DataFrame(
    data,
    index=["Atil", "Zeynep", "Atlas", "Mehmet"],
    columns=["Salary", "Age", "Seniority"],
)

print(new_df)

new_df.loc["Atlas", "Salary"] = 100
print(new_df)
"""
            Salary       Age  Seniority
Atil      0.428361  1.358150  -0.224928
Zeynep    1.650644  0.959427   0.005092
Atlas   100.000000  0.008241  -0.528537
Mehmet    1.302456  0.551723   0.828773
"""

print(new_df.reset_index())
"""
# İNDEX HALİNDE YAZDI
    index      Salary       Age  Seniority
0    Atil    0.428361  1.358150  -0.224928
1  Zeynep    1.650644  0.959427   0.005092
2   Atlas  100.000000  0.008241  -0.528537
3  Mehmet    1.302456  0.551723   0.828773
"""

reset_frame = new_df.reset_index()
print(reset_frame)
"""
    index      Salary       Age  Seniority
0    Atil    0.428361  1.358150  -0.224928
1  Zeynep    1.650644  0.959427   0.005092
2   Atlas  100.000000  0.008241  -0.528537
3  Mehmet    1.302456  0.551723   0.828773
"""
print(reset_frame.loc["Atil"])  # hata çümkü indexler oluştu

print(reset_frame.loc[0])
"""
index            Atil
Salary       0.428361
Age           1.35815
Seniority   -0.224928
Name: 0, dtype: object
"""

# Yeni Colon ve Colona Veri Ekleme
new_indices = ["A1", "A2", "A3", "A4"]
new_df["NewIndexCol"] = new_indices
print(new_df)
"""
            Salary       Age  Seniority NewIndexCol
Atil      0.428361  1.358150  -0.224928          A1
Zeynep    1.650644  0.959427   0.005092          A2
Atlas   100.000000  0.008241  -0.528537          A3
Mehmet    1.302456  0.551723   0.828773          A4
"""

# Sütunu İndeks Yapma
new_df.set_index("NewIndexCol", inplace=True)
print(new_df)
"""
                 Salary       Age  Seniority
NewIndexCol                                 
A1             0.428361  1.358150  -0.224928
A2             1.650644  0.959427   0.005092
A3           100.000000  0.008241  -0.528537
A4             1.302456  0.551723   0.828773
"""

print(new_df.loc["A1"]) # Yeni indekse göre veri çağrıldı
"""
Salary       0.428361
Age          1.358150
Seniority   -0.224928
Name: A1, dtype: float64
"""

# multi index(Birden fazla index)

first_index = ["Simpson","Simpson","Simpson","South Park","South Park","South Park"]

inner_index = ["Homer","Bart","Marge","Cartman","Kenny","Kyle"]

zipped_index = list(zip(first_index,inner_index))
print(zipped_index)
"""
# Burada her iki tarafda index olarak geliyor.
# burayı bir grup olarak düşünebiliriz
# simpsonlar ve south park lar olarak 2 grup
# sonrasında ise Sİmpsonlarda Homer,bart,Marge
# South Park da Cartman , Kenny ve Kyle gibi
# burada her iki tarafda index olarak sayılır
# bizim amacımız bunu dataframe haline getirip verilere ulaşmak
[('Simpson', 'Homer'), 
('Simpson', 'Bart'), 
('Simpson', 'Marge'), 
('South Park', 'Cartman'), 
('South Park', 'Kenny'), 
('South Park', 'Kyle')]
"""

zipped_index = pd.MultiIndex.from_tuples(zipped_index) # multi indexe çevirdik bunu kullanarak dataframe oluşturabiliyoruz
print(zipped_index)
"""
MultiIndex([(   'Simpson',   'Homer'),
            (   'Simpson',    'Bart'),
            (   'Simpson',   'Marge'),
            ('South Park', 'Cartman'),
            ('South Park',   'Kenny'),
            ('South Park',    'Kyle')],
           )
"""

sample_values = np.ones((6,2))
print(sample_values) # veriler olarak hepsini 1 yaptık
"""
[[1. 1.]
 [1. 1.]
 [1. 1.]
 [1. 1.]
 [1. 1.]
 [1. 1.]]
"""

big_df = pd.DataFrame(sample_values,index=zipped_index,columns=["Age","Salary"]) # colonada Age ve Salary yaptık
print(big_df)
"""
                    Age  Salary
Simpson    Homer    1.0     1.0
           Bart     1.0     1.0
           Marge    1.0     1.0
South Park Cartman  1.0     1.0
           Kenny    1.0     1.0
           Kyle     1.0     1.0
"""

print(big_df.loc["Simpson"].loc["Homer"])
"""
Age       1.0
Salary    1.0
Name: Homer, dtype: float64
"""



