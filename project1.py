import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("F:/python/numpy/healthcare_project/healthcare_messy_data (1).csv")
# print(df.head(10))

# 2. Clean Patient Names
df['Patient Name'] = df['Patient Name'].str.strip().str.title()
# df['Patient Name']=df.drop_duplicates(inplace=True)


df['Age']=df['Age'].replace('forty',40)
df['Age']=pd.to_numeric(df['Age'],errors='coerce')
df['Age']=df['Age'].fillna(df['Age'].median().astype(int))

df['Visit Date']=pd.to_datetime(df['Visit Date'],format="mixed")

sp_split=df['Blood Pressure'].str.split('/',expand=True)
df['Systolic_BP']=pd.to_numeric(sp_split[0])
df['Diastolic_BP']=pd.to_numeric(sp_split[1])
df.drop(columns=['Blood Pressure'],inplace=True)


df['Condition']=df['Condition'].fillna('unknow')
df['Medication']=df['Medication'].str.title()


df['Email']=df['Email'].str.strip().replace('',np.nan).fillna('no email')
df['Phone Number']=df['Phone Number'].str.strip().replace('',np.nan).fillna('no number')
print(df.head(10))

# df.to_csv('F:/python/numpy/healthcare_project/clean_healthcare_data.csv', index=False)

# #--data visulation--
sns.barplot(x='Condition',y='Age',hue='Gender',data=df,palette='viridis')
plt.legend(bbox_to_anchor=(1.02, 1),loc='upper left')
plt.show()


sns.histplot(df['Cholesterol'],kde=True)
fig,axes=plt.subplots(1,2,figsize=(14, 6))
sns.boxplot(x='Medication',y='Systolic_BP',ax=axes[0],data=df,palette='GnBu')
axes[0].set_title('Systolic BP by Medication')

sns.boxplot(x='Medication',y='Diastolic_BP',ax=axes[1],data=df,palette='viridis')
axes[1].set_title('Diastolic BP by Medication')
plt.tight_layout()
plt.show

df['Visit Date']=pd.to_datetime(df['Visit Date'])
df['Year']=df['Visit Date'].dt.year
prob=df.groupby('Year')['Patient Name'].count().head(5)
plt.figure(figsize=(10, 5))
sns.lineplot(x=prob.index, y=prob.values,marker='o', markersize=8, linewidth=2, color='#2a9d8f')
plt.title('Trend of Patient Visits (2018-2020)', fontsize=14, pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Patients', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)  # Adds a light grid for readability
plt.xticks(prob.index)
plt.show()