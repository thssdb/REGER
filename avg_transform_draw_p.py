import os
import pandas as pd

dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "CS-Sensors", 
         "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","FANYP-Sensors","TRAJET-Transport"]

path_rr_ratio_float =  './compression_ratio/p_float_vary_p/'  

df_result = pd.DataFrame(columns=['Encoding','Dataset','p','Compression Ratio'])
index_re = 0

for j in range(len(dir_r)):

    dir_ratio_rr_float = path_rr_ratio_float + dir_r[j] + "_ratio.csv"
    df_rr_float = pd.read_csv(dir_ratio_rr_float)
    df_avg_rr_float = df_rr_float.groupby(['Encoding Algorithm','p'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rr_float_df = df_avg_rr_float.shape[0]

        

    for i in range(len_rr_float_df):
        cr = 1/df_avg_rr_float.iloc[i,-1]
        df_result.loc[index_re] = [df_avg_rr_float.iloc[i,0],dir_r[j],df_avg_rr_float.iloc[i,1],cr]
        index_re += 1



df_result.to_csv('./compression_ratio/p_compression_ratio.csv',index=False)