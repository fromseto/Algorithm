import pandas as pd
import sklearn.linear_model as skl_lm
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

advertising_df = pd.read_csv("Data/Advertising.csv")
# print df[:2]
advertising_df.info()

regr = skl_lm.LinearRegression()
# X = scale(advertising.TV, with_mean=True, with_std=False).reshape(-1,1)
X = advertising_df.TV.reshape(-1,1)
y = advertising_df.Sales
regr.fit(X,y)
print(regr.intercept_)
print(regr.coef_)

est = smf.ols('Sales ~ TV', advertising_df).fit()
print est.summary().tables[1]

## multiple linear regression
X = advertising_df[['Radio', 'TV']].as_matrix()
y = advertising_df.Sales

regr.fit(X,y)
print(regr.coef_)
print(regr.intercept_)
est = smf.ols('Sales ~ Radio + TV', advertising_df).fit()
est.summary()
print est.summary().tables[1]