import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter
plt.style.use('ggplot')
import matplotlib
import math
import matplotlib.ticker as ticker
sns.set_theme(style="ticks", palette="pastel")
def log_scale_label(x, pos):
    return f'$10^{int(math.log10(x))}$'

size = 25
fmri = pd.read_csv("./compression_ratio/float_block_size_compression_ratio.csv")

sizes = []
markers_list = []
for i in range(2):
    sizes.append(5)
markers_list.append('o')
markers_list.append('^')
algorithm_order = ["REGER-32-FLOAT","REGER-64-DOUBLE"]
dataset_list = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes","CS-Sensors",
                 "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"] # "Vehicle-Charge","YZ-Electricity",
title_i = ["a","b","c","d","e","f","g","h","i","j","k","l"]

xticklabels_list = []
xticks_list = []
for i in range(4,14):
    xticklabels_list.append(r"$ 2^{{ {:2d} }}$".format(i))
    xticks_list.append(i)

size = 18
fig, ax = plt.subplots(figsize=(10, 4))

markers_list = ['o', '^', 's', 'P', '*', 'X', 'D', 'p', 'H', 'v', '<', '>']
my_palette = ["#1178b4", "#33a02c", "#ff7f00", "#6a3d9a", "#fb9a99", "#814a19", "#9dafff", "#e31a1c", "#333333", "#f032e6", "#fabebe", "#469990"]
fmri = fmri[fmri['Dataset'].isin(dataset_list)]

f = sns.lineplot(x="Block Size", y="Compression Ratio", hue="Dataset", hue_order=dataset_list,
                 markers=markers_list, markersize=10, style='Dataset', dashes=False, palette=my_palette,
                 data=fmri[fmri["Encoding"] == "REGER-32-FLOAT"], ax=ax, size='Dataset', sizes=[3])
ax.get_legend().remove()
f.tick_params(labelsize = size)
f.set_xticks(xticks_list)
f.set_xticklabels(xticklabels_list)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)


f.set_xlabel("Block Size")
f.set_ylabel("Compression Ratio")
f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
lines, labels = ax.get_legend_handles_labels()
f.set_ylim(0,1)
fig.legend(lines, labels, bbox_to_anchor=(0.48, 1.27), loc = 'upper center',fontsize=size,labelspacing=0.2,handletextpad=0.2,columnspacing =0.2,ncol=3)


fig.savefig("./figs/vary_block_size_float_4.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_block_size_float_4.png", dpi = 400,bbox_inches='tight')


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 3))

fig.subplots_adjust(wspace=0.35)

fmri = pd.read_csv("./compression_ratio/float_block_size_compression_time.csv")

markers_list = ['o', '^', 's', 'P', '*', 'X', 'D', 'p', 'H', 'v', '<', '>']
my_palette = ["#1178b4", "#33a02c", "#ff7f00", "#6a3d9a", "#fb9a99", "#814a19", "#9dafff", "#e31a1c", "#333333", "#f032e6", "#fabebe", "#469990"]
fmri = fmri[fmri['Dataset'].isin(dataset_list)]

f = sns.lineplot(x="Block Size", y="Compression Time", hue="Dataset", hue_order=dataset_list,
                 markers=markers_list, markersize=10, style='Dataset', dashes=False, palette=my_palette,
                 data=fmri[fmri["Encoding"] == "REGER-32-FLOAT"], ax=ax[0], size='Dataset', sizes=[3])
ax[0].get_legend().remove()
f.set_yscale("log")
f.yaxis.set_major_formatter(ticker.FuncFormatter(log_scale_label))
f.tick_params(labelsize = size)
f.set_xticks(xticks_list)
f.set_xticklabels(xticklabels_list)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
f_title = f.set_title("(a) Encoding Time")
f_title.set_fontsize(size)
f.set_xlabel("Block Size")
f.set_ylabel("Encoding Time (ns/block)")

fmri = pd.read_csv("./compression_ratio/float_block_size_memory.csv")

markers_list = ['o', '^', 's', 'P', '*', 'X', 'D', 'p', 'H', 'v', '<', '>']
my_palette = ["#1178b4", "#33a02c", "#ff7f00", "#6a3d9a", "#fb9a99", "#814a19", "#9dafff", "#e31a1c", "#333333", "#f032e6", "#fabebe", "#469990"]
fmri = fmri[fmri['Dataset'].isin(dataset_list)]
fmri=fmri[~((fmri['Block Size'] == 13) & (fmri['Dataset'] == 'Nifty-Stocks'))]

f = sns.lineplot(x="Block Size", y="Memory Size", hue="Dataset", hue_order=dataset_list,
                 markers=markers_list, markersize=10, style='Dataset', dashes=False, palette=my_palette,
                 data=fmri[fmri["Encoding"] == "REGER-32-FLOAT"], ax=ax[1], size='Dataset', sizes=[3])
ax[1].get_legend().remove()
f.set_yscale("log")
f.yaxis.set_major_formatter(ticker.FuncFormatter(log_scale_label))
f.tick_params(labelsize = size)
f.set_xticks(xticks_list)
f.set_xticklabels(xticklabels_list)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
f_title = f.set_title("(b) Memory Usage")
f_title.set_fontsize(size)
f.set_xlabel("Block Size")
f.set_ylabel("Memory Usage (bytes)")
lines, labels = ax[1].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.48, 1.47), loc = 'upper center',fontsize=19,labelspacing=0.2,handletextpad=0.2,columnspacing =0.2,ncol=3)


fig.savefig("./figs/vary_block_size_memory_and_time.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_block_size_memory_and_time.png", dpi = 400,bbox_inches='tight')