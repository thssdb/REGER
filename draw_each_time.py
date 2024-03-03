import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="ticks", palette="pastel")

my_palette1 = ["#1178b4", "#33a02c", "#ff7f00","#6a3d9a","#fb9a99", "#814a19","#9dafff","#e31a1c","#333333"] #"CS-Sensors",EPM-Education",
dataset_list = ["EPM-Education", "GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "CS-Sensors", 
                "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"] #,"YZ-Electricity" ,"Vehicle-Charge",
encoding_list = ["RLE","SPRINTZ","GORILLA","CHIMP","Elf","BUFF","TS_2DIFF","REGER (our)"]#"REGER-Remove-Value",,"REGER-Test"
encoding_list = ['REGER (our)',"REGER-Time-Sort","REGER-Value-Sort","REGER-Partition-Sort","REGER-Random-Sort"]
encoding_list = ["Time Sort","Value Sort","Partition Sort","Move Points"]

# ---------------------------------------------------------------
df = pd.read_csv("./compression_ratio/each_time.csv")
size = 20

fig, ax_arr = plt.subplots(1,1, figsize=(14,4))
f = sns.barplot(x="Dataset", y="Encoding Time",
            order = dataset_list,
            hue="Part",
            hue_order=encoding_list,
            palette=my_palette1,
            data=df,
            ax = ax_arr)
f.set_xticklabels(labels = dataset_list,  rotation=20,ha="right")
ax_arr.get_legend().remove()
f.tick_params(labelsize = size)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
f.set_ylabel("Time Cost (ns/point)")
f.set_ylim(0.9,170.1)

lines, labels = ax_arr.get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.5, 0.9),loc = 'upper center',fontsize=size,handletextpad=0.6,labelspacing=0.8,columnspacing =0.8, ncol=4)


fig.savefig("./figs/each_time.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/each_time.png", dpi = 400,bbox_inches='tight')
