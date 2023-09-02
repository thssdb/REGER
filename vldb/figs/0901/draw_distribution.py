import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math
import os
from collections import Counter, OrderedDict

def get_count_i_j(i, j,value_counts_dict):
    count = 0
    i = int(i)
    j = int(j)
    for k in range(i+1,j+1):
        if k in value_counts_dict:
            count += value_counts_dict[k]
    # print(count)
    return count

def find_local_minima(x, y,value_counts_dict):
    minima_indices = []
    for i in range(1, len(y) - 1):
        l = len(minima_indices)
        if y[i] < y[i - 1] and y[i] < y[i + 1] :
            if l > 0:
                if  get_count_i_j(x[minima_indices[l-1]],x[i],value_counts_dict)>64 :
                    minima_indices.append(i)
            else:
                minima_indices.append(i)
    return minima_indices

plt.rc('axes.formatter', useoffset=False)


np.set_printoptions(suppress=True)

plt.style.use('ggplot')
sns.set_theme(style="ticks", palette="pastel")

df2 = pd.read_csv("./result_evaluation/example100/100_reorder_value.csv")
df1 = pd.read_csv("./result_evaluation/example100/100_reorder_time.csv")

merged_df = pd.concat([df1, df2], axis=1)
# print(merged_df)

fontsize = 25
plt.rcParams['axes.labelsize'] = fontsize
plt.rcParams['axes.titlesize'] = fontsize
plt.rcParams['xtick.labelsize'] = fontsize
plt.rcParams['ytick.labelsize'] = fontsize

values = df2.iloc[:1000,1].values


# 创建一个包含两个子图的图像
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
# 绘制差分值的分布图
# fig = plt.figure(figsize=(10, 6))
f = sns.histplot(values, bins=20, kde=True, ax=ax1,linewidth = 3,color="#3c78d8")#, color="blue"
# ax = f.gca()

# # 设置柱子颜色为"#3c78d8"
# for patch in ax.patches:
#     patch.set_facecolor("#3c78d8")
kde_curve = ax1.get_lines()[0].get_data()  # 获取第2条线，即KDE曲线
kde_x, kde_y = kde_curve[0], kde_curve[1]
value_counts = Counter(values)

# 打印频数和数值的映射
value_counts_dict = dict(value_counts)
print(value_counts_dict)
minima_indices = find_local_minima(kde_x, kde_y, value_counts_dict)
minima_points = [(kde_x[i], kde_y[i]) for i in minima_indices]
str_kde = ""
for value in minima_indices:
    str_kde += str(int(kde_x[value]))
    str_kde += ","
print(str_kde)
# 添加频数三等分点的竖线
for value in minima_indices:
    ax1.axvline(x=kde_x[value], color='red', linestyle='--')
ax1.set_title("(a) Partition") #Distribution of values
ax1.set_xlabel("Value")
ax1.set_ylabel("Frequency")
# ax1.tick_params(axis='x', rotation=45)

# (b) 子图 - values的折线图
ax2.plot(merged_df['Timestamp'],merged_df['Value'],marker='o',linewidth = 3,color="#3c78d8")
# ax2.plot(timestamps, values, marker='o')
for value in minima_indices:
    ax2.axhline(y=kde_x[value], color='red',  linestyle='--')
ax2.set_title("(b) Order") #Partition order
ax2.set_xlabel("Time")
ax2.set_ylabel("Value")
# ax2.tick_params(axis='x', rotation=45)
    

plt.tight_layout()
# plt.show()

fig.savefig("./fig/example_distribution.eps",format='eps',dpi = 400,bbox_inches='tight')
fig.savefig("./fig/example_distribution.png", dpi = 400,bbox_inches='tight')



# for dataset_i in range(len(dataset_list)):
    
