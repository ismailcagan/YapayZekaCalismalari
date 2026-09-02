import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("athlete_events.csv")
print(data)

print(data.describe())
"""
                  ID            Age         Height         Weight  \
count  271116.000000  261642.000000  210945.000000  208241.000000   
mean    68248.954396      25.556898     175.338970      70.702393   
std     39022.286345       6.393561      10.518462      14.348020   
min         1.000000      10.000000     127.000000      25.000000   
25%     34643.000000      21.000000     168.000000      60.000000   
50%     68205.000000      24.000000     175.000000      70.000000   
75%    102097.250000      28.000000     183.000000      79.000000   
max    135571.000000      97.000000     226.000000     214.000000   

                Year  
count  271116.000000  
mean     1978.378480  
std        29.877632  
min      1896.000000  
25%      1960.000000  
50%      1988.000000  
75%      2002.000000  
max      2016.000000  
"""

print(data.head())
"""
	ID	Name	Sex	Age	Height	Weight	Team	NOC	Games	Year	Season	City	Sport	Event	Medal
0	1	A Dijiang	M	24.0	180.0	80.0	China	CHN	1992 Summer	1992	Summer	Barcelona	Basketball	Basketball Men's Basketball	NaN
1	2	A Lamusi	M	23.0	170.0	60.0	China	CHN	2012 Summer	2012	Summer	London	Judo	Judo Men's Extra-Lightweight	NaN
2	3	Gunnar Nielsen Aaby	M	24.0	NaN	NaN	Denmark	DEN	1920 Summer	1920	Summer	Antwerpen	Football	Football Men's Football	NaN
3	4	Edgar Lindenau Aabye	M	34.0	NaN	NaN	Denmark/Sweden	DEN	1900 Summer	1900	Summer	Paris	Tug-Of-War	Tug-Of-War Men's Tug-Of-War	Gold
4	5	Christine Jacoba Aaftink	F	21.0	185.0	82.0	Netherlands	NED	1988 Winter	1988	Winter	Calgary	Speed Skating	Speed Skating Women's 500 metres	NaN
"""


print(data.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 271116 entries, 0 to 271115
Data columns (total 15 columns):
 #   Column  Non-Null Count   Dtype  
---  ------  --------------   -----  
 0   ID      271116 non-null  int64  
 1   Name    271116 non-null  str    
 2   Sex     271116 non-null  str    
 3   Age     261642 non-null  float64
 4   Height  210945 non-null  float64
 5   Weight  208241 non-null  float64
 6   Team    271116 non-null  str    
 7   NOC     271116 non-null  str    
 8   Games   271116 non-null  str    
 9   Year    271116 non-null  int64  
 10  Season  271116 non-null  str    
 11  City    271116 non-null  str    
 12  Sport   271116 non-null  str    
 13  Event   271116 non-null  str    
 14  Medal   39783 non-null   str    
dtypes: float64(3), int64(2), str(10)
memory usage: 31.0 MB
"""
# 1-) SEABORN GRAFİKLERİ

# BOY VE KİLO DAĞILIMI
plt.scatter("Height", "Weight", data=data)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Kilo ve Boy Kıyaslaması")
plt.show()


sns.set_style("whitegrid")
sns.scatterplot(x="Height", y="Weight", data=data)
plt.xlabel("Height of Atheletes")
plt.ylabel("Weight of Atheletes")
plt.title("Athetes Weight vs Height")
plt.show()

# CİNSİYETI BELİRGENLEŞTİRME

sns.set_style("darkgrid")
sns.scatterplot(x="Height", y="Weight", hue="Sex", data=data)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height and Weight")
plt.show()


# 2-) SEABORN GRAFİK ÇEŞİTLERİ

print(data["Medal"].unique())
"""
ALINAN MADALYALARIN UNİQUE OLARAK GÖSTERİR YANİ AYNI MADALYALARDAN
SADECE BİR TANESİNİ GÖSTERİR

<StringArray>
[nan, 'Gold', 'Bronze', 'Silver']
Length: 4, dtype: str
"""
# 2.1-) SCATTERPLOT

# hue özelliği

sns.set_style("darkgrid")
sns.scatterplot(x="Height", y="Weight", hue="Medal", data=data)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height and Weight")
plt.show()

# style özelliği

sns.set_style("darkgrid")
sns.scatterplot(x="Height", y="Weight", hue="Sex", style="Medal", data=data)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height and Weight")
plt.show()

# size özelliği

sns.set_style("darkgrid")
sns.scatterplot(x="Height", y="Weight", hue="Sex", style="Medal", size="Age", data=data)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height and Weight")
plt.show()

# 2.2-) LİNEPLOT

sns.set_style("whitegrid")
sns.lineplot(
    x="Height",
    y="Weight",
    data=data,
)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height and Weight")
plt.show()

sns.set_style("whitegrid")
sns.lineplot(x="Height", y="Weight", data=data, hue="Sex")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height and Weight")
plt.show()

# ------------------------------------------------------------


sns.set_style("white")
sns.displot(x="Height", data=data)
plt.ylabel("Frequency")
plt.title("Athletes Height Distribution")
plt.show()


sns.set_style("white")
sns.displot(x="Height", hue="Sex", data=data)
plt.ylabel("Frequency")
plt.title("Athletes Height Distribution")
plt.show()

# ----------------------------------------------

sns.set_style("white")
sns.displot(x="Height", hue="Sex", data=data, kind="kde")
plt.ylabel("Frequency")
plt.title("Athletes Height Distribution")
plt.show()

# -------------------------------------------------------
sns.barplot(x="Medal", y="Height", hue="Sex", data=data)
plt.title("Medals by Height")
plt.show()

# --------------------------------------------------------------
sns.catplot(x="Medal", y="Height", hue="Sex", col="Season", data=data)

# ------------------------------------------------------------
# Koralasyon
print(data.corr(numeric_only="True"))
"""
              ID       Age    Height    Weight      Year
ID      1.000000 -0.003631 -0.011141 -0.009176  0.011885
Age    -0.003631  1.000000  0.138246  0.212069 -0.115137
Height -0.011141  0.138246  1.000000  0.796213  0.047578
Weight -0.009176  0.212069  0.796213  1.000000  0.019095
Year    0.011885 -0.115137  0.047578  0.019095  1.000000
"""

sns.heatmap(data.corr(numeric_only=True), annot=True)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 3-) BOX-PLOT

# median, quartile, (25%, 50%, 75% ), min max 1.5 * IQR, outlier

data = np.array([5, 7, 9, 15, 20, 22, 25, 30, 32, 35, 37, 40, 50, 55, 60, 100])

plt.figure(figsize=(6, 5)) 
sns.boxplot(y=data)
plt.title("Box Plot")
plt.ylabel("Data Value")
plt.grid(True)
plt.show()




