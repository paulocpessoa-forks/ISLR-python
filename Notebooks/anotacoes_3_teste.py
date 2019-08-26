# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:26:29 2019

@author: paulo
"""

# %load ../standard_import.txt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns

from sklearn.preprocessing import scale
import sklearn.linear_model as skl_lm
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
import statsmodels.formula.api as smf

plt.style.use('seaborn-white')


advertising = pd.read_csv('c:/git/ISLR-python/Notebooks/Data/Advertising.csv', usecols=[1,2,3,4])
advertising.info()

est = smf.ols(formula='Sales ~ TV + Radio',data=advertising).fit()
est.f_pvalue

est.summary()