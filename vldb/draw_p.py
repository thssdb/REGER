import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter
plt.style.use('ggplot')
import matplotlib

# "Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Cyber-Vehicle", "TH-Climate", "TY-Fuel", "TY-Transport"
sns.set_theme(style="ticks", palette="pastel")

# fig, ax_arr = plt.subplots(4,2,figsize=(15,21))
# #my_palette=["#1178b4", "#33a02c","#e31a1c", "#ff7f00"]#,"#6a3d9a","#fb9a99", "#814a19"]
# my_palette=["#1178b4", "#33a02c","#e31a1c"]
# fig.subplots_adjust(hspace=0.5)
# fig.subplots_adjust(wspace=0.2)
size = 25
fmri = pd.read_csv("./compression_ratio/p_compression_ratio.csv")
# x=['8','16','32','64','128','256','512']#
sizes = []
markers_list = []
for i in range(2):
    sizes.append(5)
markers_list.append('o')
markers_list.append('^')
algorithm_order = ["REGER-32-FLOAT","REGER-64-DOUBLE"]#"REGER-32-INT",,"REGER-Without-Reordering"]
dataset_list = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge","CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity"] 
title_i = ["a","b","c","d","e","f","g","h","i","j","k","l"]
xticklabels_list = []
xticks_list = []
for i in range(0,10):
    xticklabels_list.append(r"$ {{ {:2d} }}$".format(i))
    xticks_list.append(i)
length_x = 3
length_y = 4
fig, ax_arr = plt.subplots(length_x,length_y,figsize=(28,16))
my_palette=["#e31a1c", "#1178b4","#e31a1c","#ff7f00"]#,"#6a3d9a","#fb9a99"]#, "#814a19"]
fig.subplots_adjust(hspace=0.35)
fig.subplots_adjust(wspace=0.25)

count = 0
for dataset in dataset_list:
    dx = int(count / 4)
    dy = int(count % 4)
    f = sns.lineplot(x="p",y="Compression Ratio",hue="Encoding",hue_order=algorithm_order,
                        markers=markers_list,markersize=10,style='Encoding',dashes=False,palette=my_palette
                        ,data=fmri[fmri["Dataset"]==dataset],ax=ax_arr[dx][dy],size='Encoding',sizes=sizes)
    f.get_legend().remove()
    f.tick_params(labelsize = size)
    f.set_xticks(xticks_list)
    f.set_xticklabels(xticklabels_list)
    f.xaxis.label.set_size(size)
    f.yaxis.label.set_size(size)
    f_title = f.set_title("("+title_i[count] +") "+ dataset)
    f_title.set_fontsize(size)
    f.set_xlabel("p")
    f.set_ylabel("Compression Ratio")
    f.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    count += 1

lines, labels = ax_arr[0][0].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(0.5, 0.95), loc = 'upper center',fontsize=size,labelspacing=0.2,handletextpad=0.2,columnspacing =0.8,ncol=2)


fig.savefig("./figs/vary_p.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./figs/vary_p.png", dpi = 400,bbox_inches='tight')
