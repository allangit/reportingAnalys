import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn


data=pd.read_csv("CustomerChurnModel.txt")
ldata=len(data)
print ldata
print "\n\nDividir usando la distribucion normal\n\n"
check=[]
check2=[]
a=np.random.randn(ldata)

for i in range(ldata):

	if(a[i] <= 0.8):

		check.append(a[i])
	else:

		check2.append(a[i])


print "\n\nImprimiendo los vectores\n\n"
print len(check2)
print len(check)
print check[:100]
plt.hist(check)
plt.show()
