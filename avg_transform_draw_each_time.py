import os
import pandas as pd

dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge",
         "CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity","FANYP-Sensors","TRAJET-Transport"]
 
path_time_ratio =  './compression_ratio/reger_sort_each_time/'  

df_result = pd.DataFrame(columns=['Part','Dataset','Encoding Time'])
res_index = 0

for j in range(len(dir_r)):


        dir_ratio_time = path_time_ratio + dir_r[j] + "_ratio.csv"
        df_time = pd.read_csv(dir_ratio_time)
        for k in range(df_time.shape[0]):
            df_time.loc[k,"Time_initial"] = df_time.iloc[k,7] / df_time.iloc[k,4]
            df_time.loc[k,"Value_initial"] = df_time.iloc[k,8] / df_time.iloc[k,4]
            df_time.loc[k,"Partition_initial"] = df_time.iloc[k,9] / df_time.iloc[k,4]
            df_time.loc[k,"Other"] = df_time.iloc[k,10] / df_time.iloc[k,4]

        df_avg_time = df_time.groupby(by = df_time['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_time_df = df_avg_time.shape[0]


        for i in range(len_time_df):
            df_result.loc[res_index] = ["Time Sort",dir_r[j],df_avg_time.iloc[i,-4]]
            res_index += 1
            df_result.loc[res_index] = ["Value Sort",dir_r[j],df_avg_time.iloc[i,-3]]
            res_index += 1
            df_result.loc[res_index] = ["Partition Sort",dir_r[j],df_avg_time.iloc[i,-2]]
            res_index += 1
            df_result.loc[res_index] = ["Move Points",dir_r[j],df_avg_time.iloc[i,-1]]
            res_index += 1


df_result.to_csv("./compression_ratio/each_time.csv",index=False)


