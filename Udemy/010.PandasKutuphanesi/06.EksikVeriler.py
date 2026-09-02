import numpy as np
import pandas as pd

weather_na_df = pd.read_excel("6-weatherna.xlsx")
print(weather_na_df)
"""
   Istanbul  New York  Amsterdam  Paris
0      20.0      10.0       15.0   12.0
1      21.0      10.0        NaN   14.0
2       NaN      13.0       18.0   15.0
3      22.0      14.0       19.0   18.0
4      25.0      15.0       15.0   20.0
5      28.0       NaN       22.0    NaN
6      15.0      12.0       15.0   15.0
7      20.0      15.0       14.0    NaN
8      22.0      16.0       16.0    NaN
"""

print(weather_na_df.isna())
"""
BOŞ VERİ OLDUĞU İÇİN True DEĞERLERİ DÖNÜYOR
   Istanbul  New York  Amsterdam  Paris
0     False     False      False  False
1     False     False       True  False
2      True     False      False  False
3     False     False      False  False
4     False     False      False  False
5     False      True      False   True
6     False     False      False  False
7     False     False      False   True
8     False     False      False   True
"""

print(weather_na_df.describe())
"""
EKSİK VERİLERE GÖRE İSTATİK VE OLASILIK HESAPLAMALARI YAPILIR
        Istanbul   New York  Amsterdam      Paris
count   8.000000   8.000000   8.000000   6.000000
mean   21.625000  13.125000  16.750000  15.666667
std     3.814914   2.295181   2.712405   2.875181
min    15.000000  10.000000  14.000000  12.000000
25%    20.000000  11.500000  15.000000  14.250000
50%    21.500000  13.500000  15.500000  15.000000
75%    22.750000  15.000000  18.250000  17.250000
max    28.000000  16.000000  22.000000  20.000000
"""

print(weather_na_df["Istanbul"])
# istanbul verilerini görebiliriz
"""
0    20.0
1    21.0
2     NaN
3    22.0
4    25.0
5    28.0
6    15.0
7    20.0
8    22.0
Name: Istanbul, dtype: float64
"""

print(weather_na_df["Istanbul"].count())
"""
8 verinin dolu olduğunu gösterir olduğunu gösterir
"""

print(weather_na_df["Istanbul"].isna)
"""
HANGİ VERİLER NaN OLDUĞUNU GÖSTERİR
<bound method Series.isna of 0    20.0
1    21.0
2     NaN
3    22.0
4    25.0
5    28.0
6    15.0
7    20.0
8    22.0
Name: Istanbul, dtype: float64>
"""

print(weather_na_df.dropna())  # eksik satırları siler(Tavsiye edilmez)

"""
EKSİK SATIRLARI SİLER
   Istanbul  New York  Amsterdam  Paris
0      20.0      10.0       15.0   12.0
3      22.0      14.0       19.0   18.0
4      25.0      15.0       15.0   20.0
6      15.0      12.0       15.0   15.0
"""

print(weather_na_df.drop("Paris", axis=1))  # belirtilen sütunu siler
"""
   Istanbul  New York  Amsterdam
0      20.0      10.0       15.0
1      21.0      10.0        NaN
2       NaN      13.0       18.0
3      22.0      14.0       19.0
4      25.0      15.0       15.0
5      28.0       NaN       22.0
6      15.0      12.0       15.0
7      20.0      15.0       14.0
8      22.0      16.0       16.0
"""

print(weather_na_df.fillna(100))  # eksik verileri 100 ile doldur
"""
   Istanbul  New York  Amsterdam  Paris
0      20.0      10.0       15.0   12.0
1      21.0      10.0      100.0   14.0
2     100.0      13.0       18.0   15.0
3      22.0      14.0       19.0   18.0
4      25.0      15.0       15.0   20.0
5      28.0     100.0       22.0  100.0
6      15.0      12.0       15.0   15.0
7      20.0      15.0       14.0  100.0
8      22.0      16.0       16.0  100.0
"""

print(weather_na_df.mean())  # sütun değerlerinin ortalamasını alır
"""
Istanbul     21.625000
New York     13.125000
Amsterdam    16.750000
Paris        15.666667
dtype: float64
"""

print(weather_na_df.fillna(weather_na_df.mean()))
# eksik verileri ortalama ile doldur
"""
   Istanbul  New York  Amsterdam      Paris
0    20.000    10.000      15.00  12.000000
1    21.000    10.000      16.75  14.000000
2    21.625    13.000      18.00  15.000000
3    22.000    14.000      19.00  18.000000
4    25.000    15.000      15.00  20.000000
5    28.000    13.125      22.00  15.666667
6    15.000    12.000      15.00  15.000000
7    20.000    15.000      14.00  15.666667
8    22.000    16.000      16.00  15.666667
"""
