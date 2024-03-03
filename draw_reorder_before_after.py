import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="ticks", palette="pastel")

my_palette1 = ["#39A0DC","#33a02c", "#ff7f00","#6a3d9a","#fb9a99", "#814a19","#9dafff","#e31a1c"] #"CS-Sensors",EPM-Education",
dataset_list = ["EPM-Education", "GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "CS-Sensors", 
                "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"] #,"YZ-Electricity" ,"Vehicle-Charge",
encoding_list = ["RLE","VORTEX","SPRINTZ","GORILLA","CHIMP","Elf","BUFF","TS_2DIFF","REGER (our)"]#"REGER-Remove-Value",,"REGER-Test"
encoding_list = ["TS_2DIFF-Time","TS_2DIFF-Value","Before-Reorder-Time","Before-Reorder-Value","After-Reorder-Time","After-Reorder-Value"]
encoding_list = ["TS_2DIFF-Time","TS_2DIFF-Value","REGER-Time","REGER-Value"]

df = pd.read_csv("./compression_ratio/compression_ratio_reoder_before_after.csv")

size = 20


fig, ax_arr = plt.subplots(1,1, figsize=(14,4))

f = sns.barplot(x="Dataset", y="Compression Ratio",
            order = dataset_list,
            hue="Encoding",
            hue_order=encoding_list,
            palette=my_palette1,
            data=df,
            ax = ax_arr)
f.set_xticklabels(labels = dataset_list,  rotation=20, ha="right")#
ax_arr.get_legend().remove()
f.tick_params(labelsize = size)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
f.set_ylim(0,3600.1)
f.set_ylabel("Storage Usage (bytes)")

lines, labels = ax_arr.get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.51, 0.9),loc = 'upper center',fontsize=size,handletextpad=0.4,labelspacing=0.4,columnspacing =0.4, ncol=4)

fig.savefig("./figs/ratio_reorder_before_after.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/ratio_reorder_before_after.png", dpi = 400,bbox_inches='tight')
