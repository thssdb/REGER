import os
import pandas as pd

dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge",
         "CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity","FANYP-Sensors","TRAJET-Transport"]
path_ratio = './compression_ratio/sota_ratio/'  
path_rr_ratio =  './compression_ratio/elf/'  
path_remove_value_ratio =  './compression_ratio/reger_float/'  
path_tods_ratio =  './compression_ratio/tods_ratio/'

path_dir_list = [path_ratio,path_rr_ratio,path_remove_value_ratio,path_tods_ratio] 
df_result = pd.DataFrame(columns=['Encoding','Dataset','Compression Ratio'])
res_index = 0

for j in range(len(dir_r)):


    for path_time_ratio in path_dir_list:
        dir_ratio_time = path_time_ratio + dir_r[j] + "_ratio.csv"
        df_time = pd.read_csv(dir_ratio_time)
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('ElfCompressor', 'Elf')
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER', 'REGER (our)') 
        df_avg_time = df_time.groupby(by = df_time['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_time_df = df_avg_time.shape[0]


        for i in range(len_time_df):
            cr = df_avg_time.iloc[i,-1]
            df_result.loc[res_index] = [df_avg_time.iloc[i,0],dir_r[j],cr]
            res_index += 1


df_result.to_csv("./compression_ratio/compression_ratio.csv",index=False)

df_result = pd.DataFrame(columns=['Encoding','Dataset','Encoding Time'])
res_index = 0
for j in range(len(dir_r)):

    for path_time_ratio in path_dir_list:
        dir_ratio_time = path_time_ratio + dir_r[j] + "_ratio.csv"
        df_time = pd.read_csv(dir_ratio_time)
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('ElfCompressor', 'Elf')
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER', 'REGER (our)') 
        if df_time['Encoding Algorithm'][0] == 'Elf':
            for k in range(df_time.shape[0]):
                df_time.loc[k,"Encode"] = df_time.iloc[k,2] / 1000
        elif df_time['Encoding Algorithm'][0] == 'REGER (our)':
            for k in range(df_time.shape[0]):
                df_time.loc[k,"Encode"] = df_time.iloc[k,2] / df_time.iloc[k,4]
        else:
            for k in range(df_time.shape[0]):
                df_time.loc[k,"Encode"] = df_time.iloc[k,4] / df_time.iloc[k,6]

        df_avg_time = df_time.groupby(by = df_time['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_time_df = df_avg_time.shape[0]


        for i in range(len_time_df):
            cr = df_avg_time.iloc[i,-1]
            df_result.loc[res_index] = [df_avg_time.iloc[i,0],dir_r[j],cr]
            res_index += 1

df_result.to_csv("./compression_ratio/encode_time.csv",index=False)

df_result = pd.DataFrame(columns=['Encoding','Dataset','Decoding Time'])
res_index = 0
for j in range(len(dir_r)):

    for path_time_ratio in path_dir_list:
        dir_ratio_time = path_time_ratio + dir_r[j] + "_ratio.csv"
        df_time = pd.read_csv(dir_ratio_time)
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('ElfCompressor', 'Elf')
        df_time['Encoding Algorithm'] = df_time['Encoding Algorithm'].replace('REGER', 'REGER (our)') 
        if df_time['Encoding Algorithm'][0] == 'Elf':
            for k in range(df_time.shape[0]):
                df_time.loc[k,"Encode"] = df_time.iloc[k,3] / 1000
        elif df_time['Encoding Algorithm'][0] == 'REGER (our)':
            for k in range(df_time.shape[0]):
                df_time.loc[k,"Encode"] = df_time.iloc[k,3] / df_time.iloc[k,4]
        else:
            for k in range(df_time.shape[0]):
                df_time.loc[k,"Encode"] = df_time.iloc[k,5] / df_time.iloc[k,6]

        df_avg_time = df_time.groupby(by = df_time['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_time_df = df_avg_time.shape[0]


        for i in range(len_time_df):
            cr = df_avg_time.iloc[i,-1]
            df_result.loc[res_index] = [df_avg_time.iloc[i,0],dir_r[j],cr]
            res_index += 1

df_result.to_csv("./compression_ratio/decode_time.csv",index=False)