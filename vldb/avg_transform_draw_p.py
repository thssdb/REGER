import os
import pandas as pd

path_datasets = './iotdb_datasets_lists/'  # 文件目录
path_rr_ratio_int =  './compression_ratio/p_int/'  # 文件目录
path_rr_ratio_float =  './compression_ratio/p_float/'  # 文件目录
path_rr_ratio_double =  './compression_ratio/p_double/'  # 文件目录


# path_rr_ratio =  'C:/Users/xiaoj/Documents/GitHub/encoding-reorder/vldb/compression_ratio/segment_size_only_segment/'  # 文件目录

df_result = pd.DataFrame(columns=['Encoding','Dataset','p','Compression Ratio'])
index_re = 0
for root_r, dir_r, files_r in os.walk(path_datasets):
    # for j in range(1):
    for j in range(len(dir_r)):

        # dir_ratio_rd = path_rr_ratio_int + dir_r[j] + "_ratio.csv"
        # df_rd = pd.read_csv(dir_ratio_rd)
        # df_avg_rd = df_rd.groupby(['Encoding Algorithm','p'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # # print(df_avg_rd)
        # len_rd_df = df_avg_rd.shape[0]

        dir_ratio_rr_float = path_rr_ratio_float + dir_r[j] + "_ratio.csv"
        df_rr_float = pd.read_csv(dir_ratio_rr_float)
        df_avg_rr_float = df_rr_float.groupby(['Encoding Algorithm','p'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_rr_float_df = df_avg_rr_float.shape[0]

        dir_ratio_rr_double = path_rr_ratio_double + dir_r[j] + "_ratio.csv"
        df_rr_double = pd.read_csv(dir_ratio_rr_double)
        df_avg_rr_double = df_rr_double.groupby(['Encoding Algorithm','p'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_rr_double_df = df_avg_rr_double.shape[0]

         

        # for i in range(len_rd_df):
        #     cr = 1/df_avg_rd.iloc[i,-1]
        #     df_result.loc[index_re] = [df_avg_rd.iloc[i,0],dir_r[j],df_avg_rd.iloc[i,1],cr]
        #     index_re += 1
        
        for i in range(len_rr_float_df):
            cr = 1/df_avg_rr_float.iloc[i,-1]
            df_result.loc[index_re] = [df_avg_rr_float.iloc[i,0],dir_r[j],df_avg_rr_float.iloc[i,1],cr]
            index_re += 1

        for i in range(len_rr_double_df):
            cr = 1/df_avg_rr_double.iloc[i,-1]
            df_result.loc[index_re] = [df_avg_rr_double.iloc[i,0],dir_r[j],df_avg_rr_double.iloc[i,1],cr]
            index_re += 1




df_result.to_csv('./compression_ratio/p_compression_ratio.csv',index=False)