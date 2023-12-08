import os
import pandas as pd

dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes",
         "CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"]
path_ratio = './compression_ratio/sota_ratio/'  
path_rr_ratio =  './compression_ratio/elf/'  
path_remove_value_ratio =  './compression_ratio/reger_float/'  


df_result = pd.DataFrame(columns=['Encoding','Dataset','Compression Ratio'])
res_index = 0

for j in range(len(dir_r)):
    dir_ratio = path_ratio + dir_r[j] + "_ratio.csv"
    df = pd.read_csv(dir_ratio)
    df_avg = df.groupby(by = df['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_6_df = df_avg.shape[0]


    dir_ratio_rr = path_rr_ratio + dir_r[j] + "_ratio.csv"
    df_rr = pd.read_csv(dir_ratio_rr)
    df_rr['Encoding Algorithm'] = df_rr['Encoding Algorithm'].replace('ElfCompressor', 'Elf')
    df_avg_rr = df_rr.groupby(by = df_rr['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rr_df = df_avg_rr.shape[0]

    dir_ratio_delta = path_remove_value_ratio + dir_r[j] + "_ratio.csv"
    df_delta = pd.read_csv(dir_ratio_delta)
    df_delta['Encoding Algorithm'] = df_delta['Encoding Algorithm'].replace('REGER', 'REGER (our)') 
    df_avg_delta = df_delta.groupby(by = df_delta['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)      
    len_delta_df = df_avg_delta.shape[0]




    for i in range(len_6_df):
        cr = 1/df_avg.iloc[i,-1]
        df_result.loc[res_index] = [df_avg.iloc[i,0],dir_r[j],cr]
        res_index += 1

    for i in range(len_rr_df):
        cr = 1/df_avg_rr.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_rr.iloc[i,0],dir_r[j],cr]
        res_index += 1

    for i in range(len_delta_df):
        cr = 1/df_avg_delta.iloc[i,-1]
        df_result.loc[res_index] = [df_avg_delta.iloc[i,0],dir_r[j],cr]
        res_index += 1
        

df_result.to_csv("./compression_ratio/compression_ratio.csv",index=False)