import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregressdf = pd.read_csv('epa-sea-level.csv')
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
plt.plot(range(1880, 2051), intercept + slope * range(1880, 2051), 'r', label='Best Fit Line 1880-2013')
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
plt.plot(range(2000, 2051), intercept_recent + slope_recent * range(2000, 2051), 'g', label='Best Fit Line 2000-2013')
