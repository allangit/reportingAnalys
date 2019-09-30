import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("001.csv")
x=len(data)

for i in range(2,30):

	if i<10:

		file="00"+str(i)+".csv"

	elif i>=10:

		file="0"+str(i)+".csv"

	temp_data=pd.read_csv(file)
	x2=len(temp_data)
	print "La suma es",x+x2

	full=pd.concat([data,temp_data],axis=0)

print full.shape
print full
