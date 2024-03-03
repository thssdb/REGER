import numpy as np
import pandas as pd
import seaborn as sns
import math
import matplotlib.pyplot as plt

plt.rcParams['agg.path.chunksize'] = 60000

np.set_printoptions(suppress=True)

plt.style.use('ggplot')
sns.set_theme(style="ticks", palette="pastel")

# fig, ax_arr = plt.subplots(6,2,figsize=(14,36))
# my_palette=["#1178b4", "#33a02c","#e31a1c", "#ff7f00"]#,"#6a3d9a","#fb9a99", "#814a19"]
# fig.subplots_adjust(hspace=0.3)
# fig.subplots_adjust(wspace=0.3)
size =25
dataset_list = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes","CS-Sensors",
                 "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"] # "Vehicle-Charge","YZ-Electricity",

df = []
df1 = pd.read_csv("./data_draw/EPM-Education/epm_0.csv")
df2 = pd.read_csv("./data_draw/GW-Magnetic/syndata_magnetic0.csv")
df3 = pd.read_csv("./data_draw/Metro-Traffic/syndata_metro.csv")
df4 = pd.read_csv("./data_draw/Nifty-Stocks/syndata_stocks0.csv")
df5 = pd.read_csv("./data_draw/USGS-Earthquakes/syndata_earthquakes0.csv")
# df6 = pd.read_csv("./data_draw/Vehicle-Charge/electric_vehicle_charging_2.csv")
df6 = pd.read_csv("./data_draw/CS-Sensors/test.csv")
df7 = pd.read_csv("./data_draw/Cyber-Vehicle/syndata_vehicle0.csv")
df8 = pd.read_csv("./data_draw/TH-Climate/syndata_climate0.csv")
df9 = pd.read_csv("./data_draw/TY-Fuel/syndata_fuel0.csv")
df10 = pd.read_csv("./data_draw/TY-Transport/syndata_transport0.csv")
# df12 = pd.read_csv("./data_draw/YZ-Electricity/0_2.csv")
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
# dataset_list = ["TY-Transport"]

title_i = ["a","b","c","d","e","f","g","h","i","j","k","l"]
# xticklabels_list = []
# xticks_list = []
# for i in range(0,10):
#     xticklabels_list.append(r"$ {{ {:2d} }}$".format(i))
#     xticks_list.append(i)
length_x = 3
length_y = 4
# fig, ax_arr = plt.subplots(length_x,length_y,figsize=(28,16))
#ax_arr.ticklabel_format(useOffset=False)
my_palette=["#e31a1c", "#1178b4","#e31a1c","#ff7f00"]#,"#6a3d9a","#fb9a99"]#, "#814a19"]
# fig.subplots_adjust(hspace=0.35)
# fig.subplots_adjust(wspace=0.5)

count = 0
for dataset in dataset_list:
    # dx = int(count / 4)
    # dy = int(count % 4)
    length = len(df[count])
    # print(length)
    block_num = int(length/1024)
    ratio_spread = 0
    ratio_variance = 0
    ratio_delta_mean = 0
    for i in range(block_num):
        # print(i)
        # print(df[count])
        cur_df = df[count][i*1024:(i+1)*1024]
        
        time_spread = cur_df['time'].max() - cur_df['time'].min()
        
        # normalized_time = (cur_df['time'] - cur_df['time'].min()) / (cur_df['time'].max() - cur_df['time'].min())
        
        # variance_normalized_time = normalized_time.var()
        
        # time_variance = cur_df['time'].var()
        value_spread = cur_df['value'].max() - cur_df['value'].min()
        cur_df_delta  = cur_df['value'].diff()
        cur_df_delta = cur_df_delta - cur_df_delta.min()
        
        delta_spread = cur_df_delta.max() - cur_df_delta.min() #0
        delta_mean = cur_df_delta.abs().mean()#-cur_df_delta.min()
        # if cur_df['value'].max() - cur_df['value'].min()!=0 :
        #     normalized_value = (cur_df['value'] - cur_df['value'].min()) / (cur_df['value'].max() - cur_df['value'].min())
        #     delta_spread = normalized_value.var()
        # value_variance = cur_df['value'].var()
        ratio_spread += (value_spread / time_spread)
        if value_spread != 0:
            ratio_variance += (delta_spread/value_spread)
            ratio_delta_mean += (delta_mean/value_spread)
        # ratio_variance += math.sqrt(delta_spread)
        # print(cur_df['value'].max() - cur_df['value'].min())
    ratio_spread /= block_num
    ratio_variance /= block_num
    ratio_delta_mean /=block_num

    print(f"{dataset_list[count]}  Spread: {ratio_spread:.3f}, Delta Spread/Spread: {ratio_variance:.3f},  Delta Mean: {ratio_delta_mean:.3f}")
    print("----------------------------------------------------------------------------")
    # print(length)

    # break
    # cur_df = df[count][:1024]
    # time_spread = cur_df['time'].max() - cur_df['time'].min()
    # time_variance = cur_df['time'].var()
    # print(f"{dataset_list[count]}  time : Spread: {time_spread},Variance: {time_variance}")
    # value_spread = cur_df['value'].max() - cur_df['value'].min()
    # value_variance = cur_df['value'].var()
    # print(f"{dataset_list[count]}  value: Spread: {value_spread},Variance: {value_variance}")
    # print(f"{dataset_list[count]}  Spread: {value_spread/time_spread},Variance: {math.sqrt(value_variance/time_variance)}")
    # print("----------------------------------------------------------------------------")


    count += 1

# plt.savefig("./figs/datasets_value_subgraph1000.eps",format='eps',dpi = 400,bbox_inches='tight')
# plt.savefig("./figs/datasets_value_subgraph1000.png", dpi = 400,bbox_inches='tight')
