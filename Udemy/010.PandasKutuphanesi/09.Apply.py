import pandas as pd

df = pd.read_csv("8-apply_function_data.csv")
print(df)
"""
    Employee_ID     Name Department  Salary  Experience  Performance_Score
0             1    Emp_1  Marketing   82251           6                  5
1             2    Emp_2      Sales   52662          24                  3
2             3    Emp_3    Finance   38392           5                  3
3             4    Emp_4      Sales   60535          20                  3
4             5    Emp_5      Sales  108603           2                  2
..          ...      ...        ...     ...         ...                ...
95           96   Emp_96    Finance   93734          19                  4
96           97   Emp_97      Sales  100467          22                  2
97           98   Emp_98         IT   82662          23                  3
98           99   Emp_99         IT   42688          22                  1
99          100  Emp_100         HR   55342          14  
"""
print(df.head())
"""
   Employee_ID   Name Department  Salary  Experience  Performance_Score
0            1  Emp_1  Marketing   82251           6                  5
1            2  Emp_2      Sales   52662          24                  3
2            3  Emp_3    Finance   38392           5                  3
3            4  Emp_4      Sales   60535          20                  3
4            5  Emp_5      Sales  108603           2      
"""
print(df.tail())
"""
    Employee_ID     Name Department  Salary  Experience  Performance_Score
95           96   Emp_96    Finance   93734          19                  4
96           97   Emp_97      Sales  100467          22                  2
97           98   Emp_98         IT   82662          23                  3
98           99   Emp_99         IT   42688          22                  1
99          100  Emp_100         HR   55342          14   
"""

print(df.describe())
"""
       Employee_ID         Salary  Experience  Performance_Score
count   100.000000     100.000000  100.000000          100.00000
mean     50.500000   77508.090000   12.090000            3.03000
std      29.011492   26083.327596    7.543939            1.41746
min       1.000000   30206.000000    1.000000            1.00000
25%      25.750000   54347.500000    5.000000            2.00000
50%      50.500000   80932.000000   12.000000            3.00000
75%      75.250000   97620.500000   19.000000            4.00000
max     100.000000  119474.000000   24.000000            5.00000
"""

print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 6 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   Employee_ID        100 non-null    int64
 1   Name               100 non-null    str  
 2   Department         100 non-null    str  
 3   Salary             100 non-null    int64
 4   Experience         100 non-null    int64
 5   Performance_Score  100 non-null    int64
dtypes: int64(4), str(2)
memory usage: 4.8 KB
None
"""

print(df.columns)
"""

Index(['Employee_ID', 'Name', 'Department', 'Salary', 'Experience',
       'Performance_Score'],
      dtype='str')
"""

print(df[1:20])
"""
    Employee_ID    Name Department  Salary  Experience  Performance_Score
1             2   Emp_2      Sales   52662          24                  3
2             3   Emp_3    Finance   38392           5                  3
3             4   Emp_4      Sales   60535          20                  3
4             5   Emp_5      Sales  108603           2                  2
5             6   Emp_6         IT   82256           6                  5
6             7   Emp_7    Finance  119135          22                  1
7             8   Emp_8    Finance   65222          11                  4
8             9   Emp_9    Finance  107373          16                  1
9            10  Emp_10      Sales  109575          16                  5
10           11  Emp_11  Marketing  114651           1                  4
11           12  Emp_12    Finance   93335           9                  5
12           13  Emp_13      Sales   40965           6                  3
13           14  Emp_14         IT   54538          16                  4
14           15  Emp_15  Marketing  100592           3                  3
15           16  Emp_16         IT   38110          20                  1
16           17  Emp_17  Marketing  109309           4                  1
17           18  Emp_18      Sales   57266          19                  4
18           19  Emp_19         HR   82992           3                  4
19           20  Emp_20  Marketing  112948          19     
"""


def salary_category(salary):
    if salary < 50000:
        return "Low"
    elif 50000 <= salary < 80000:
        return "Medium"
    else:
        return "High"


df["Salary_Category"] = df["Salary"].apply(salary_category)
"""
YENİ KOLON OLUŞTURUR
0       High
1     Medium
2        Low
3     Medium
4       High
       ...  
95      High
96      High
97      High
98       Low
99    Medium
"""

print(df)
"""

    Employee_ID     Name Department  Salary  Experience  Performance_Score  \
0             1    Emp_1  Marketing   82251           6                  5   
1             2    Emp_2      Sales   52662          24                  3   
2             3    Emp_3    Finance   38392           5                  3   
3             4    Emp_4      Sales   60535          20                  3   
4             5    Emp_5      Sales  108603           2                  2   
..          ...      ...        ...     ...         ...                ...   
95           96   Emp_96    Finance   93734          19                  4   
96           97   Emp_97      Sales  100467          22                  2   
97           98   Emp_98         IT   82662          23                  3   
98           99   Emp_99         IT   42688          22                  1   
99          100  Emp_100         HR   55342          14                  3   

   Salary_Category  
0             High  
1           Medium  
2              Low  
3           Medium  
4             High  
..             ...  
95            High  
96            High  
97            High  
98             Low  
99          Medium  

