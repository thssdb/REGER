import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['agg.path.chunksize'] = 60000

np.set_printoptions(suppress=True)

plt.style.use('ggplot')
sns.set_theme(style="ticks", palette="pastel")

fig, ax_arr = plt.subplots(6,2,figsize=(14,36))
my_palette=["#1178b4", "#33a02c","#e31a1c", "#ff7f00"]#,"#6a3d9a","#fb9a99", "#814a19"]
fig.subplots_adjust(hspace=0.3)
fig.subplots_adjust(wspace=0.3)
size =25

df = []
df1 = pd.read_csv("./data_draw/EPM-Education/epm_0_2.csv")
df2 = pd.read_csv("./data_draw/GW-Magnetic/syndata_magnetic0_2.csv")
df3 = pd.read_csv("./data_draw/Metro-Traffic/syndata_metro_2.csv")
df4 = pd.read_csv("./data_draw/Nifty-Stocks/syndata_stocks0_2.csv")
df5 = pd.read_csv("./data_draw/USGS-Earthquakes/syndata_earthquakes0_2.csv")
df6 = pd.read_csv("./data_draw/Vehicle-Charge/electric_vehicle_charging_2.csv")
df7 = pd.read_csv("./data_draw/CS-Sensors/test_2.csv")
df8 = pd.read_csv("./data_draw/Cyber-Vehicle/syndata_vehicle0_2.csv")
df9 = pd.read_csv("./data_draw/TH-Climate/syndata_climate0_2.csv")
df10 = pd.read_csv("./data_draw/TY-Fuel/syndata_fuel0_2.csv")
df11 = pd.read_csv("./data_draw/TY-Transport/syndata_transport0_2.csv")
df12 = pd.read_csv("./data_draw/YZ-Electricity/0_2.csv")
df.append(df1)
df.append(df2)
df.append(df3)
df.append(df4)
df.append(df5)
df.append(df6)
df.append(df7)
df.append(df8)
df.append(df9)
df.append(df10)
df.append(df11)
df.append(df12)


dataset_list = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"] 
title_i = ["a","b","c","d","e","f","g","h","i","j","k","l"]
# xticklabels_list = []
# xticks_list = []
# for i in range(0,10):
#     xticklabels_list.append(r"$ {{ {:2d} }}$".format(i))
#     xticks_list.append(i)
length_x = 3
length_y = 4
fig, ax_arr = plt.subplots(length_x,length_y,figsize=(28,16))
my_palette=["#e31a1c", "#1178b4","#e31a1c","#ff7f00"]#,"#6a3d9a","#fb9a99"]#, "#814a19"]
fig.subplots_adjust(hspace=0.35)
fig.subplots_adjust(wspace=0.35)

count = 0
for dataset in dataset_list:
    dx = int(count / 4)
    dy = int(count % 4)

    f=sns.lineplot(x='order',y='value',linewidth = 3,data=df[count][0:1000],color="#3c78d8",dashes=False,ax=ax_arr[dx][dy])
    #f.get_legend().remove()
    f.tick_params(labelsize = size)
    f.xaxis.label.set_size(size)
    f.yaxis.label.set_size(size)
    f.set_title("("+title_i[count] +") "+ dataset).set_fontsize(size)
    f.set_xlabel("Order")
    f.set_ylabel("Value")
    count += 1

plt.savefig("./figs/datasets_value_subgraph1000.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./figs/datasets_value_subgraph1000.png", dpi = 400,bbox_inches='tight')


# f=sns.lineplot(x='order',y='value',linewidth = 3,data=df2[0:1000],color="#3c78d8",dashes=False,ax=ax_arr[0][1])
# #f.get_legend().remove()
# f.tick_params(labelsize = size)
# f.xaxis.label.set_size(size)
# f.yaxis.label.set_size(size)
# f.set_title("(b) GW-Magnetic - Value").set_fontsize(size)
# f.set_xlabel("Order")
# f.set_ylabel("Value")

# f=sns.lineplot(x='order',y='value',linewidth = 3,data=df3[0:1000],color="#3c78d8",dashes=False,ax=ax_arr[1][0])
# #f.get_legend().remove()
# f.tick_params(labelsize = size)
# f.xaxis.label.set_size(size)
# f.yaxis.label.set_size(size)
# f.set_title("(c) Metro-Traffic - Value").set_fontsize(size)
# f.set_xlabel("Order")
# f.set_ylabel("Value")

