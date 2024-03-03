import os
import pandas as pd

dir_r = ["EPM-Education","GW-Magnetic","Metro-Traffic", "Nifty-Stocks", "USGS-Earthquakes", "Vehicle-Charge",
         "CS-Sensors", "Cyber-Vehicle", "TH-Climate", "TY-Fuel","TY-Transport","YZ-Electricity","FANYP-Sensors","TRAJET-Transport"]

path_ratio = './compression_ratio/sota_ratio/' 
path_rr_ratio =  './compression_ratio/elf/'  
path_remove_value =  './compression_ratio/reger_float/'  
path_tods_ratio =  './compression_ratio/tods_ratio/'

df_result = pd.DataFrame(columns=['Encoding','Dataset','Encoding Time'])
result_count = 0

for j in range(len(dir_r)):
    dir_ratio = path_ratio + dir_r[j] + "_ratio.csv"
    df = pd.read_csv(dir_ratio)
    for k in range(df.shape[0]):
        df.loc[k,"Encode"] = df.iloc[k,4] / df.iloc[k,6]
    df_avg = df.groupby(by = df['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_6_df = df_avg.shape[0]


    dir_ratio_rr = path_rr_ratio + dir_r[j] + "_ratio.csv"
    df_rr = pd.read_csv(dir_ratio_rr)
    df_rr['Encoding Algorithm'] = df_rr['Encoding Algorithm'].replace('ElfCompressor', 'Elf')
    for k in range(df_rr.shape[0]):
        df_rr.loc[k,"Encode"] = df_rr.iloc[k,2] / 1000 #df_rr.iloc[k,4] 
    df_avg_rr = df_rr.groupby(by = df_rr['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rr_df = df_avg_rr.shape[0]


    dir_ratio_pfor = path_remove_value + dir_r[j] + "_ratio.csv"
    df_pfor = pd.read_csv(dir_ratio_pfor)
    df_pfor['Encoding Algorithm'] = df_pfor['Encoding Algorithm'].replace('REGER', 'REGER (our)')
    for k in range(df_pfor.shape[0]):
        df_pfor.loc[k,"Encode"] = df_pfor.iloc[k,2] / df_pfor.iloc[k,4]
    df_avg_pfor = df_pfor.groupby(by = df_pfor['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pfor_df = df_avg_pfor.shape[0]

    dir_ratio_tods = path_tods_ratio + dir_r[j] + "_ratio.csv"
    df_tods = pd.read_csv(dir_ratio_tods)
    for k in range(df_tods.shape[0]):
        df_tods.loc[k,"Encode"] = df_tods.iloc[k,4] / df_tods.iloc[k,6]
    df_avg_tods = df_tods.groupby(by = df_tods['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)      
    len_tods_df = df_avg_tods.shape[0]


    for i in range(len_6_df):
        cr = df_avg.iloc[i,-1]
        df_result.loc[result_count] = [df_avg.iloc[i,0],dir_r[j],cr]
        result_count += 1

    
    for i in range(len_rr_df):
        cr = df_avg_rr.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_rr.iloc[i,0],dir_r[j],cr]
        result_count += 1        


    for i in range(len_pfor_df):
        cr = df_avg_pfor.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_pfor.iloc[i,0],dir_r[j],cr]
        result_count += 1

    for i in range(len_tods_df):
        cr = df_avg_tods.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_tods.iloc[i,0],dir_r[j],cr]
        result_count += 1


df_result.to_csv("./compression_ratio/encode_time.csv",index=False)


df_result = pd.DataFrame(columns=['Encoding','Dataset','Decoding Time'])
result_i = 0

for j in range(len(dir_r)):

    dir_ratio = path_ratio + dir_r[j] + "_ratio.csv"
    df = pd.read_csv(dir_ratio)
    for k in range(df.shape[0]):
        df.loc[k,"Decode"] = df.iloc[k,5] / df.iloc[k,6]
    df_avg = df.groupby(by = df['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_6_df = df_avg.shape[0]


    dir_ratio_rr = path_rr_ratio + dir_r[j] + "_ratio.csv"
    df_rr = pd.read_csv(dir_ratio_rr)
    df_rr['Encoding Algorithm'] = df_rr['Encoding Algorithm'].replace('ElfCompressor', 'Elf')
    for k in range(df_rr.shape[0]):
        df_rr.loc[k,"Decode"] = df_rr.iloc[k,3] / 1000 #df_rr.iloc[k,4] 
    df_avg_rr = df_rr.groupby(by = df_rr['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_rr_df = df_avg_rr.shape[0]

    dir_ratio_pfor = path_remove_value + dir_r[j] + "_ratio.csv"
    df_pfor = pd.read_csv(dir_ratio_pfor)
    df_pfor['Encoding Algorithm'] = df_pfor['Encoding Algorithm'].replace('REGER', 'REGER (our)')
    for k in range(df_pfor.shape[0]):
        df_pfor.loc[k,"Encode"] = df_pfor.iloc[k,3] / df_pfor.iloc[k,4]
    df_avg_pfor = df_pfor.groupby(by = df_pfor['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
    len_pfor_df = df_avg_pfor.shape[0]

    dir_ratio_tods = path_tods_ratio + dir_r[j] + "_ratio.csv"
    df_tods = pd.read_csv(dir_ratio_tods)
    for k in range(df_tods.shape[0]):
        df_tods.loc[k,"Encode"] = df_tods.iloc[k,5] / df_tods.iloc[k,6]
    df_avg_tods = df_tods.groupby(by = df_tods['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)      
    len_tods_df = df_avg_tods.shape[0]


    for i in range(len_6_df):
        cr = df_avg.iloc[i,-1]
        df_result.loc[result_i] = [df_avg.iloc[i,0],dir_r[j],cr]
        result_i += 1
    

    for i in range(len_rr_df):
        cr = df_avg_rr.iloc[i,-1]
        df_result.loc[result_i] = [df_avg_rr.iloc[i,0],dir_r[j],cr]
        result_i += 1

    
    for i in range(len_pfor_df):
        cr = df_avg_pfor.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_pfor.iloc[i,0],dir_r[j],cr]
        result_count += 1
    
    for i in range(len_tods_df):
        cr = df_avg_tods.iloc[i,-1]
        df_result.loc[result_count] = [df_avg_tods.iloc[i,0],dir_r[j],cr]
        result_count += 1

df_result.to_csv("./compression_ratio/decode_time.csv",index=False)