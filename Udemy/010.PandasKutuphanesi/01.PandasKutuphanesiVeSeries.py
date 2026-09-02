import numpy as np
import pandas as pd


# 1-) SERİES --> tek boyutlu basit dataları tutar
grades = {"İsmail": 50, "James": 60, "Lars": 30}
pd.Series(grades)
"""
İsmail    50
James     60
Lars      30
dtype: int64
"""

names = ["ismail", "James", "Lars"]
grades = [50, 60, 30]

pd.Series(names)
"""
0    ismail
1     James
2      Lars
dtype: str
"""
pd.Series(grades)
"""
0    50
1    60
2    30
dtype: int64
"""
pd.Series(names,grades)
"""
50    ismail
60     James
30      Lars
dtype: str
"""

pd.Series(data=grades, index=names)
"""
ismail    50
James     60
Lars      30
dtype: int64
"""

# with numpy
numpy_array = np.array([50,40,30,20])
pd.Series(numpy_array)
"""
0    50
1    40
2    30
3    20
dtype: int64
"""
# aritmetic
contest_result = pd.Series(data=[10,5,100],index = ["ismail","James","Lars"])
context_result2 = pd.Series(data=[20,50,10],index = ["ismail","James","Lars"])

print(contest_result)
"""
ismail     10
James       5
Lars      100
dtype: int64
"""
print(contest_result["ismail"]) # 10
print(contest_result["Lars"]) # 100

final_result = contest_result + context_result2 # diğer 4 işlem yapılabilir
print(final_result)
"""
ismail     30
James      55
Lars      110
dtype: int64
"""

different_series1 = pd.Series([20,30,40,50],["a","b","c","d"])
print(different_series)
"""
ismail     30
James      55
Lars      110
dtype: int64
"""
different_series2 = pd.Series([10,5,3,1],["a","c","f","g"])
print(different_series2)
"""
a    10
c     5
f     3
g     1
dtype: int64
"""
different_series = different_series1 + different_series2

print(different_series)
"""
a    30.0
b     NaN
c    45.0
d     NaN
f     NaN
g     NaN
dtype: float64
"""

# 2-) DataFrame 










