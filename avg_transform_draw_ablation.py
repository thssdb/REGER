import os
import pandas as pd

dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge",
         "CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity","FANYP-Sensors","TRAJET-Transport"]
 
path_time_ratio =  './compression_ratio/reger_sort_time/'  
path_value_ratio =  './compression_ratio/reger_sort_value/'  
path_partition_ratio = './compression_ratio/reger_sort_partition/'
path_random_ratio =  './compression_ratio/reger_sort_random/'  
path_prune_ratio = './compression_ratio/reger_prune/'
path_all_ratio = './compression_ratio/reger/'

path_dir_list = [path_time_ratio,path_value_ratio,path_partition_ratio,path_random_ratio,path_prune_ratio,path_all_ratio] 

df_result = pd.DataFrame(columns=['Encoding','Dataset','Compression Ratio'])
res_index = 0

for j in range(len(dir_r)):

    for path_time_ratio in path_dir_list:
        dir_ratio_time = path_time_ratio + dir_r[j] + "_ratio.csv"
        df_time = pd.read_csv(dir_ratio_time)

        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER (PRUNE)', 'REGER-Pruned-Sort')
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER (prune)', 'REGER-Pruned-Sort')
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER', 'REGER-All-Sort')
        df_avg_time = df_time.groupby(by = df_time['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_time_df = df_avg_time.shape[0]


        for i in range(len_time_df):
            cr = df_avg_time.iloc[i,-1]
            df_result.loc[res_index] = [df_avg_time.iloc[i,0],dir_r[j],cr]
            res_index += 1
                

df_result.to_csv("./compression_ratio/compression_ratio_ablation.csv",index=False)

#----------------------------------------------------------------------------

df_result = pd.DataFrame(columns=['Encoding','Dataset','Encoding Time'])
res_index = 0

for j in range(len(dir_r)):

    for path_time_ratio in path_dir_list:
        dir_ratio_time = path_time_ratio + dir_r[j] + "_ratio.csv"
        df_time = pd.read_csv(dir_ratio_time)
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER (PRUNE)', 'REGER-Pruned-Sort')
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER (prune)', 'REGER-Pruned-Sort')
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER', 'REGER-All-Sort')
        for k in range(df_time.shape[0]):
            df_time.loc[k,"Encode"] = df_time.iloc[k,2] / df_time.iloc[k,4]
        df_avg_time = df_time.groupby(by = df_time['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_time_df = df_avg_time.shape[0]


        for i in range(len_time_df):
            cr = df_avg_time.iloc[i,-1]
            df_result.loc[res_index] = [df_avg_time.iloc[i,0],dir_r[j],cr]
            res_index += 1


df_result.to_csv("./compression_ratio/encode_time_ablation.csv",index=False)


#----------------------------------------------------------------------------

df_result = pd.DataFrame(columns=['Encoding','Dataset','Decoding Time'])
res_index = 0

for j in range(len(dir_r)):

    for path_time_ratio in path_dir_list:
        dir_ratio_time = path_time_ratio + dir_r[j] + "_ratio.csv"
        df_time = pd.read_csv(dir_ratio_time)
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER (PRUNE)', 'REGER-Pruned-Sort')
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER (prune)', 'REGER-Pruned-Sort')
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER', 'REGER-All-Sort')
        for k in range(df_time.shape[0]):
            df_time.loc[k,"Encode"] = df_time.iloc[k,3] / df_time.iloc[k,4]
        df_avg_time = df_time.groupby(by = df_time['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_time_df = df_avg_time.shape[0]


        for i in range(len_time_df):
            cr = df_avg_time.iloc[i,-1]
            df_result.loc[res_index] = [df_avg_time.iloc[i,0],dir_r[j],cr]
            res_index += 1


df_result.to_csv("./compression_ratio/decode_time_ablation.csv",index=False)