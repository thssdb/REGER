import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math
import os
from matplotlib.pyplot import MultipleLocator

def get_bitwidth(v):
    if v == 0:
        return 1
    else:
        return math.floor(math.log2(abs(v)))+1

plt.rc('axes.formatter', useoffset=False)


np.set_printoptions(suppress=True)

plt.style.use('ggplot')
sns.set_theme(style="ticks", palette="pastel")

# fig, ax_arr = plt.subplots(1,2,figsize=(7,10))
# my_palette=["#1178b4", "#33a02c","#e31a1c", "#ff7f00"]#,"#6a3d9a","#fb9a99", "#814a19"]
# fig.subplots_adjust(hspace=0.4)
# fig.subplots_adjust(wspace=0.35)

df2 = pd.read_csv("./result_evaluation/example100/100_timeorder_value.csv")


# path_dir = r"C:\Users\xiaoj\Documents\GitHub\encoding-reorder\vldb\dataset_test\\"
# "GW-Magnetic","Metro-Traffic", "Nifty-Stocks","USGS-Earthquakes", "Cyber-Vehicle", "TH-Climate", "TY-Fuel", "TY-Transport","CS-Sensors","Vehicle-Charge","EPM-Education"
# dataset_list = [ "TY-Fuel"]
# dataset_list = ["Nifty-Stocks"]
fontsize = 25
# sns.set_theme(style="ticks", palette="pastel")

plt.rcParams['axes.labelsize'] = fontsize
plt.rcParams['axes.titlesize'] = fontsize
plt.rcParams['xtick.labelsize'] = fontsize
plt.rcParams['ytick.labelsize'] = fontsize

df2['Value_diff'] = df2['Value'].diff().fillna(0)
min_value_diff = df2['Value_diff'].min()

# 将'Value_diff'列的所有值减去最小值
df2['Value_diff'] = df2['Value_diff'] - min_value_diff
df2['Value_bit_width'] = df2['Value_diff'].apply(get_bitwidth)
x = range(0,100) 

# diff_values = np.diff(values)
# min_diff = np.min(diff_values)

# residual_diff = []
# residual_diff_bit_width = []
# for i in diff_values:
#     residual_diff.append(i-min_diff)
#     residual_diff_bit_width.append(get_bitwidth(i-min_diff))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
f=sns.lineplot(x='Order',y='Value_diff',linewidth = 3,data=df2,color="#3c78d8",dashes=False,ax=ax1)
f.set_title(r"(a) $\xi^{(v)}$")
f.set_xlabel("Order")
f.set_ylabel("Value") 

f=sns.lineplot(x='Order',y='Value_bit_width',linewidth = 3,data=df2,color="#3c78d8",dashes=False,ax=ax2)
f.set_title(r"(b) b($\xi^{(v)}$)")
f.set_xlabel("Order")
f.set_ylabel("Bit width of value") 
y_major_locator=MultipleLocator(3)
f.yaxis.set_major_locator(y_major_locator)

# ax2.plot(x, residual_diff_bit_width, linewidth = 3)
# ax2.set_title("(b) Bit widths of residuals of values")
# ax2.set_xlabel("Order")
# ax2.set_ylabel("Bit width")  
# # ax2.tick_params(axis='x', rotation=45)


# plt.title("Line plot of bit width of residuals")
# plt.xlabel("Timestamps")
# plt.ylabel("Bit width")

plt.tight_layout()
# plt.show()

fig.savefig("./fig/example_bitwidth.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./fig/example_bitwidth.png", dpi = 400,bbox_inches='tight')



# for dataset_i in range(len(dataset_list)):

#     dataset = dataset_list[dataset_i]
#     print(dataset)
#     # if dataset_i < 7:
#     #     continue

#     file_path = path_dir + dataset + "\\0.csv"
    

#     data = pd.read_csv(file_path)
#     # Extract the file name without extension

#     timestamps = data.iloc[:100,0].values
#     values = data.iloc[:101,1].values
#     x = range(0,100) 

#     diff_values = np.diff(values)
#     min_diff = np.min(diff_values)

#     residual_diff = []
#     residual_diff_bit_width = []
#     for i in diff_values:
#         residual_diff.append(i-min_diff)
#         residual_diff_bit_width.append(get_bitwidth(i-min_diff))
    
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 12))
#     ax1.plot(x, residual_diff, marker='o')
#     ax1.set_title("(a) Residuals of values")
#     ax1.set_xlabel("Order")
#     ax1.set_ylabel("Residuals") 

#     # 绘制差分值的分布图
#     # fig = plt.figure(figsize=(10, 6))
#     ax2.plot(x, residual_diff_bit_width, marker='o')
#     ax2.set_title("(b) Bit widths of residuals of values")
#     ax2.set_xlabel("Order")
#     ax2.set_ylabel("Bit width")  
#     # ax2.tick_params(axis='x', rotation=45)


#     # plt.title("Line plot of bit width of residuals")
#     # plt.xlabel("Timestamps")
#     # plt.ylabel("Bit width")
   
#     plt.tight_layout()
#     # plt.show()

#     fig.savefig("./figs/"+dataset+"_example_bitwidth.eps",format='eps',dpi = 400,bbox_inches='tight')
#     fig.savefig("./figs/"+dataset+"_example_bitwidth.png", dpi = 400,bbox_inches='tight')