import numpy as np
import pandas as pd
from scipy.stats import lognorm, gamma

# Load your data
df = pd.read_excel(r"C:\Users\Ambuj Kumar\Desktop\IIMA\Info\data_income_consumption_gender.xlsx", header=None)
df.columns = ['Income', 'Consumption', 'Gender']
income_data = df['Income']

# Lognormal MLE fit
shape_ln, loc_ln, scale_ln = lognorm.fit(income_data, floc=0)
loglik_ln = np.sum(lognorm.logpdf(income_data, shape_ln, loc=loc_ln, scale=scale_ln))
k_ln = 2  # shape and scale
aic_ln = 2 * k_ln - 2 * loglik_ln

# Gamma MLE fit
shape_g, loc_g, scale_g = gamma.fit(income_data, floc=0)
loglik_g = np.sum(gamma.logpdf(income_data, shape_g, loc=loc_g, scale=scale_g))
k_g = 2  # shape and scale
aic_g = 2 * k_g - 2 * loglik_g

# Display results
print("Lognormal: Log-Likelihood =", loglik_ln, ", AIC =", aic_ln)
print("Gamma: Log-Likelihood =", loglik_g, ", AIC =", aic_g)
