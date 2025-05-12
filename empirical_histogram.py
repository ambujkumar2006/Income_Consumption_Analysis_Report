import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\Ambuj Kumar\Desktop\IIMA\Info\data_income_consumption_gender.xlsx")

df.columns = ['Income', 'Consumption', 'Gender']
print(df.head())
print(df.describe())

plt.hist(df['Income'], bins=30, density=True, edgecolor='black')
plt.title('Empirical Histogram of Income')
plt.xlabel('Income')
plt.ylabel('Density')
plt.grid(True)
plt.show()