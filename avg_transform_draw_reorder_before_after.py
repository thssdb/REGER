import os
import pandas as pd

dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge",
         "CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity","FANYP-Sensors","TRAJET-Transport"]
 
path_time_ratio =  './compression_ratio/reger_time_space_cost/'  
path_value_ratio =  './compression_ratio/reger_value_space_cost/'  
path_time_ratio_before =  './compression_ratio/reger_time_space_cost_before/'  
path_value_ratio_before =  './compression_ratio/reger_value_space_cost_before/'  
path_sota_ratio = './compression_ratio/sota_ratio/'

path_dir_list = [path_time_ratio,path_value_ratio,path_time_ratio_before,path_value_ratio_before]#,path_partition_ratio,path_random_ratio,path_prune_ratio] 

df_result = pd.DataFrame(columns=['Encoding','Dataset','Compression Ratio'])
res_index = 0

for j in range(len(dir_r)):

    for path_time_ratio in path_dir_list:
        dir_ratio_time = path_time_ratio + dir_r[j] + "_ratio.csv"
        df_time = pd.read_csv(dir_ratio_time)

        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('After-Reorder-Time', 'REGER-Time')
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('After-Reorder-Value', 'REGER-Value')
        df_avg_time = df_time.groupby(by = df_time['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_time_df = df_avg_time.shape[0]


        for i in range(len_time_df):
            cr = df_avg_time.iloc[i,-1]*4*1024
            df_result.loc[res_index] = [df_avg_time.iloc[i,0],dir_r[j],cr]
            res_index += 1
    dir_ratio_time = path_sota_ratio + dir_r[j] + "_ratio.csv"
    df_time = pd.read_csv(dir_ratio_time)
    df_time = df_time[df_time["Encoding Algorithm"]=="TS_2DIFF"]


    df_avg_time = df_time.groupby(by = ['Encoding Algorithm','Column Index'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_time_df = df_avg_time.shape[0]



    for i in range(len_time_df):
        cr = df_avg_time.iloc[i,-1]*4*1024
        if df_avg_time.iloc[i,1] == 0:
            df_result.loc[res_index] = ["TS_2DIFF-Time",dir_r[j],cr]
        if df_avg_time.iloc[i,1] == 1:
            df_result.loc[res_index] = ["TS_2DIFF-Value",dir_r[j],cr]
    
        res_index += 1
                

df_result.to_csv("./compression_ratio/compression_ratio_reoder_before_after.csv",index=False)

