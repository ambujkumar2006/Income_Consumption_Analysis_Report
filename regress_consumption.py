import pandas as pd
import statsmodels.api as sm

df = pd.read_excel(r"C:\Users\Ambuj Kumar\Desktop\IIMA\Info\data_income_consumption_gender.xlsx", header = None)
df.columns = ['Income', 'Consumption', 'Gender']

# adding constant term for intercept
X = sm.add_constant(df[['Income', 'Gender']])
y =df['Consumption']

# fitting the model
model = sm.OLS(y, X).fit()

print(model.summary())