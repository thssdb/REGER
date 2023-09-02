import pandas as pd

df5 = pd.read_csv("./result_evaluation/example100/100_reorder_time.csv")
df6 = pd.read_csv("./result_evaluation/example100/100_reorder_value.csv")
fontsize = 25

df5['Timestamp'] = df5['Timestamp'].values[::-1]
df6['Value'] = df6['Value'].values[::-1]

df5.to_csv("./result_evaluation/example100/100_reorder_reverse_time.csv",index=None)
df6.to_csv("./result_evaluation/example100/100_reorder_reverse_value.csv",index=None)