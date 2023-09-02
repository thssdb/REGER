import os
import pandas as pd

path_datasets = './iotdb_datasets_lists/'  # 文件目录
path_rd_ratio =  './compression_ratio/block_size_test/'  # 文件目录
path_rr_ratio =  './compression_ratio/block_size_only_segment/'  # 文件目录
# path_rd_ratio =  r'./result_evaluation/vary_parameter/rd_ratio/'  # 文件目录
# path_rr_float_ratio = 
# path_rr_int_ratio =  r'./result_evaluation/vary_parameter/rr_int_ratio/'  # 文件目录
# path_rr_ratio =  r'./result_evaluation/vary_parameter/rr_double_ratio/'  # 文件目录
# path_rd_ratio =  r'./result_evaluation/vary_parameter/rd_ratio/'  # 文件目录
df_result = pd.DataFrame(columns=['Encoding','Dataset','Block Size','Compression Ratio'])
index_re = 0
for root_r, dir_r, files_r in os.walk(path_datasets):
    # for j in range(1):
    for j in range(len(dir_r)):

        dir_ratio_rd = path_rd_ratio + dir_r[j] + "_ratio.csv"
        df_rd = pd.read_csv(dir_ratio_rd)
        df_avg_rd = df_rd.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # print(df_avg_rd)
        len_rd_df = df_avg_rd.shape[0]

        dir_ratio_rr_float = path_rr_ratio + dir_r[j] + "_ratio.csv"
        df_rr_float = pd.read_csv(dir_ratio_rr_float)
        df_avg_rr_float = df_rr_float.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_rr_float_df = df_avg_rr_float.shape[0]

        # dir_ratio_rr_int = path_rr_int_ratio + dir_r[j] + "_ratio.csv"
        # df_rr_int = pd.read_csv(dir_ratio_rr_int)
        # df_avg_rr_int = df_rr_int.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # len_rr_int_df = df_avg_rr_int.shape[0]

        # dir_ratio_rr = path_rr_ratio + dir_r[j] + "_ratio.csv"
        # df_rr = pd.read_csv(dir_ratio_rr)
        # df_avg_rr = df_rr.groupby(['Encoding Algorithm','Block Size'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # len_rr_df = df_avg_rr.shape[0]
        
        # len_all = len_rr_df + len_rr_float_df + len_rr_int_df
         
        
        # for i in range(len_rr_df):
        #     cr = 1/df_avg_rr.iloc[i,-1]
        #     # df_avg_rr.iloc[i,0]
        #     df_result.loc[index_re] = [df_avg_rr.iloc[i,0],dir_r[j],df_avg_rr.iloc[i,1],cr]
        #     index_re += 1

        for i in range(len_rd_df):
            cr = 1/df_avg_rd.iloc[i,-1]
            df_result.loc[index_re] = [df_avg_rd.iloc[i,0],dir_r[j],df_avg_rd.iloc[i,1],cr]
            index_re += 1
        
        for i in range(len_rr_float_df):
            cr = 1/df_avg_rr_float.iloc[i,-1]
            df_result.loc[index_re] = [df_avg_rr_float.iloc[i,0],dir_r[j],df_avg_rr_float.iloc[i,1],cr]
            index_re += 1

        # for i in range(len_rr_int_df):
        #     cr = 1/df_avg_rr_int.iloc[i,-1]
        #     df_result.loc[index_re] = [df_avg_rr_int.iloc[i,0],dir_r[j],df_avg_rr_int.iloc[i,1],cr]
        #     index_re += 1



        
# print(df_result)
df_result.to_csv('./compression_ratio/block_size_compression_ratio.csv',index=False)