#     dataset = dataset_list[dataset_i]
    # print(dataset)
    # if dataset_i != 3:
    #     continue


    # file_path = path_dir + dataset + "\\0.csv"
    

    # data = pd.read_csv(file_path)
    # # Extract the file name without extension

    # timestamps = data.iloc[:1000,0].values
    # values = data.iloc[:1000,1].values


    # # 创建一个包含两个子图的图像
    # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 12))
    # # 绘制差分值的分布图
    # # fig = plt.figure(figsize=(10, 6))
    # sns.histplot(values, bins=20, kde=True, ax=ax1,linewidth = 3,color="#3c78d8")#, color="blue"
    # kde_curve = ax1.get_lines()[0].get_data()  # 获取第2条线，即KDE曲线
    # kde_x, kde_y = kde_curve[0], kde_curve[1]
    # print(len(kde_x))
    # print(len(kde_y))
    # kde_interpolator = interpolate.interp1d(kde_x, kde_y)

    # # 计算两个点之间的分布积
    # x1 = kde_x[10]  # 第一个点的x坐标
    # x2 = kde_x[30]  # 第二个点的x坐标
    # integral_value = integrate.quad(kde_interpolator, x1, x2)[0]
    # print(integral_value)
    # value_counts = Counter(values)

    # # 打印频数和数值的映射
    # value_counts_dict = dict(value_counts)
    # minima_indices = find_local_minima(kde_x, kde_y, value_counts_dict)
    # # minima_points = [(kde_x[i], kde_y[i]) for i in minima_indices]
    # str_kde = ""
    # for value in minima_indices:
    #     str_kde += str(int(kde_x[value]))
    #     str_kde += ","
    # print(str_kde)

    # print(value_counts_dict[0])


    # plt.axvline(x=mean_diff - 3 * std_diff, color='red', linestyle='--', label='-3$\sigma$')
    # plt.axvline(x=mean_diff + 3 * std_diff, color='red', linestyle='--', label='+3$\sigma$')

    # quantiles = [ 1/3, 2/3, 1]
    # quantile_values = pd.qcut(values, q=quantiles, duplicates='drop').categories.mid
    # print(quantile_values)
    
    # quantile_values = [25,53]

    # # 添加频数三等分点的竖线
    # for value in minima_indices:
    #     ax1.axvline(x=kde_x[value], color='red', linestyle='--')
    # ax1.set_title("(a) Distribution of values in "+dataset)
    # ax1.set_xlabel("Values")
    # ax1.set_ylabel("Frequency")
    # # ax1.tick_params(axis='x', rotation=45)

    # # (b) 子图 - values的折线图
    # ax2.plot(timestamps, values, marker='o')
    # for value in minima_indices:
    #     ax2.axhline(y=kde_x[value], color='red', linestyle='--')
    # ax2.set_title("(b) Line Plot of Values")
    # ax2.set_xlabel("Timestamps")
    # ax2.set_ylabel("Values")
    # ax2.tick_params(axis='x', rotation=45)
        

    # plt.tight_layout()
    # # plt.show()
    
    # fig.savefig("./figs/example_sigma/"+dataset+"_example_values.eps",format='eps',dpi = 400,bbox_inches='tight')
    # fig.savefig("./figs/example_sigma/"+dataset+"_example_values.png", dpi = 400,bbox_inches='tight')


    # timestamps = data.iloc[:,0].values
    # values = data.iloc[:,1].values

    # # 创建一个DataFrame以存储排序后的数据
    # sorted_data = pd.DataFrame({'Timestamp': timestamps, 'Value': values})

    # # 按值（Value）从小到大对数据进行排序
    # sorted_data = sorted_data.sort_values(by='Value')

    # # 将结果保存到新的CSV文件中
    # sorted_file_path = path_dir + dataset + "\\1.csv"
    # sorted_data.to_csv(sorted_file_path, index=False)
    # print("1.csv")

    # sorted_data = pd.DataFrame(columns=['Timestamp', 'Value'])
    # for timestamp, value in zip(timestamps, values):
    #     if value > kde_x[len(minima_indices)-1]:
    #         sorted_data = pd.concat([sorted_data, pd.DataFrame({'Timestamp': [timestamp], 'Value': [value]})], ignore_index=True)

    # for iminima_i in range(len(minima_indices)-1,0,-1):
    #     for timestamp, value in zip(timestamps, values):
    #         if value <= kde_x[iminima_i] and value > kde_x[iminima_i-1]:
    #             sorted_data = pd.concat([sorted_data, pd.DataFrame({'Timestamp': [timestamp], 'Value': [value]})], ignore_index=True)
 
    # for timestamp, value in zip(timestamps, values):
    #     if value <= kde_x[0]:
    #         sorted_data = pd.concat([sorted_data, pd.DataFrame({'Timestamp': [timestamp], 'Value': [value]})], ignore_index=True)
    
    # sorted_file_path = path_dir + dataset + "\\2.csv"
    # sorted_data.to_csv(sorted_file_path, index=False)
    # print("2.csv")
