import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.ticker as mticker
from matplotlib.ticker import MaxNLocator
# from IPython.display import Latex

plt.rc('axes.formatter', useoffset=False)

np.set_printoptions(suppress=True)

plt.style.use('ggplot')
sns.set_theme(style="ticks", palette="pastel")

fig, ax_arr = plt.subplots(3,2,figsize=(12,13))
my_palette=["#1178b4", "#33a02c","#e31a1c", "#ff7f00"]#,"#6a3d9a","#fb9a99", "#814a19"]
fig.subplots_adjust(hspace=0.35)
fig.subplots_adjust(wspace=0.35)

df1 = pd.read_csv("./result_evaluation/example100/100_timeorder_time.csv")
df2 = pd.read_csv("./result_evaluation/example100/100_timeorder_value.csv")
df3 = pd.read_csv("./result_evaluation/example100/100_valueorder_time.csv")
df4 = pd.read_csv("./result_evaluation/example100/100_valueorder_value.csv")
df5 = pd.read_csv("./result_evaluation/example100/100_reorder_reverse_move_time.csv")
df6 = pd.read_csv("./result_evaluation/example100/100_reorder_reverse_move_value.csv")
fontsize = 20

data_number = 100 #1000 #10000 #len(df1)
df1=df1[0:data_number]
df2=df2[0:data_number]
df3=df3[0:data_number]
df4=df4[0:data_number]
df5=df5[0:data_number]
df6=df6[0:data_number]

a_list=[]
b_list=[33,39,40,41,42,43,44,45,52,53,54,55,59,60,61,62,67,68,69,70,71,75,76,77,78,83,84,85,86,93,94,95,96,97]
# for i in range(len(b_list)):
#     b_list[i]=100-b_list[i]
for i in range(1,100):
    if i not in b_list:
        a_list.append(i)

f=sns.lineplot(x='Order',y='Timestamp',linewidth = 3,data=df1,color="#3c78d8",dashes=False,ax=ax_arr[0][0])
for i in range(len(b_list)):
    index=b_list[i]
    sns.regplot(x=np.array([df1["Order"][index-1]]), y=np.array([df1["Timestamp"][index-1]]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[0][0])
f.get_yaxis().get_major_formatter().set_scientific(False)
#f.get_legend().remove()
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(a) Time Order").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Time (+1,634,662,800ms)")
f.yaxis.set_major_locator(MaxNLocator(nbins=3)) 
f.set_ylim(-20,530)

f=sns.lineplot(x='Order',y='Value',linewidth = 3,data=df2,color="#3c78d8",dashes=False,ax=ax_arr[0][1])
for i in range(len(b_list)):
    index=b_list[i]
    sns.regplot(x=np.array([df2["Order"][index-1]]), y=np.array([df2["Value"][index-1]]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[0][1])
#f.get_legend().remove()
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(b) Time Order").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Value")

a_list=list(range(1,67))
b_list=list(range(67,101))

f=sns.lineplot(x='Order',y='Timestamp',linewidth = 3,data=df3,color="#3c78d8",dashes=False,ax=ax_arr[1][0])
for i in range(len(b_list)):
    index=b_list[i]
    sns.regplot(x=np.array([df3["Order"][index-1]]), y=np.array([df3["Timestamp"][index-1]]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[1][0])
f.get_yaxis().get_major_formatter().set_scientific(False)
#f.get_legend().remove()
f.get_yaxis().get_major_formatter().set_scientific(False)
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(c) Value Order").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Time (+1,634,662,800ms)")
f.yaxis.set_major_locator(MaxNLocator(nbins=3)) 
f.set_ylim(-20,530)

f=sns.lineplot(x='Order',y='Value',linewidth = 3,data=df4,color="#3c78d8",dashes=False,ax=ax_arr[1][1])
for i in range(len(b_list)):
    index=b_list[i]
    sns.regplot(x=np.array([df4["Order"][index-1]]), y=np.array([df4["Value"][index-1]]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[1][1])
#f.get_legend().remove()
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(d) Value Order").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Value")

a_list=list(range(1,67))
b_list=list(range(67,101))

f=sns.lineplot(x='Order',y='Timestamp',linewidth = 3,data=df5,color="#3c78d8",dashes=False,ax=ax_arr[2][0])
for i in range(len(b_list)):
    index=b_list[i]
    sns.regplot(x=np.array([df5["Order"][index-1]]), y=np.array([df5["Timestamp"][index-1]]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[2][0])
f.get_yaxis().get_major_formatter().set_scientific(False)
#f.get_legend().remove()
f.get_yaxis().get_major_formatter().set_scientific(False)
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(e) REGER Order").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Time (+1,634,662,800ms)")
f.yaxis.set_major_locator(MaxNLocator(nbins=3)) 
f.set_ylim(-20,530)

f=sns.lineplot(x='Order',y='Value',linewidth = 3,data=df6,color="#3c78d8",dashes=False,ax=ax_arr[2][1])
for i in range(len(b_list)):
    index=b_list[i]
    sns.regplot(x=np.array([df6["Order"][index-1]]), y=np.array([df6["Value"][index-1]]), scatter=True, fit_reg=False, marker='o', scatter_kws={"s": 100},color="red",ax=ax_arr[2][1])
#f.get_legend().remove()
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(f) REGER Order").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Value")


plt.savefig("./fig/example_fluctuation_subgraph_100_2.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./fig/example_fluctuation_subgraph_100_2.png", dpi = 400,bbox_inches='tight')