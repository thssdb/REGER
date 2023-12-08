import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math
import os
from collections import Counter, OrderedDict

def get_count_i_j(i, j,value_counts_dict):
    count = 0
    i = int(i)
    j = int(j)
    for k in range(i+1,j+1):
        if k in value_counts_dict:
            count += value_counts_dict[k]
    # print(count)
    return count

def find_local_minima(x, y,value_counts_dict):
    minima_indices = []
    for i in range(1, len(y) - 1):
        l = len(minima_indices)
        if y[i] < y[i - 1] and y[i] < y[i + 1] :
            if l > 0:
                if  get_count_i_j(x[minima_indices[l-1]],x[i],value_counts_dict)>64 :
                    minima_indices.append(i)
            else:
                minima_indices.append(i)
    return minima_indices

plt.rc('axes.formatter', useoffset=False)


np.set_printoptions(suppress=True)

plt.style.use('ggplot')
sns.set_theme(style="ticks", palette="pastel")

df2 = pd.read_csv("./result_evaluation/example100/100_reorder_value.csv")
df1 = pd.read_csv("./result_evaluation/example100/100_reorder_time.csv")

merged_df = pd.concat([df1, df2], axis=1)
# print(merged_df)

fontsize = 25
plt.rcParams['axes.labelsize'] = fontsize
plt.rcParams['axes.titlesize'] = fontsize
plt.rcParams['xtick.labelsize'] = fontsize
plt.rcParams['ytick.labelsize'] = fontsize

values = df2.iloc[:1000,1].values


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

f = sns.histplot(values, bins=20, kde=True, ax=ax1,linewidth = 3,color="#3c78d8")

kde_curve = ax1.get_lines()[0].get_data()  
kde_x, kde_y = kde_curve[0], kde_curve[1]
value_counts = Counter(values)


value_counts_dict = dict(value_counts)

minima_indices = find_local_minima(kde_x, kde_y, value_counts_dict)
minima_points = [(kde_x[i], kde_y[i]) for i in minima_indices]
str_kde = ""
for value in minima_indices:
    str_kde += str(int(kde_x[value]))
    str_kde += ","

for value in minima_indices:
    ax1.axvline(x=kde_x[value], color='red', linestyle='--')
ax1.set_title("(a) Partition") 
ax1.set_xlabel("Value")
ax1.set_ylabel("Frequency")

ax2.plot(merged_df['Timestamp'],merged_df['Value'],marker='o',linewidth = 3,color="#3c78d8")

for value in minima_indices:
    ax2.axhline(y=kde_x[value], color='red',  linestyle='--')
ax2.set_title("(b) Order") 
ax2.set_xlabel("Time")
ax2.set_ylabel("Value")


plt.tight_layout()

fig.savefig("./fig/example_distribution.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./fig/example_distribution.png", dpi = 400,bbox_inches='tight')

