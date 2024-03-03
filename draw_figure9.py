import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

plt.rcParams['agg.path.chunksize'] = 60000

np.set_printoptions(suppress=True)

plt.style.use('ggplot')
sns.set_theme(style="ticks", palette="pastel")


size =20
dataset_list = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes","CS-Sensors",
                 "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"]

df = []
df1 = pd.read_csv("./data_draw/EPM-Education/epm_0.csv")
df2 = pd.read_csv("./data_draw/GW-Magnetic/syndata_magnetic0.csv")
df3 = pd.read_csv("./data_draw/Metro-Traffic/syndata_metro.csv")
df4 = pd.read_csv("./data_draw/Nifty-Stocks/syndata_stocks0.csv")
df5 = pd.read_csv("./data_draw/USGS-Earthquakes/syndata_earthquakes0.csv")
df6 = pd.read_csv("./data_draw/CS-Sensors/test.csv")
df7 = pd.read_csv("./data_draw/Cyber-Vehicle/syndata_vehicle0.csv")
df8 = pd.read_csv("./data_draw/TH-Climate/syndata_climate0.csv")
df9 = pd.read_csv("./data_draw/TY-Fuel/syndata_fuel0.csv")
df10 = pd.read_csv("./data_draw/TY-Transport/syndata_transport0.csv")
df11 = pd.read_csv("./data_draw/FANYP-Sensors/data_20230626_020000_1_2.csv")
df12 = pd.read_csv("./data_draw/TRAJET-Transport/trajet_0_2.csv")
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


dataset_list = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"]
title_i = ["a","b","c","d","e","f","g","h","i","j","k","l"]

length_x = 3
length_y = 4
fig, ax_arr = plt.subplots(length_x,length_y,figsize=(28,11))
my_palette=["#e31a1c", "#1178b4","#e31a1c","#ff7f00"]
fig.subplots_adjust(hspace=0.45)
fig.subplots_adjust(wspace=0.4)



count = 0
for dataset in dataset_list:
    dx = int(count / 4)
    dy = int(count % 4)

    data = df[count]

    if count == 10 or count == 11:
        delta_time = []
        for i in range(1,512):
            delta_time.append(data.loc[i, 'time'] - data.loc[i-1, 'time']+1)
        for i in range(1,512):
            data.loc[i, 'time'] = delta_time[i-1]+data.loc[i-1, 'time']

    data = data.drop_duplicates(subset='time')
    time_initial = data["time"][0]
    data.loc[:255, 'time'] = data.loc[:255, 'time'] - time_initial

    if count == 1:
        time_initial = data["time"][256]

    f=sns.lineplot(x='time',y='value',linewidth = 3,data=data[0:128],color="#3c78d8",dashes=False,ax=ax_arr[dx][dy])
    f.get_yaxis().get_major_formatter().set_scientific(False)
    if count != 10:
        f.get_xaxis().get_major_formatter().set_scientific(False)
    if count == 3:
        ax_arr[dx][dy].xaxis.set_major_locator(MaxNLocator(nbins=3)) 
    f.tick_params(labelsize = size)
    f.xaxis.label.set_size(size)
    f.yaxis.label.set_size(size)
    f.set_title("("+title_i[count] +") "+ dataset).set_fontsize(size)
    if count == 5:
        f.set_xlabel(f"Time(+1,634,662,800ms)")
    else:
        f.set_xlabel(f"Time(+{time_initial:,}ms)")
    f.set_ylabel("Value")
    count += 1

plt.savefig("./figs/new_datasets_value.eps",format='eps',dpi = 400,bbox_inches='tight')
plt.savefig("./figs/new_datasets_value.png", dpi = 400,bbox_inches='tight')