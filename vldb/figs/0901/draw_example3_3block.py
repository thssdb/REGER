import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.ticker as mticker
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

df1 = pd.read_csv("./result_evaluation/example100/100_reorder_time.csv")
df2 = pd.read_csv("./result_evaluation/example100/100_reorder_value.csv")


fontsize = 25

plt.rcParams['axes.labelsize'] = fontsize
plt.rcParams['axes.titlesize'] = fontsize
plt.rcParams['xtick.labelsize'] = fontsize
plt.rcParams['ytick.labelsize'] = fontsize

# df1["timestamp"] = df1["timestamp"] - 1634660000

# f=sns.lineplot(x='Order',y='Timestamp',linewidth = 3,data=df1,color="#3c78d8",dashes=False,ax=ax_arr[0][0])
# #f.get_legend().remove()
# f.get_yaxis().get_major_formatter().set_scientific(False)
# f.tick_params(labelsize = fontsize)
# f.xaxis.label.set_size(fontsize)
# f.yaxis.label.set_size(fontsize)
# f.set_title(r"(a) $x^{(t)}$").set_fontsize(fontsize)
# f.set_xlabel("Order")
# f.set_ylabel("Time (+1,634,662,800ms)")
# y_major_locator=MultipleLocator(100)
# f.yaxis.set_major_locator(y_major_locator)
# f.set_ylim(-5,570)
#
# f=sns.lineplot(x='Order',y='Value',linewidth = 3,data=df2,color="#3c78d8",dashes=False,ax=ax_arr[0][1])
# f.tick_params(labelsize = fontsize)
# f.xaxis.label.set_size(fontsize)
# f.yaxis.label.set_size(fontsize)
# f.set_title(r"(b) $x^{(v)}$").set_fontsize(fontsize)
# f.set_xlabel("Order")
# f.set_ylabel("Value")
# y_major_locator=MultipleLocator(2000)
# f.yaxis.set_major_locator(y_major_locator)
# f.set_ylim(-200,6200)


df1['Timestamp_diff'] = df1['Timestamp'].diff().fillna(0)
min_value_diff = df1['Timestamp_diff'].min()
df1['Timestamp_diff'] = df1['Timestamp_diff'] - min_value_diff

partition1_time=[]
partition2_time=[]
partition3_time=[]
for i in range(len(df1)):
    if i < int(len(df1)/3):
        partition1_time.append(df1['Timestamp_diff'][i])
    elif i<int(len(df1)*2/3):
        partition2_time.append(df1['Timestamp_diff'][i])
    else:
        partition3_time.append(df1['Timestamp_diff'][i])

min1=min(partition1_time)
min2=min(partition2_time)
min3=min(partition3_time)

diff2=[]
for i in range(len(partition1_time)):
    diff2.append(partition1_time[i]-min1)
    partition1_time[i]=partition1_time[i]-min1
for i in range(len(partition2_time)):
    diff2.append(partition2_time[i] - min2)
    partition2_time[i]=partition2_time[i]-min2
for i in range(len(partition3_time)):
    diff2.append(partition3_time[i] - min3)
    partition3_time[i]=partition3_time[i]-min3

df1['Timestamp_diff2']=diff2

df1['Timestamp_diff_width'] = df1['Timestamp_diff2'].apply(get_bitwidth)
print(np.sum(df1['Timestamp_diff_width']))

f=sns.lineplot(x='Order',y='Timestamp_diff2',linewidth = 3,data=df1,color="#3c78d8",dashes=False,ax=ax_arr[0][0])
#f.get_legend().remove()
f.get_yaxis().get_major_formatter().set_scientific(False)

f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title(r"(a) $\xi^{(t)}$").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Time")
y_major_locator=MultipleLocator(100)
f.yaxis.set_major_locator(y_major_locator)
f.axvline(x=int(len(df2)/3), color='red', linestyle='--')
f.axvline(x=int(len(df2)*2/3), color='red', linestyle='--')
f.set_ylim(-5,570)

df2['Value_diff'] = df2['Value'].diff().fillna(0)
min_value_diff = df2['Value_diff'].min()
df2['Value_diff'] = df2['Value_diff'] - min_value_diff

partition1_value=[]
partition2_value=[]
partition3_value=[]
for i in range(len(df2)):
    if i < int(len(df2)/3):
        partition1_value.append(df2['Value_diff'][i])
    elif i<int(len(df2)*2/3):
        partition2_value.append(df2['Value_diff'][i])
    else:
        partition3_value.append(df2['Value_diff'][i])

min1=min(partition1_value)
min2=min(partition2_value)
min3=min(partition3_value)

diff2=[]
for i in range(len(partition1_value)):
    diff2.append(partition1_value[i]-min1)
    partition1_value[i]=partition1_value[i]-min1
for i in range(len(partition1_value)):
    diff2.append(partition2_value[i] - min2)
    partition2_value[i]=partition2_value[i]-min2
for i in range(len(partition3_value)):
    diff2.append(partition3_value[i] - min3)
    partition3_value[i]=partition3_value[i]-min3

df2['Value_diff2']=diff2
df2['Value_bit_width'] = df2['Value_diff2'].apply(get_bitwidth)

print(np.sum(df2['Value_bit_width']))

# print(df2)
f=sns.lineplot(x='Order',y='Value_diff2',linewidth = 3,data=df2,color="#3c78d8",dashes=False,ax=ax_arr[0][1])
#f.get_legend().remove()
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title(r"(b) $\xi^{(v)}$").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Value")
y_major_locator=MultipleLocator(2000)
f.yaxis.set_major_locator(y_major_locator)
f.axvline(x=int(len(df2)/3), color='red', linestyle='--')
f.axvline(x=int(len(df2)*2/3), color='red', linestyle='--')
f.set_ylim(-200,6200)

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

#lines, labels = ax_arr[1][1].get_legend_handles_labels()
#fig.legend(lines, labels,  loc = 'upper center',fontsize=25,ncol=2)

#plt.xticks([])
#plt.yticks([])
plt.savefig("./fig/example3.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./fig/example3.png", dpi = 400,bbox_inches='tight')