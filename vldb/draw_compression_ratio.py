from cProfile import label
import csv
from itertools import islice
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib
# from brokenaxes import brokenaxes

# plt.rcParams['pdf.fonttype'] = 42
# plt.rcParams['ps.fonttype'] = 42

# python result_ratio_vis.py
sns.set_theme(style="ticks", palette="pastel")
# my_palette=["#1178b4", "#33a02c","#e31a1c", "#ff7f00","#6a3d9a","#fb9a99", "#814a19"]
my_palette1 = ["#1178b4", "#33a02c", "#ff7f00","#6a3d9a","#fb9a99", "#814a19","#9dafff","#e31a1c","#333333"] #"CS-Sensors",EPM-Education",
dataset_list = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"] #  
#encoding_list = ["RAKE","GORILLA","RLBE","SPRINTZ","TS_2DIFF","RD","RR"]"REGER","REGER-DELTA",,"TS2DIFF-Top-K""REGER","REGER-DELTA",
# encoding_list = ["RLE","SPRINTZ","GORILLA","CHIMP","BUFF","Windows-Reorder"]#,"A-Star-Search-TopK","REGER-DELTA-2-Edges","REGER-DELTA-3-Edges"]"TS2DIFF-Top-K"]
encoding_list = ["RLE","SPRINTZ","GORILLA","CHIMP","BUFF","TS_2DIFF","Elf","REGER (our)"]#,"REGER-Test"
# 画压缩率的图
# "Reordering based on Regression""Reordering based on Delta"
df = pd.read_csv("./compression_ratio.csv")

size = 20

# plt.tick_params(labelsize=15)
#fig, ax_arr = plt.subplots(1,1, figsize=(28,12))
fig, ax_arr = plt.subplots(1,1, figsize=(28,5))

f = sns.barplot(x="Dataset", y="Compression Ratio",
            order = dataset_list,
            hue="Encoding",
            hue_order=encoding_list,
            palette=my_palette1,
            data=df,
            ax = ax_arr)
f.set_xticklabels(labels = dataset_list,  rotation=10)#
ax_arr.get_legend().remove()
f.tick_params(labelsize = size)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
# f.set_title("(a) Compression ratio").set_fontsize(20)
lines, labels = ax_arr.get_legend_handles_labels()
fig.legend(lines, labels,loc = 'upper center',fontsize=size,handletextpad=0.6,labelspacing=0.8,columnspacing =0.8, ncol=8)
# bbox_to_anchor=(0.45,1.45),
fig.savefig("./figs/vary_dataset_ratio.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_dataset_ratio.png", dpi = 400,bbox_inches='tight')

# plt.close()