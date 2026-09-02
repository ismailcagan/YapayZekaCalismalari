import numpy as np
import pandas as pd

data = np.random.randn(4, 3)
print(data)
"""
[[ 0.47653174 -0.3871543  -1.15481748]
 [-0.3634987  -0.55361778 -0.52925488]
 [-1.17968579 -1.0514755   0.5527554 ]
 [ 1.60158621  1.13653746  0.75976652]]
"""

data_frame = pd.DataFrame(data)
print(data_frame)
"""
          0         1         2
0  0.476532 -0.387154 -1.154817
1 -0.363499 -0.553618 -0.529255
2 -1.179686 -1.051475  0.552755
3  1.601586  1.136537  0.759767
"""
print(type(data_frame))  # <class 'pandas.DataFrame'>

print(data_frame[0])
"""
0    0.476532
1   -0.363499
2   -1.179686
3    1.601586
Name: 0, dtype: float64
"""
print(type(data_frame[0]))  # <class 'pandas.Series'>

new_df = pd.DataFrame(
    data,
    index=["İsmail", "Zeynep", "Atlas", "Necati"],
    columns=["Salary", "Age", "Seniority"],
)
print(new_df)
"""
          Salary       Age  Seniority
İsmail -2.577488 -0.492121   1.487324
Zeynep  0.730033  0.071949  -0.098435
Atlas   1.844755  0.965323  -2.036049
Necati  0.681796  0.999357  -1.021701
"""

print(new_df["Age"])
"""
İsmail   -0.492121
Zeynep    0.071949
Atlas     0.965323
Necati    0.999357
Name: Age, dtype: float64
"""

print(new_df[["Age", "Salary"]])
"""
             Age    Salary
İsmail -0.492121 -2.577488
Zeynep  0.071949  0.730033
Atlas   0.965323  1.844755
Necati  0.999357  0.681796
"""

print(new_df.loc["İsmail"])
"""
Salary      -2.577488
Age         -0.492121
Seniority    1.487324
Name: İsmail, dtype: float64
"""

print(new_df.iloc[0])
"""
Salary      -2.577488
Age         -0.492121
Seniority    1.487324
Name: İsmail, dtype: float64
"""


print(new_df.iloc[:, 1])
"""
İsmail   -0.492121
Zeynep    0.071949
Atlas     0.965323
Necati    0.999357
Name: Age, dtype: float64
"""

print(new_df.iloc[:, 2])
"""
İsmail   -0.244377
Zeynep    1.096213
Atlas     1.077995
Necati   -1.231650
Name: Seniority, dtype: float64
"""
