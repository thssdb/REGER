import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import math

plt.rc('axes.formatter', useoffset=False)
def get_bitwidth(v):
    if v == 0:
        return 1
    else:
        return math.floor(math.log2(abs(v)))+1

np.set_printoptions(suppress=True)

plt.style.use('ggplot')
sns.set_theme(style="ticks", palette="pastel")

fig, ax_arr = plt.subplots(2,2,figsize=(12,12))
my_palette=["#1178b4", "#33a02c","#e31a1c", "#ff7f00"]#,"#6a3d9a","#fb9a99", "#814a19"]
fig.subplots_adjust(hspace=0.4)
fig.subplots_adjust(wspace=0.4)

df1 = pd.read_csv("./result_evaluation/example100/100_timeorder_time.csv") #time order
df2 = pd.read_csv("./result_evaluation/example100/100_timeorder_value.csv") #time order
x = range(0,16)

df1['Timestamp_diff'] = df1['Timestamp'].diff().fillna(0)
min_value_diff = df1['Timestamp_diff'].min()
print("min_value_diff",min_value_diff)
df1['Timestamp_diff'] = df1['Timestamp_diff'] - min_value_diff

bitwidths = df1['Timestamp_diff'].apply(get_bitwidth)
print(np.sum(bitwidths))


f=sns.lineplot(x='Order',y='Timestamp_diff',linewidth = 3,data=df1,color="#3c78d8",dashes=False,ax=ax_arr[0][0])
#f.get_legend().remove()
f.get_yaxis().get_major_formatter().set_scientific(False)

f.tick_params(labelsize = 25)
f.xaxis.label.set_size(25)
f.yaxis.label.set_size(25)
f.set_title(r"(a) $\xi^{(t)}$").set_fontsize(25)
f.set_xlabel("Order")
f.set_ylabel("Time")
y_major_locator=MultipleLocator(100)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-5,570)

df2['Value_diff'] = df2['Value'].diff().fillna(0)
min_value_diff = df2['Value_diff'].min()
print("min_value_diff",min_value_diff)
df2['Value_diff'] = df2['Value_diff'] - min_value_diff

bitwidths = df2['Value_diff'].apply(get_bitwidth)
print(np.sum(bitwidths))

f=sns.lineplot(x='Order',y='Value_diff',linewidth = 3,data=df2,color="#3c78d8",dashes=False,ax=ax_arr[0][1])
#f.get_legend().remove()
f.tick_params(labelsize = 25)
f.xaxis.label.set_size(25)
f.yaxis.label.set_size(25)
f.set_title(r"(b) $\xi^{(v)}$").set_fontsize(25)
f.set_xlabel("Order")
f.set_ylabel("Value")
y_major_locator=MultipleLocator(2000)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-200,6200)

df1['Timestamp_diff_width'] = df1['Timestamp_diff'].apply(get_bitwidth)
df2['Value_bit_width'] = df2['Value_diff'].apply(get_bitwidth)

f=sns.lineplot(x='Order',y='Timestamp_diff_width',linewidth = 3,data=df1,color="#3c78d8",dashes=False,ax=ax_arr[1][0])
f.tick_params(labelsize = 25)
f.xaxis.label.set_size(25)
f.yaxis.label.set_size(25)
f.set_title(r"(c) b($\xi^{(t)}$)").set_fontsize(25)
f.set_xlabel("Order")
f.set_ylabel("Bit width")
y_major_locator=MultipleLocator(3)
f.set_ylim(0,14)
f.yaxis.set_major_locator(y_major_locator)

f=sns.lineplot(x='Order',y='Value_bit_width',linewidth = 3,data=df2,color="#3c78d8",dashes=False,ax=ax_arr[1][1])
f.tick_params(labelsize = 25)
f.xaxis.label.set_size(25)
f.yaxis.label.set_size(25)
f.set_title(r"(d) b($\xi^{(v)}$)").set_fontsize(25)
f.set_xlabel("Order")
f.set_ylabel("Bit width")
y_major_locator=MultipleLocator(3)
f.set_ylim(0,14)
f.yaxis.set_major_locator(y_major_locator)
# f.get_yaxis().get_major_formatter().set_scientific(False)

plt.savefig("./fig/example_2_5.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./fig/example_2_5.png", dpi = 400,bbox_inches='tight')