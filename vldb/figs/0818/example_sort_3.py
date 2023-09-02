import numpy as np
import pandas as pd

f=open("result_evaluation/example100/100.csv","r")
g1=open("result_evaluation/example100/100_reorder_time.csv","w")
g2=open("result_evaluation/example100/100_reorder_value.csv","w")

data=f.readlines()

time1=[]
value1=[]
time2=[]
value2=[]

for i in range(1,len(data)):
    li = data[i][:-1].split(",")
    if int(li[1])<2000:
        value2.append(int(li[1]))
        time2.append(int(li[0]))
    else:
        value1.append(int(li[1]))
        time1.append(int(li[0]))
print(value1)
print(value2)

for tmp in time2:
    time1.append(tmp)
for tmp in value2:
    value1.append(tmp)
print(value1)

g1.write("Order,Timestamp"+"\n")
g2.write("Order,Value"+"\n")
for i in range(len(time1)):
    line1=str(i+1)+","+str(time1[i])+"\n"
    g1.write(line1)
    line2 = str(i + 1) + "," + str(value1[i]) + "\n"
    g2.write(line2)