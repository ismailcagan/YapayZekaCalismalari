import numpy as np
import pandas as pd

weather_df = pd.read_excel('6-weather.xlsx')
print(weather_df)
"""
   Istanbul  New York  Amsterdam  Paris
0        20        10         15     12
1        21        10         17     14
2        20        13         18     15
3        22        14         19     18
4        25        15         15     20
5        28        13         22     16
6        15        12         15     15
7        20        15         14     14
8        22        16         16     16
"""

print(weather_df.head()) # ilk 5 datayı gösterir
"""
   Istanbul  New York  Amsterdam  Paris
0        20        10         15     12
1        21        10         17     14
2        20        13         18     15
3        22        14         19     18
4        25        15         15     20
"""

print(weather_df.tail()) # son 5 datayı gösterir
"""
   Istanbul  New York  Amsterdam  Paris
4        25        15         15     20
5        28        13         22     16
6        15        12         15     15
7        20        15         14     14
8        22        16         16     16
"""

print(weather_df.info()) # tablo hakkında bilgi verir
"""
<class 'pandas.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 4 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   Istanbul   9 non-null      int64
 1   New York   9 non-null      int64
 2   Amsterdam  9 non-null      int64
 3   Paris      9 non-null      int64
dtypes: int64(4)
memory usage: 420.0 bytes
None
"""

print(weather_df.describe()) # istatik ve olasılık hesaplamalarını verir
"""
        Istanbul   New York  Amsterdam      Paris
count   9.000000   9.000000   9.000000   9.000000
mean   21.444444  13.111111  16.777778  15.555556
std     3.609401   2.147350   2.538591   2.351123
min    15.000000  10.000000  14.000000  12.000000
25%    20.000000  12.000000  15.000000  14.000000
50%    21.000000  13.000000  16.000000  15.000000
75%    22.000000  15.000000  18.000000  16.000000
max    28.000000  16.000000  22.000000  20.000000
"""

print(weather_df.count()) 
# her bir sütunda toplam kaç tane eksiksiz (boş olmayan / NaN olmayan) veri olduğunu gösterir.
"""
Istanbul     9
New York     9
Amsterdam    9
Paris        9
dtype: int64
"""

print(weather_df.isna())
"""
veri tablonuzdaki hangi hücrelerin boş (eksik veri / NaN) 
olduğunu tüm tablo üzerinde tek tek kontrol eder.Bu komutu çalıştırdığınızda, 
orijinal tablonuzla tamamen aynı boyutlarda, sadece True ve False değerlerinden 
oluşan bir tablo görürsünüz:True: O hücrenin boş (eksik veri) olduğu anlamına gelir.
False: O hücrenin dolu (veri var) olduğu anlamına gelir.
"""

"""
   Istanbul  New York  Amsterdam  Paris
0     False     False      False  False
1     False     False      False  False
2     False     False      False  False
3     False     False      False  False
4     False     False      False  False
5     False     False      False  False
6     False     False      False  False
7     False     False      False  False
8     False     False      False  False
"""


