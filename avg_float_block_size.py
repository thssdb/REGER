import os
import pandas as pd
dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes","CS-Sensors", 
         "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"]
path_rd_ratio =  './compression_ratio/block_size_float/' 

df_result = pd.DataFrame(columns=['Encoding','Dataset','Block Size','Compression Ratio'])
index_re = 0

for j in range(len(dir_r)):

    dir_ratio_rd = path_rd_ratio + dir_r[j] + "_ratio.csv"
    df_rd = pd.read_csv(dir_ratio_rd)
    df_avg_rd = df_rd.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    # print(df_avg_rd)
    len_rd_df = df_avg_rd.shape[0]



    for i in range(len_rd_df):
        cr = 1/df_avg_rd.iloc[i,-1]
        df_result.loc[index_re] = [df_avg_rd.iloc[i,0],dir_r[j],df_avg_rd.iloc[i,1],cr]
        index_re += 1
    

df_result.to_csv('./compression_ratio/float_block_size_compression_ratio.csv',index=False)