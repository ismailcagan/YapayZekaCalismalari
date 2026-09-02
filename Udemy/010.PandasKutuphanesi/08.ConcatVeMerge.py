import numpy as np
import pandas as pd

# Senaryoya göre datalar 2 ye bölünmüş biz burada dataları birleştirecez
df1 = pd.read_csv("7-concat_data1.csv")
print(df1)
"""
   Employee_ID    Name Department
0            1   Emp_1    Finance
1            2   Emp_2  Marketing
2            3   Emp_3         HR
3            4   Emp_4    Finance
4            5   Emp_5    Finance
5            6   Emp_6  Marketing
6            7   Emp_7         HR
7            8   Emp_8         HR
8            9   Emp_9    Finance
9           10  Emp_10         IT
"""

df2 = pd.read_csv("7-concat_data2.csv")
print(df2)
"""
   Employee_ID    Name Department
0           11  Emp_11    Finance
1           12  Emp_12    Finance
2           13  Emp_13    Finance
3           14  Emp_14    Finance
4           15  Emp_15  Marketing
5           16  Emp_16         HR
6           17  Emp_17  Marketing
7           18  Emp_18  Marketing
8           19  Emp_19  Marketing
9           20  Emp_20    Finance
"""

# CONCAT

df_concat = pd.concat([df1, df2], ignore_index=True)
# ignore_index --> indexleri gözardı et

print(df_concat)
"""
    Employee_ID    Name Department
0             1   Emp_1    Finance
1             2   Emp_2  Marketing
2             3   Emp_3         HR
3             4   Emp_4    Finance
4             5   Emp_5    Finance
5             6   Emp_6  Marketing
6             7   Emp_7         HR
7             8   Emp_8         HR
8             9   Emp_9    Finance
9            10  Emp_10         IT
10           11  Emp_11    Finance
11           12  Emp_12    Finance
12           13  Emp_13    Finance
13           14  Emp_14    Finance
14           15  Emp_15  Marketing
15           16  Emp_16         HR
16           17  Emp_17  Marketing
17           18  Emp_18  Marketing
18           19  Emp_19  Marketing
19           20  Emp_20    Finance
"""

# MERGE

df_merge1 = pd.read_csv("7-merge_data1.csv")
print(df_merge1)
"""
   Employee_ID    Name Department
0            1   Emp_1         IT
1            2   Emp_2         HR
2            3   Emp_3         IT
3            4   Emp_4  Marketing
4            5   Emp_5  Marketing
5            6   Emp_6         IT
6            7   Emp_7         IT
7            8   Emp_8         IT
8            9   Emp_9  Marketing
9           10  Emp_10  Marketing
"""

df_merge2 = pd.read_csv("7-merge_data2.csv")
print(df_merge2)
"""
   Employee_ID  Salary  Experience
0            5   55658           3
1            1  114478           5
2           12   48431          19
3           10   32747           7
4            6   89150           9
5           13   95725           7
6            9   65773           4
7           11   86886          18
"""

# merge - outer join
df_merged_outer = pd.merge(df_merge1, df_merge2, on="Employee_ID", how="outer")
print(df_merged_outer)
"""
    Employee_ID    Name Department    Salary  Experience
0             1   Emp_1         IT  114478.0         5.0
1             2   Emp_2         HR       NaN         NaN
2             3   Emp_3         IT       NaN         NaN
3             4   Emp_4  Marketing       NaN         NaN
4             5   Emp_5  Marketing   55658.0         3.0
5             6   Emp_6         IT   89150.0         9.0
6             7   Emp_7         IT       NaN         NaN
7             8   Emp_8         IT       NaN         NaN
8             9   Emp_9  Marketing   65773.0         4.0
9            10  Emp_10  Marketing   32747.0         7.0
10           11     NaN        NaN   86886.0        18.0
11           12     NaN        NaN   48431.0        19.0
12           13     NaN        NaN   95725.0         7.0
"""

# merge - left join
df_merged_left = pd.merge(df_merge1, df_merge2, on="Employee_ID", how="left")
print(df_merged_left)
"""

   Employee_ID    Name Department    Salary  Experience
0            1   Emp_1         IT  114478.0         5.0
1            2   Emp_2         HR       NaN         NaN
2            3   Emp_3         IT       NaN         NaN
3            4   Emp_4  Marketing       NaN         NaN
4            5   Emp_5  Marketing   55658.0         3.0
5            6   Emp_6         IT   89150.0         9.0
6            7   Emp_7         IT       NaN         NaN
7            8   Emp_8         IT       NaN         NaN
8            9   Emp_9  Marketing   65773.0         4.0
9           10  Emp_10  Marketing   32747.0         7.0
"""

# merge - rightt join
df_merged_right = pd.merge(df_merge1, df_merge2, on="Employee_ID", how="right")
print(df_merged_right)

"""
   Employee_ID    Name Department  Salary  Experience
0            5   Emp_5  Marketing   55658           3
1            1   Emp_1         IT  114478           5
2           12     NaN        NaN   48431          19
3           10  Emp_10  Marketing   32747           7
4            6   Emp_6         IT   89150           9
5           13     NaN        NaN   95725           7
6            9   Emp_9  Marketing   65773           4
7           11     NaN        NaN   86886          18
"""

# merge - inner join

df_merged = pd.merge(df_merge1, df_merge2, on="Employee_ID", how="inner")
print(df_merged)

"""
   Employee_ID    Name Department  Salary  Experience
0            1   Emp_1         IT  114478           5
1            5   Emp_5  Marketing   55658           3
2            6   Emp_6         IT   89150           9
3            9   Emp_9  Marketing   65773           4
4           10  Emp_10  Marketing   32747           7
"""
