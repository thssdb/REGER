import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.ticker as mticker
from matplotlib.pyplot import MultipleLocator
# from IPython.display import Latex

plt.rc('axes.formatter', useoffset=False)

np.set_printoptions(suppress=True)

plt.style.use('ggplot')
sns.set_theme(style="ticks", palette="pastel")

fig, ax_arr = plt.subplots(3,2,figsize=(12,17))
my_palette=["#1178b4", "#33a02c","#e31a1c", "#ff7f00"]#,"#6a3d9a","#fb9a99", "#814a19"]
fig.subplots_adjust(hspace=0.35)
fig.subplots_adjust(wspace=0.45)

df1 = pd.read_csv("./result_evaluation/example100/100_timeorder_time.csv")
df2 = pd.read_csv("./result_evaluation/example100/100_timeorder_value.csv")
df3 = pd.read_csv("./result_evaluation/example100/100_valueorder_time.csv")
df4 = pd.read_csv("./result_evaluation/example100/100_valueorder_value.csv")
df5 = pd.read_csv("./result_evaluation/example100/100_reorder_time.csv")
df6 = pd.read_csv("./result_evaluation/example100/100_reorder_value.csv")
fontsize = 25

data_number = 100 #1000 #10000 #len(df1)
df1=df1[0:data_number]
df2=df2[0:data_number]
df3=df3[0:data_number]
df4=df4[0:data_number]
df5=df5[0:data_number]
df6=df6[0:data_number]

f=sns.lineplot(x='Order',y='Timestamp',linewidth = 3,data=df1,color="#3c78d8",dashes=False,ax=ax_arr[0][0])
f.get_yaxis().get_major_formatter().set_scientific(False)
#f.get_legend().remove()
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(a) Time Order - Time").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Time (+1,634,662,800ms)")
y_major_locator=MultipleLocator(100)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-5,570)

f=sns.lineplot(x='Order',y='Value',linewidth = 3,data=df2,color="#3c78d8",dashes=False,ax=ax_arr[0][1])
#f.get_legend().remove()
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(b) Time Order - Value").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Value")
y_major_locator=MultipleLocator(2000)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-200,6200)


f=sns.lineplot(x='Order',y='Timestamp',linewidth = 3,data=df3,color="#3c78d8",dashes=False,ax=ax_arr[1][0])
f.get_yaxis().get_major_formatter().set_scientific(False)
#f.get_legend().remove()
f.get_yaxis().get_major_formatter().set_scientific(False)
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(c) Value Order - Time").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Time (+1,634,662,800ms)")
y_major_locator=MultipleLocator(100)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-5,570)

f=sns.lineplot(x='Order',y='Value',linewidth = 3,data=df4,color="#3c78d8",dashes=False,ax=ax_arr[1][1])
#f.get_legend().remove()
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(d) Value Order - Value").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Value")
y_major_locator=MultipleLocator(2000)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-200,6200)


f=sns.lineplot(x='Order',y='Timestamp',linewidth = 3,data=df5,color="#3c78d8",dashes=False,ax=ax_arr[2][0])
f.get_yaxis().get_major_formatter().set_scientific(False)
#f.get_legend().remove()
f.get_yaxis().get_major_formatter().set_scientific(False)
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(e) Reordered - Time").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Time (+1,634,662,800ms)")
y_major_locator=MultipleLocator(100)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-5,570)

f=sns.lineplot(x='Order',y='Value',linewidth = 3,data=df6,color="#3c78d8",dashes=False,ax=ax_arr[2][1])
#f.get_legend().remove()
f.tick_params(labelsize = fontsize)
f.xaxis.label.set_size(fontsize)
f.yaxis.label.set_size(fontsize)
f.set_title("(f) Reordered - Value").set_fontsize(fontsize)
f.set_xlabel("Order")
f.set_ylabel("Value")
y_major_locator=MultipleLocator(2000)
f.yaxis.set_major_locator(y_major_locator)
f.set_ylim(-200,6200)


plt.savefig("fig/example_fluctuation_subgraph_100.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("fig/example_fluctuation_subgraph_100.png", dpi = 400,bbox_inches='tight')