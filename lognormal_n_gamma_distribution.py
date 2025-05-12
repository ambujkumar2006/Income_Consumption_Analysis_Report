import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import lognorm, gamma

df = pd.read_excel(r"C:\Users\Ambuj Kumar\Desktop\IIMA\Info\data_income_consumption_gender.xlsx", header = None)
df.columns = ['Income', 'Consumption', 'Gender']

income = df['Income']

# plotting empirical histogram (normalized)
count, bins, _ = plt.hist(income, bins=30, density=True, alpha=0.5, color='gray', edgecolor='black',label='Empirical Histogram')

# fitting lognormal distribution
shape_ln, loc_ln, scale_ln = lognorm.fit(income, floc=0)
x = np.linspace(min(income), max(income), 1000)
pdf_lognormal = lognorm.pdf(x, shape_ln, loc_ln, scale_ln)
plt.plot(x, pdf_lognormal, 'r-', label='Lognormal Fit')

# Gamma Distribution
shape_g, loc_g, scale_g = gamma.fit(income, floc=0)
pdf_gamma = gamma.pdf(x, shape_g, loc_g, scale_g)
plt.plot(x, pdf_gamma, 'b--', label='Gamma fit')

#  Final Plot
plt.title('Fitted Distrubution to Income Data')
plt.xlabel('Income')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()