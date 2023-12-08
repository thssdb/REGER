import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter
plt.style.use('ggplot')
import matplotlib
sns.set_theme(style="ticks", palette="pastel")


fmri = pd.read_csv("./compression_ratio/float_block_size_compression_ratio.csv")

size = 20
fig, ax = plt.subplots(figsize=(10, 5))
dataset_list = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes","CS-Sensors",
                 "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"]
xticklabels_list = []
xticks_list = []
for i in range(4,14):
    xticklabels_list.append(r"$ 2^{{ {:2d} }}$".format(i))
    xticks_list.append(i)
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
fig.legend(lines, labels, bbox_to_anchor=(0.5, 1.2), loc = 'upper center',fontsize=size,labelspacing=0.2,handletextpad=0.2,columnspacing =0.8,ncol=3)


fig.savefig("./figs/vary_block_size_float_4.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_block_size_float_4.png", dpi = 400,bbox_inches='tight')
