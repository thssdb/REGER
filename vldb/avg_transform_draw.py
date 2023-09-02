import os
import pandas as pd

path_datasets = 'C:/Users/Jinnsjao Shawl/Documents/GitHub/encoding-reorder/reorder/iotdb_datasets_lists'  # 文件目录
path_ratio = './compression_ratio/sota_ratio/'  # 文件目录
# path_rd_ratio =  'C:/Users/xiaoj/Documents/GitHub/encoding-reorder/vldb/compression_ratio/delta_reordering_ratio/'  # 文件目录
# path_rr_ratio =  r'./result_evaluation/compression_ratio/rr_float_ratio/'  # 文件目录
path_rd_ratio =  './compression_ratio/segment_test/' 
path_rr_ratio =  './compression_ratio/elf/'  # 文件目录
# path_rr_ratio =  'C:/Users/xiaoj/Documents/GitHub/encoding-reorder/vldb/compression_ratio/reger_ratio/'  # 文件目录

# path_delta_ratio =  'C:/Users/xiaoj/Documents/GitHub/encoding-reorder/vldb/compression_ratio/segment_test/'  # 文件目录
# path_regression_ratio =  'C:/Users/xiaoj/Documents/GitHub/encoding-reorder/vldb/compression_ratio/regression_ratio/'  # 文件目录
# path_top_k_ratio =  'C:/Users/xiaoj/Documents/GitHub/encoding-reorder/vldb/compression_ratio/windows_topk_revised/'  # 文件目录
# path_top_k_whole_ratio =  'C:/Users/xiaoj/Documents/GitHub/encoding-reorder/vldb/compression_ratio/reorder/'  # 文件目录
# path_tsdiff_ratio =  'C:/Users/xiaoj/Documents/GitHub/encoding-reorder/reorder/result_evaluation/compression_ratio/top_k_ts2diff/'  # 文件目录
# path_tsdiff_top_k_ratio =  'C:/Users/xiaoj/Documents/GitHub/encoding-reorder/reorder/result_evaluation/compression_ratio/ts2diff_topk/'  # 文件目录

