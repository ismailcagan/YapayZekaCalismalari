import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")
print(df)

print(df.columns)

plt.figure(figsize=(15,10))

plt.subplot(1,2,1)
sns.boxplot(x="class", y="age",data=df)
plt.title("Age by Class")
plt.xlabel("Class")
plt.ylabel("Age")

plt.subplot(1,2,2)
sns.boxplot(x="class", y="fare",data=df)
plt.title("Fare by Class")
plt.xlabel("Class")
plt.ylabel("Fare")

plt.show()













