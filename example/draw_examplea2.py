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

plt.rc('axes.formatter', useoffset=False)


np.set_printoptions(suppress=True)

plt.style.use('ggplot')
sns.set_theme(style="ticks", palette="pastel")

fig, ax_arr = plt.subplots(3,2,figsize=(12,17))
my_palette=["#1178b4", "#33a02c","#e31a1c", "#ff7f00"]#,"#6a3d9a","#fb9a99", "#814a19"]
fig.subplots_adjust(hspace=0.4)
fig.subplots_adjust(wspace=0.4)

df1 = pd.read_csv("./result_evaluation/example100/100_reorder_reverse_time.csv")
df2 = pd.read_csv("./result_evaluation/example100/100_reorder_reverse_value.csv")
index1=36
index2=35
y2=df2["Value"][index2]

a=33
b=37
x=36

time_re=[]
value_re=[]
for i in range(a,b):
    time_re.append(df1["Timestamp"][i])
    value_re.append(df2["Value"][i])
for i in range(len(time_re)):
    df1.iloc[i+a,1]=time_re[len(time_re)-1-i]
    df2.iloc[i+a,1] = value_re[len(value_re)-1-i]


# df1["timestamp"] = df1["timestamp"] - 1634660000
f=sns.lineplot(x='Order',y='Timestamp',linewidth = 3,data=df1,color="#3c78d8",dashes=False,ax=ax_arr[0][0])
sns.regplot(x=np.array([index1+1]), y=np.array([df1["Timestamp"][index1]]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[0][0])
#f.get_legend().remove()
f.get_yaxis().get_major_formatter().set_scientific(False)

f.tick_params(labelsize = 25)
f.xaxis.label.set_size(25)
f.yaxis.label.set_size(25)
f.set_title(r"(a) $x^{(t)}$").set_fontsize(25)
f.set_xlabel("Order")
f.set_ylabel("Time (+1,634,662,800ms)")
y_major_locator=MultipleLocator(100)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-5,570)

f=sns.lineplot(x='Order',y='Value',linewidth = 3,data=df2,color="#3c78d8",dashes=False,ax=ax_arr[0][1])
sns.regplot(x=np.array([index2]), y=np.array([y2]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[0][1])
#f.get_legend().remove()
f.tick_params(labelsize = 25)
f.xaxis.label.set_size(25)
f.yaxis.label.set_size(25)
f.set_title(r"(b) $x^{(v)}$").set_fontsize(25)
f.set_xlabel("Order")
f.set_ylabel("Value")
y_major_locator=MultipleLocator(1000)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-200,3200)


df1['Timestamp_diff'] = df1['Timestamp'].diff().fillna(0)
min_value_diff = df1['Timestamp_diff'].min()
df1['Timestamp_diff'] = df1['Timestamp_diff'] - min_value_diff
#print(df1['Timestamp_diff'].iloc[31:46])
print("min_value_diff: "+str(min_value_diff))
bitwidths = df1['Timestamp_diff'].apply(get_bitwidth)
print(np.sum(bitwidths))

f=sns.lineplot(x='Order',y='Timestamp_diff',linewidth = 3,data=df1,color="#3c78d8",dashes=False,ax=ax_arr[1][0])
sns.regplot(x=np.array([index1]), y=np.array([df1["Timestamp_diff"][index1]]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[1][0])
#f.get_legend().remove()
f.get_yaxis().get_major_formatter().set_scientific(False)

f.tick_params(labelsize = 25)
f.xaxis.label.set_size(25)
f.yaxis.label.set_size(25)
f.set_title(r"(c) $\xi^{(t)}$").set_fontsize(25)
f.set_xlabel("Order")
f.set_ylabel("Time")
y_major_locator=MultipleLocator(100)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-5,570)

df2['Value_diff'] = df2['Value'].diff().fillna(0)
min_value_diff = df2['Value_diff'].min()
df2['Value_diff'] = df2['Value_diff'] - min_value_diff
print("min_value_diff: "+str(min_value_diff))
#print( df2['Value_diff'].iloc[31:46])

bitwidths = df2['Value_diff'].apply(get_bitwidth)
print(np.sum(bitwidths))

f=sns.lineplot(x='Order',y='Value_diff',linewidth = 3,data=df2,color="#3c78d8",dashes=False,ax=ax_arr[1][1])
sns.regplot(x=np.array([index2]), y=np.array([df2["Value_diff"][index2-1]]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[1][1])
#f.get_legend().remove()
f.tick_params(labelsize = 25)
f.xaxis.label.set_size(25)
f.yaxis.label.set_size(25)
f.set_title(r"(d) $\xi^{(v)}$").set_fontsize(25)
f.set_xlabel("Order")
f.set_ylabel("Value")
y_major_locator=MultipleLocator(1000)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-200,3200)
# f.get_yaxis().get_major_formatter().set_scientific(False)

df1['Timestamp_diff_width'] = df1['Timestamp_diff'].apply(get_bitwidth)
df2['Value_bit_width'] = df2['Value_diff'].apply(get_bitwidth)

f=sns.lineplot(x='Order',y='Timestamp_diff_width',linewidth = 3,data=df1,color="#3c78d8",dashes=False,ax=ax_arr[2][0])
sns.regplot(x=np.array([index1-1]), y=np.array([df1["Timestamp_diff_width"][index1-2]]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[2][0])
f.tick_params(labelsize = 25)
f.xaxis.label.set_size(25)
f.yaxis.label.set_size(25)
f.set_title(r"(e) b($\xi^{(t)}$)").set_fontsize(25)
f.set_xlabel("Order")
f.set_ylabel("Bit width")
y_major_locator=MultipleLocator(3)
f.set_ylim(0,14)
f.yaxis.set_major_locator(y_major_locator)

f=sns.lineplot(x='Order',y='Value_bit_width',linewidth = 3,data=df2,color="#3c78d8",dashes=False,ax=ax_arr[2][1])
sns.regplot(x=np.array([index2+1]), y=np.array([df2["Value_bit_width"][index2]]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[2][1])
f.tick_params(labelsize = 25)
f.xaxis.label.set_size(25)
f.yaxis.label.set_size(25)
f.set_title(r"(f) b($\xi^{(v)}$)").set_fontsize(25)
f.set_xlabel("Order")
f.set_ylabel("Bit width")
y_major_locator=MultipleLocator(3)
f.set_ylim(0,14)
f.yaxis.set_major_locator(y_major_locator)

plt.savefig("./fig/example_a2.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./fig/example_a2.png", dpi = 400,bbox_inches='tight')