[100 rows x 7 columns]
"""


def adjust_performance(experience):
    if experience > 10:
        return 1
    else:
        return 0


df["Adjusted"] = df["Experience"].apply(adjust_performance)
"""
0     0
1     1
2     0
3     1
4     0
     ..
95    1
96    1
97    1
98    1
99    1
Name: Experience, Length: 100, dtype: int64
"""
print(df)

"""
    Employee_ID     Name Department  Salary  Experience  Performance_Score  \
0             1    Emp_1  Marketing   82251           6                  5   
1             2    Emp_2      Sales   52662          24                  3   
2             3    Emp_3    Finance   38392           5                  3   
3             4    Emp_4      Sales   60535          20                  3   
4             5    Emp_5      Sales  108603           2                  2   
..          ...      ...        ...     ...         ...                ...   
95           96   Emp_96    Finance   93734          19                  4   
96           97   Emp_97      Sales  100467          22                  2   
97           98   Emp_98         IT   82662          23                  3   
98           99   Emp_99         IT   42688          22                  1   
99          100  Emp_100         HR   55342          14                  3   

   Salary_Category  Adjusted  
0             High         0  
1           Medium         1  
2              Low         0  
3           Medium         1  
4             High         0  
..             ...       ...  
95            High         1  
96            High         1  
97            High         1  
98             Low         1  
99          Medium         1  
"""

df["New_Score"] = df["Performance_Score"] + df["Adjusted"]

print(df)
"""
    Employee_ID     Name Department  Salary  Experience  Performance_Score  \
0             1    Emp_1  Marketing   82251           6                  5   
1             2    Emp_2      Sales   52662          24                  3   
2             3    Emp_3    Finance   38392           5                  3   
3             4    Emp_4      Sales   60535          20                  3   
4             5    Emp_5      Sales  108603           2                  2   
..          ...      ...        ...     ...         ...                ...   
95           96   Emp_96    Finance   93734          19                  4   
96           97   Emp_97      Sales  100467          22                  2   
97           98   Emp_98         IT   82662          23                  3   
98           99   Emp_99         IT   42688          22                  1   
99          100  Emp_100         HR   55342          14                  3   

   Salary_Category  Adjusted  New_Score  
0             High         0          5  
1           Medium         1          4  
2              Low         0          3  
3           Medium         1          4  
4             High         0          2  
..             ...       ...        ...  
95            High         1          5  
96            High         1          3  
97            High         1          4  
98             Low         1          2  
99          Medium         1          4  

[100 rows x 9 columns]
"""

def adjust_new(row):
    if row["Experience"] > 10:
        return row["Performance_Score"] + 1
    else:
        return row["Performance_Score"]
    
df["Adjusted_Score"] = df.apply(adjust_new, axis=1)
print(df)

"""
    Employee_ID     Name Department  Salary  Experience  Performance_Score  \
0             1    Emp_1  Marketing   82251           6                  5   
1             2    Emp_2      Sales   52662          24                  3   
2             3    Emp_3    Finance   38392           5                  3   
3             4    Emp_4      Sales   60535          20                  3   
4             5    Emp_5      Sales  108603           2                  2   
..          ...      ...        ...     ...         ...                ...   
95           96   Emp_96    Finance   93734          19                  4   
96           97   Emp_97      Sales  100467          22                  2   
97           98   Emp_98         IT   82662          23                  3   
98           99   Emp_99         IT   42688          22                  1   
99          100  Emp_100         HR   55342          14                  3   

   Salary_Category  Adjusted  New_Score  Adjusted_Score  
0             High         0          5               5  
1           Medium         1          4               4  
2              Low         0          3               3  
3           Medium         1          4               4  
4             High         0          2               2  
..             ...       ...        ...             ...  
95            High         1          5               5  
96            High         1          3               3  
97            High         1          4               4  
98             Low         1          2               2  
99          Medium         1          4               4  

[100 rows x 10 columns]
"""

# Namedeki alt treleri (_) yok et

df["Formatted_Name"] = df["Name"].apply(lambda x : x.replace("_"," "))

print(df)
"""

    Employee_ID     Name Department  Salary  Experience  Performance_Score  \
0             1    Emp_1  Marketing   82251           6                  5   
1             2    Emp_2      Sales   52662          24                  3   
2             3    Emp_3    Finance   38392           5                  3   
3             4    Emp_4      Sales   60535          20                  3   
4             5    Emp_5      Sales  108603           2                  2   
..          ...      ...        ...     ...         ...                ...   
95           96   Emp_96    Finance   93734          19                  4   
96           97   Emp_97      Sales  100467          22                  2   
97           98   Emp_98         IT   82662          23                  3   
98           99   Emp_99         IT   42688          22                  1   
99          100  Emp_100         HR   55342          14                  3   

   Salary_Category  Adjusted  New_Score  Adjusted_Score Formatted_Name  
0             High         0          5               5          Emp 1  
1           Medium         1          4               4          Emp 2  
2              Low         0          3               3          Emp 3  
3           Medium         1          4               4          Emp 4  
4             High         0          2               2          Emp 5  
..             ...       ...        ...             ...            ...  
95            High         1          5               5         Emp 96  
96            High         1          3               3         Emp 97  
97            High         1          4               4         Emp 98  
98             Low         1          2               2         Emp 99  
99          Medium         1          4               4        Emp 100  
"""