# f=sns.lineplot(x='order',y='value',linewidth = 3,data=df4[0:1000],color="#3c78d8",dashes=False,ax=ax_arr[1][1])
# #f.get_legend().remove()
# f.tick_params(labelsize = size)
# f.xaxis.label.set_size(size)
# f.yaxis.label.set_size(size)
# f.set_title("(d) Nifty-Stocks - Value").set_fontsize(size)
# f.set_xlabel("Order")
# f.set_ylabel("Value")

# f=sns.lineplot(x='order',y='value',linewidth = 3,data=df5[0:1000],color="#3c78d8",dashes=False,ax=ax_arr[2][0])
# #f.get_legend().remove()
# f.tick_params(labelsize = size)
# f.xaxis.label.set_size(size)
# f.yaxis.label.set_size(size)
# f.set_title("(e) USGS-Earthquakes - Value").set_fontsize(size)
# f.set_xlabel("Order")
# f.set_ylabel("Value")


# f=sns.lineplot(x='order',y='value',linewidth = 3,data=df6[0:1000],color="#3c78d8",dashes=False,ax=ax_arr[2][1])
# #f.get_legend().remove()
# f.tick_params(labelsize = size)
# f.xaxis.label.set_size(size)
# f.yaxis.label.set_size(size)
# f.set_title("(f) Vehicle-Charge - Value").set_fontsize(size)
# f.set_xlabel("Order")
# f.set_ylabel("Value")



# f=sns.lineplot(x='order',y='value',linewidth = 3,data=df7[0:1000],color="#3c78d8",dashes=False,ax=ax_arr[3][0])
# #f.get_legend().remove()
# f.tick_params(labelsize = size)
# f.xaxis.label.set_size(size)
# f.yaxis.label.set_size(size)
# f.set_title("(g) CS-Sensors - Value").set_fontsize(size)
# f.set_xlabel("Order")
# f.set_ylabel("Value")

# f=sns.lineplot(x='order',y='value',linewidth = 3,data=df8[0:1000],color="#3c78d8",dashes=False,ax=ax_arr[3][1])
# #f.get_legend().remove()
# f.tick_params(labelsize = size)
# f.xaxis.label.set_size(size)
# f.yaxis.label.set_size(size)
# f.set_title("(h) Cyber-Vehicle - Value").set_fontsize(size)
# f.set_xlabel("Order")
# f.set_ylabel("Value")


# f=sns.lineplot(x='order',y='value',linewidth = 3,data=df9[0:1000],color="#3c78d8",dashes=False,ax=ax_arr[4][0])
# #f.get_legend().remove()
# f.tick_params(labelsize = size)
# f.xaxis.label.set_size(size)
# f.yaxis.label.set_size(size)
# f.set_title("(i) TH-Climate - Value").set_fontsize(size)
# f.set_xlabel("Order")
# f.set_ylabel("Value")

# f=sns.lineplot(x='order',y='value',linewidth = 3,data=df10[0:1000],color="#3c78d8",dashes=False,ax=ax_arr[4][1])
# #f.get_legend().remove()
# f.tick_params(labelsize = size)
# f.xaxis.label.set_size(size)
# f.yaxis.label.set_size(size)
# f.set_title("(j) TY-Fuel - Value").set_fontsize(size)
# f.set_xlabel("Order")
# f.set_ylabel("Value")

# f=sns.lineplot(x='order',y='value',linewidth = 3,data=df11[0:1000],color="#3c78d8",dashes=False,ax=ax_arr[5][0])
# #f.get_legend().remove()
# f.tick_params(labelsize = size)
# f.xaxis.label.set_size(size)
# f.yaxis.label.set_size(size)
# f.set_title("(k) TY-Transport - Value").set_fontsize(size)
# f.set_xlabel("Order")
# f.set_ylabel("Value")

# f=sns.lineplot(x='order',y='value',linewidth = 3,data=df12[0:1000],color="#3c78d8",dashes=False,ax=ax_arr[5][1])
# #f.get_legend().remove()
# f.tick_params(labelsize = size)
# f.xaxis.label.set_size(size)
# f.yaxis.label.set_size(size)
# f.set_title("(l) YZ-Electricity - Value").set_fontsize(size)
# f.set_xlabel("Order")
# f.set_ylabel("Value")





#plt.xticks([])
#plt.yticks([])
