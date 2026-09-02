import numpy as np
import pandas as pd

df = pd.read_csv("6-employee.csv")
print(df)

print(df.describe())
"""
              Salary  Experience
count      50.000000   50.000000
mean    78344.500000    7.060000
std     27817.603904    3.966235
min     31016.000000    1.000000
25%     53687.250000    3.000000
50%     78769.500000    7.000000
75%    100778.000000   10.000000
max    119812.000000   14.000000
"""

print(df.count())
"""
Department    50
Employee      50
Salary        50
Experience    50
City          50
dtype: int64
"""

print(df.mean())  # çalışmaz çünkü satırların hepsi sayısal değer değil

print(df["Salary"].mean())  # salary sütununun ortalaması alındı
# 78344.5


print(df[["Salary", "Experience"]].mean())
"""
Salary        78344.50
Experience        7.06
dtype: float64
"""

print((df["Experience"] > 6).head(10))  # tecrübesi 6 yıldan fazla olanlar
"""
0    False
1     True
2    False
3    False
4    False
5     True
6    False
7     True
8     True
9     True
Name: Experience, dtype: bool
"""

print(df[df["Experience"] > 6].head())  # tecrübesi 6 yıldan fazla olan ilk beş kişi
"""
  Department Employee  Salary  Experience      City
1      Sales    Emp_2   78555           8    Austin
5         IT    Emp_6   97121          11   Chicago
7    Finance    Emp_8  119475          10  New York
8    Finance    Emp_9   49457           7   Chicago
9      Sales   Emp_10   96557          10   Chicago
"""

print(
    df[df["Experience"] > 6].count()
)  # tecrübesi 6 yıldan fazla olan kişilerin sayısı
"""
Department    30
Employee      30
Salary        30
Experience    30
City          30
dtype: int64
"""

print(df.head())
"""
  Department Employee  Salary  Experience           City
0  Marketing    Emp_1   53483           1       New York
1      Sales    Emp_2   78555           8         Austin
2    Finance    Emp_3   47159           3         Austin
3      Sales    Emp_4  110077           3  San Francisco
4      Sales    Emp_5   65920           1       New York

Burada csv dosyasında yer alan verilerin ilk beşi gözükmektedir.
bu veriler incelendiğinde departmanlara bakıldığında market satış ve finans gözükmekte
employee çalışanları singeliyor
salary maaşları gösteriyor
Experience deneyimleri gösteriyor
city de şehirleri
bu bilgilerikullanarak bazı sorunları çözeceğiz
"""

# deparmanlara göre gruplama yapacağız
df_group = df.groupby("Department")
print(df_group.count())
"""
            Employee  Salary  Experience  City
Department                                    
Finance           10      10          10    10
HR                 7       7           7     7
IT                10      10          10    10
Marketing         13      13          13    13
Sales             10      10          10    10

burada deparmanlarda çalışanların sayısal bilgilerine ulaşabiliriz
"""

print(df_group.describe())
"""
           Salary                                                          \
            count          mean           std      min       25%      50%   
Department                                                                  
Finance      10.0  90552.700000  27228.231832  47159.0  73222.00  96591.5   
HR            7.0  76182.571429  31647.523983  31016.0  55114.50  78984.0   
IT           10.0  63381.600000  24272.881041  32568.0  39755.25  66681.5   
Marketing    13.0  79555.000000  28431.207129  39268.0  54300.00  70774.0   
Sales        10.0  81038.900000  26623.181534  38571.0  68987.50  80775.0   

                                Experience                                \
                  75%       max      count      mean       std  min  25%   
Department                                                                 
Finance     111836.75  119812.0       10.0  6.500000  3.566822  1.0  3.5   
HR           96630.00  119789.0        7.0  8.714286  4.572173  3.0  5.0   
IT           79850.00   97121.0       10.0  9.000000  4.163332  1.0  7.5   
Marketing   104065.00  117538.0       13.0  6.153846  4.079341  1.0  3.0   
Sales       100047.50  116779.0       10.0  5.700000  3.093003  1.0  3.5   

                               
             50%    75%   max  
Department                     
Finance      6.5   9.50  12.0  
HR           9.0  12.50  14.0  
IT          10.5  11.75  14.0  
Marketing    5.0   9.00  14.0  
Sales        7.0   7.75  10.0  
"""

print(df_group["Salary"].mean()) # departmana göre maaşların ortalaması bulundu
"""
Department
Finance      90552.700000
HR           76182.571429
IT           63381.600000
Marketing    79555.000000
Sales        81038.900000
Name: Salary, dtype: float64
"""

# Şehirlere Göre Maaşları inceleyeceğiz

df_city_group = df.groupby("City")
print(df_city_group.count())
"""
               Department  Employee  Salary  Experience
City                                                   
Austin                 13        13      13          13
Chicago                11        11      11          11
New York               15        15      15          15
San Francisco          11        11      11  
"""

print(df_city_group["Salary"].mean())
"""
City
Austin           81216.000000
Chicago          76869.363636
New York         70484.133333
San Francisco    87144.727273
Name: Salary, dtype: float64
"""




































