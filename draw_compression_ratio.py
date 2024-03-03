import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="ticks", palette="pastel")

my_palette1 = ["#39A0DC","#0f6692", "#33a02c", "#ff7f00","#6a3d9a","#fb9a99", "#814a19","#9dafff","#e31a1c"] #"CS-Sensors",EPM-Education",
dataset_list = ["EPM-Education", "GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "CS-Sensors", 
                "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"] #,"YZ-Electricity" ,"Vehicle-Charge",
encoding_list = ["RLE","VORTEX","SPRINTZ","GORILLA","CHIMP","Elf","BUFF","TS_2DIFF","REGER (our)"]#"REGER-Remove-Value",,"REGER-Test"

df = pd.read_csv("./compression_ratio/compression_ratio.csv")

size = 20


fig, ax_arr = plt.subplots(1,1, figsize=(28,5))

f = sns.barplot(x="Dataset", y="Compression Ratio",
            order = dataset_list,
            hue="Encoding",
            hue_order=encoding_list,
            palette=my_palette1,
            data=df,
            ax = ax_arr)
f.set_xticklabels(labels = dataset_list,  rotation=10, ha='right')#
ax_arr.get_legend().remove()
f.tick_params(labelsize = size)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
f.set_ylim(0,1)

lines, labels = ax_arr.get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.52, 1.01),loc = 'upper center',fontsize=size,handletextpad=0.6,labelspacing=0.8,columnspacing =0.8, ncol=9)

fig.savefig("./figs/vary_dataset_ratio.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_dataset_ratio.png", dpi = 400,bbox_inches='tight')


df = pd.read_csv("./compression_ratio/encode_time.csv")


# size = 20

fig, ax_arr = plt.subplots(1,1, figsize=(28,5))

f = sns.barplot(x="Dataset", y="Encoding Time",
            order = dataset_list,
            hue="Encoding",
            hue_order=encoding_list,
            palette=my_palette1,
            data=df,
            ax = ax_arr)
ax_arr.set_yscale("log")
f.set_xticklabels(labels = dataset_list,  rotation=10, ha='right')
ax_arr.get_legend().remove()
f.tick_params(labelsize = size)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
f.set_ylabel("Encoding Time (ns/point)")

lines, labels = ax_arr.get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.52, 1.01),loc = 'upper center',fontsize=size,handletextpad=0.6,labelspacing=0.8,columnspacing =0.8, ncol=9)


fig.savefig("./figs/vary_dataset_time.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_dataset_time.png", dpi = 400,bbox_inches='tight')

df = pd.read_csv("./compression_ratio/decode_time.csv")


# size = 20


fig, ax_arr = plt.subplots(1,1, figsize=(28,5))
f = sns.barplot(x="Dataset", y="Decoding Time",
            order = dataset_list,
            hue="Encoding",
            hue_order=encoding_list,
            palette=my_palette1,
            data=df,
            ax = ax_arr)
ax_arr.set_yscale("log")
f.set_xticklabels(labels = dataset_list,  rotation=10, ha='right')
ax_arr.get_legend().remove()
f.tick_params(labelsize = size)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
f.set_ylabel("Decoding Time (ns/point)")
f.set_ylim(0.9,900)

lines, labels = ax_arr.get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.52, 1.01),loc = 'upper center',fontsize=size,handletextpad=0.6,labelspacing=0.8,columnspacing =0.8, ncol=9)


fig.savefig("./figs/vary_dataset_time_decode.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_dataset_time_decode.png", dpi = 400,bbox_inches='tight')