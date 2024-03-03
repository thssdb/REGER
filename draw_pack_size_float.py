import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter
plt.style.use('ggplot')
import matplotlib

# "Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Cyber-Vehicle", "TH-Climate", "TY-Fuel", "TY-Transport"
sns.set_theme(style="ticks", palette="pastel")


fmri = pd.read_csv("./compression_ratio/float_pack_size_compression_ratio.csv")

sizes = []
markers_list = []
for i in range(2):
    sizes.append(5)
markers_list.append('o')
markers_list.append('^')
algorithm_order = ["REGER-32-FLOAT","REGER-64-DOUBLE"]
dataset_list = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "CS-Sensors", "Cyber-Vehicle", 
                "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"] #"Vehicle-Charge","YZ-Electricity",
title_i = ["a","b","c","d","e","f","g","h","i","j","k","l"]

xticklabels_list = []
xticks_list = []
for i in range(3,9):
    xticklabels_list.append(r"$ 2^{{ {:2d} }}$".format(i))
    xticks_list.append(i)

length_x = 6
length_y = 2
fig, ax_arr = plt.subplots(length_x,length_y,figsize=(14,34))
fig.subplots_adjust(hspace=0.5)
fig.subplots_adjust(wspace=0.25)

size = 18
fig, ax = plt.subplots(figsize=(10, 4))

markers_list = ['o', '^', 's', 'P', '*', 'X', 'D', 'p', 'H', 'v', '<', '>']
my_palette = ["#1178b4", "#33a02c", "#ff7f00", "#6a3d9a", "#fb9a99", "#814a19", "#9dafff", "#e31a1c", "#333333", "#f032e6", "#fabebe", "#469990"]
fmri = fmri[fmri['Dataset'].isin(dataset_list)]

f = sns.lineplot(x="Pack Size", y="Compression Ratio", hue="Dataset", hue_order=dataset_list,
                 markers=markers_list, markersize=10, style='Dataset', dashes=False, palette=my_palette,
                 data=fmri[fmri["Encoding"] == "REGER-32-FLOAT"], ax=ax, size='Dataset', sizes=[3])
ax.get_legend().remove()
f.tick_params(labelsize = size)
f.set_xticks(xticks_list)
f.set_xticklabels(xticklabels_list)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
f.set_xlabel("Pack Size")
f.set_ylabel("Compression Ratio")
f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
f.set_ylim(0,1)
lines, labels = ax.get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.48, 1.27), loc = 'upper center',fontsize=size,labelspacing=0.2,handletextpad=0.2,columnspacing =0.2,ncol=3)


fig.savefig("./figs/vary_pack_size_float_4.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_pack_size_float_4.png", dpi = 400,bbox_inches='tight')


fmri = pd.read_csv("./compression_ratio/p_compression_ratio.csv")


xticklabels_list = []
xticks_list = []
for i in range(1,10):
    xticklabels_list.append(r"$ {{ {:2d} }}$".format(i))
    xticks_list.append(i)

length_x = 6
length_y = 2
fig, ax_arr = plt.subplots(length_x,length_y,figsize=(14,34))
fig.subplots_adjust(hspace=0.5) # middle gap ----
fig.subplots_adjust(wspace=0.25) # center gap ｜｜｜｜


fig, ax = plt.subplots(figsize=(10, 4))

fmri = fmri[fmri['Dataset'].isin(dataset_list)]

f = sns.lineplot(x="p", y="Compression Ratio", hue="Dataset", hue_order=dataset_list,
                 markers=markers_list, markersize=10, style='Dataset', dashes=False, palette=my_palette,
                 data=fmri[fmri["Encoding"] == "REGER-32-FLOAT"], ax=ax, size='Dataset', sizes=[3])
ax.get_legend().remove()
f.tick_params(labelsize = size)
f.set_xticks(xticks_list)
f.set_xticklabels(xticklabels_list)
f.xaxis.label.set_size(size)
f.yaxis.label.set_size(size)
f.set_ylim(0,1)
f.set_xlabel("p")
f.set_ylabel("Compression Ratio")
f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

lines, labels = ax.get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.48, 1.27), loc = 'upper center',fontsize=size,labelspacing=0.2,handletextpad=0.2,columnspacing =0.2,ncol=3)


fig.savefig("./figs/vary_p_4.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_p_4.png", dpi = 400,bbox_inches='tight')
