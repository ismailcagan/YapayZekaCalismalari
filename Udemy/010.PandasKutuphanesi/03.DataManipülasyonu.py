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

print(new_df.iloc[:, 2])

new_df["Extra"] = 10
print(new_df)
"""
          Salary       Age  Seniority  Extra
Atil    0.728817  0.326017   0.788082     10
Zeynep  0.283831  0.536404   0.624593     10
Atlas   0.490203  0.270813   0.085039     10
Mehmet  0.457839  0.185447   0.792889     10
"""

new_df.drop("Extra", axis=1, inplace=True)
print(new_df)
"""
          Salary       Age  Seniority
Atil    0.728817  0.326017   0.788082
Zeynep  0.283831  0.536404   0.624593
Atlas   0.490203  0.270813   0.085039
Mehmet  0.457839  0.185447   0.792889
"""

print(new_df.loc["Atlas"])
"""
Salary       0.490203
Age          0.270813
Seniority    0.085039
Name: Atlas, dtype: float64
"""

print(new_df.loc["Atlas"]["Salary"])
# 0.4902030561796269

print(new_df.loc["Atlas", "Salary"])
# 0.4902030561796269

new_df.loc["Atlas", "Salary"] = 100
print(new_df)
"""
            Salary       Age  Seniority
Atil      0.728817  0.326017   0.788082
Zeynep    0.283831  0.536404   0.624593
Atlas   100.000000  0.270813   0.085039
Mehmet    0.457839  0.185447   0.792889
"""

print(new_df > 0)
"""
        Salary    Age  Seniority
Atil     False  False       True
Zeynep    True   True      False
Atlas     True   True      False
Mehmet    True   True       True
"""

print(new_df[new_df > 0])
"""
            Salary       Age  Seniority
Atil           NaN       NaN   0.314512
Zeynep    0.318553  0.727362        NaN
Atlas   100.000000  1.087921        NaN
Mehmet    0.485385  0.610526   0.934717
"""

print(new_df[new_df["Salary"] > 1])
"""
       Salary       Age  Seniority
Atlas   100.0  1.087921  -0.344556
"""


print(new_df[new_df["Age"] > 1])
"""
       Salary       Age  Seniority
Atlas   100.0  1.087921  -0.344556
"""
