df_result = pd.DataFrame(columns=['Encoding','Dataset','Compression Ratio'])
res_index = 0
for root_r, dir_r, files_r in os.walk(path_datasets):
    # for j in range(1):
    for j in range(len(dir_r)):
        dir_ratio = path_ratio + dir_r[j] + "_ratio.csv"
        df = pd.read_csv(dir_ratio)
        df_avg = df.groupby(by = df['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        len_6_df = df_avg.shape[0]

        dir_ratio_rd = path_rd_ratio + dir_r[j] + "_ratio.csv"
        df_rd = pd.read_csv(dir_ratio_rd)
        df_rd['Encoding Algorithm'] = df_rd['Encoding Algorithm'].replace('REGER', 'REGER (our)')
        df_avg_rd = df_rd.groupby(by = df_rd['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # for k in range(df_avg_rd.shape[0]):
        #     df_avg_rd.loc[k,"CR"] = df_avg_rd.iloc[k,4] / (8*df_avg_rd.iloc[k,3])        
        len_rd_df = df_avg_rd.shape[0]

        dir_ratio_rr = path_rr_ratio + dir_r[j] + "_ratio.csv"
        df_rr = pd.read_csv(dir_ratio_rr)
        # df_rr = df_rr[df_rr['Encoding Algorithm'] == "ElfCompressor"]
        df_rr['Encoding Algorithm'] = df_rr['Encoding Algorithm'].replace('ElfCompressor', 'Elf')
        df_avg_rr = df_rr.groupby(by = df_rr['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # print(df_avg_rr)
        # for k in range(df_avg_rr.shape[0]):
        #     df_avg_rr.loc[k,"CR"] = df_avg_rr.iloc[k,4] / (8*df_avg_rr.iloc[k,3])
        len_rr_df = df_avg_rr.shape[0]

        # dir_ratio_delta = path_delta_ratio + dir_r[j] + "_ratio.csv"
        # df_delta = pd.read_csv(dir_ratio_delta)
        # df_avg_delta = df_delta.groupby(by = df_delta['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # # for k in range(df_avg_rd.shape[0]):
        # #     df_avg_rd.loc[k,"CR"] = df_avg_rd.iloc[k,4] / (8*df_avg_rd.iloc[k,3])        
        # len_delta_df = df_avg_delta.shape[0]

        # dir_ratio_regression = path_regression_ratio + dir_r[j] + "_ratio.csv"
        # df_regression = pd.read_csv(dir_ratio_regression)
        # df_avg_regression = df_regression.groupby(by = df_regression['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # # for k in range(df_avg_rd.shape[0]):
        # #     df_avg_rd.loc[k,"CR"] = df_avg_rd.iloc[k,4] / (8*df_avg_rd.iloc[k,3])        
        # len_regression_df = df_avg_regression.shape[0]

        # dir_top_k_ratio = path_top_k_ratio + dir_r[j] + "_ratio.csv"
        # df_top_k = pd.read_csv(dir_top_k_ratio)
        # df_top_k['Encoding Algorithm'] = df_top_k['Encoding Algorithm'].replace('A-star-search', 'A-star-Top-K-0.05')
        # df_avg_top_k = df_top_k.groupby(by = df_top_k['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # # for k in range(df_avg_top_k.shape[0]):
        # #     df_avg_top_k.loc[k,"CR"] = df_avg_top_k.iloc[k,5] / (8*df_avg_top_k.iloc[k,4])        
        # len_top_k_df = df_avg_top_k.shape[0]

        # dir_top_k_whole_ratio = path_top_k_whole_ratio + dir_r[j] + "_ratio.csv"
        # df_top_k_whole = pd.read_csv(dir_top_k_whole_ratio)
        # df_avg_top_k_whole = df_top_k_whole.groupby(by = df_top_k_whole['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # # for k in range(df_avg_top_k_whole.shape[0]):
        # #     df_avg_top_k_whole.loc[k,"CR"] = df_avg_top_k_whole.iloc[k,5] / (8*df_avg_top_k_whole.iloc[k,4])        
        # len_top_k_whole_df = df_avg_top_k_whole.shape[0]

        # dir_ratio_tsdiff = path_tsdiff_ratio + dir_r[j] + "_ratio.csv"
        # df_tsdiff = pd.read_csv(dir_ratio_tsdiff)
        # df_avg_tsdiff = df_tsdiff.groupby(['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
                
        # # df_avg_tsdiff = df_tsdiff[ df_tsdiff['threshold']==0.05].groupby(['Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
        # # df_top_k['Encoding Algorithm'] = df_top_k['Encoding Algorithm'].replace('TS2DIFF-Top-K', 'A-star-Top-K-0.05') 
        # len_tsdiff_df = df_avg_tsdiff.shape[0]

        # dir_tsdiff_top_k_ratio = path_tsdiff_top_k_ratio + dir_r[j] + "_ratio.csv"
        # df_tsdiff_top_k = pd.read_csv(dir_tsdiff_top_k_ratio)
        # df_tsdiff_avg_top_k= df_tsdiff_top_k.groupby(by = df_tsdiff_top_k['Encoding Algorithm'], as_index=False).mean()
        # for k in range(df_tsdiff_avg_top_k.shape[0]):
        #     df_tsdiff_avg_top_k.loc[k,"CR"] = df_tsdiff_avg_top_k.iloc[k,6] / (8*df_tsdiff_avg_top_k.iloc[k,5])        
        # len_tsdiff_top_k_df = df_tsdiff_avg_top_k.shape[0]



        for i in range(len_6_df):
            cr = 1/df_avg.iloc[i,-1]
            df_result.loc[res_index] = [df_avg.iloc[i,0],dir_r[j],cr]
            res_index += 1
    
        
        for i in range(len_rd_df):
            cr = 1/df_avg_rd.iloc[i,-1]
            df_result.loc[res_index] = [df_avg_rd.iloc[i,0],dir_r[j],cr]
            res_index += 1

        for i in range(len_rr_df):
            cr = 1/df_avg_rr.iloc[i,-1]
            df_result.loc[res_index] = [df_avg_rr.iloc[i,0],dir_r[j],cr]
            res_index += 1

        # for i in range(len_delta_df):
        #     cr = 1/df_avg_delta.iloc[i,-1]
        #     df_result.loc[res_index] = [df_avg_delta.iloc[i,0],dir_r[j],cr]
        #     res_index += 1
        
        # for i in range(len_regression_df):
        #     cr = 1/df_avg_regression.iloc[i,-1]
        #     df_result.loc[res_index] = [df_avg_regression.iloc[i,0],dir_r[j],cr]
        #     res_index += 1
        # for i in range(len_top_k_df):
        #     # print(df_avg_top_k.iloc[i,-2])
        #     cr = 1/df_avg_top_k.iloc[i,-1]
        #     df_result.loc[res_index] = [df_avg_top_k.iloc[i,0],dir_r[j],cr]
        #     res_index += 1
        
        # for i in range(len_top_k_whole_df):
        #     # print(df_avg_top_k.iloc[i,-2])
        #     cr = 1/df_avg_top_k_whole.iloc[i,-1]
        #     df_result.loc[res_index] = [df_avg_top_k_whole.iloc[i,0],dir_r[j],cr]
        #     res_index += 1

        # for i in range(len_tsdiff_df):
        #     cr = 1/df_avg_tsdiff.iloc[i,-1]
        #     df_result.loc[res_index] = [df_avg_tsdiff.iloc[i,0],dir_r[j],cr]
        #     res_index += 1
        # for i in range(len_tsdiff_top_k_df):
        #     # print(df_avg_top_k.iloc[i,-2])
        #     cr = 1/df_tsdiff_avg_top_k.iloc[i,-2]
        #     df_result.loc[res_index] = [df_tsdiff_avg_top_k.iloc[i,0],dir_r[j],cr]
        #     res_index += 1


# dir_ratio_rr = path_rr_ratio + "elf.csv"
# df_rr = pd.read_csv(dir_ratio_rr)
# df_rr = df_rr[df_rr['Encoding Algorithm'] == "ElfCompressor"]
# df_rr['Encoding Algorithm'] = df_rr['Encoding Algorithm'].replace('ElfCompressor', 'Elf')
# df_avg_rr = df_rr.groupby(by = ['Input Direction','Encoding Algorithm'], as_index=False).agg(lambda x: x.mean() if pd.api.types.is_numeric_dtype(x) else x)
# len_rr_df = df_avg_rr.shape[0]
# # print(df_avg_rr)
# for i in range(len_rr_df):
#     cr = 1/(df_avg_rr.iloc[i,-1]*2)
#     df_result.loc[res_index] = [df_avg_rr.iloc[i,1],df_avg_rr.iloc[i,0],cr]
#     res_index += 1

df_result.to_csv("./compression_ratio.csv",index=False)