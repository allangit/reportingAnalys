import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data=pd.read_csv("Advertising.csv")
data["corrn"]=(data["TV"]-np.mean(data["TV"]))*(data["Sales"]-np.mean(data["Sales"]))
data["corre1"]=(data["TV"]-np.mean(data["TV"]))**2
data["corre2"]=(data["Sales"]-np.mean(data["Sales"]))**2
corr=sum(data["corrn"])/(np.sqrt(sum(data["corre1"])*sum(data["corre2"])))
print corr
print data.head()

def coeficientes(df,var1,var2):


	df["corrn"]=(df[var1]-np.mean(df[var1]))*(df[var2]-np.mean(df[var2]))
	df["corre1"]=(df[var1]-np.mean(df[var1]))**2
	df["corre2"]=(df[var2]-np.mean(df[var2]))**2
	corr=sum(df["corrn"])/(np.sqrt(sum(df["corre1"])*sum(df["corre2"])))

	return corr


print coeficientes(data,"TV","Sales")
print coeficientes(data,"Radio","Sales")


data2=pd.read_csv("Advertising.csv")
cols=data2.columns.values

print data2.corr()
for x in cols:
	for y in cols:

		print(x + ","+ y + " : "+ str(coeficientes(data2,x,y)))


figure,axs=plt.subplots(2,2, sharey=True, sharex=True)
data2.plot(kind="scatter",x="TV",y="Sales",ax=axs[0][0])
data2.plot(kind="scatter",x="Newspaper", y="Sales", ax=axs[0][1])
data2.plot(kind="scatter",x="Radio", y="Sales", ax= axs[1][0])
data2.plot(kind="scatter",x="TV",y="Radio",ax=axs[1][1])
plt.show()
