import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=open("CustomerChurnModel.txt",'r')
cols=data.readline().strip().split(",")
n_cols=len(cols)
print n_cols
counter=0
main_dict={}

for col in cols:

	main_dict[col]=[]

for line in data:

	values=line.strip().split(",")

	for i in range(n_cols):

		main_dict[cols[i]].append(values[i])
	counter+=1

print counter, n_cols

df=pd.DataFrame(main_dict)
print df.head()

