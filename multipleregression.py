import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


data=pd.read_csv("Advertising.csv")
print data.head()


print "\n\nmodelo de regresion lineal usando el meltodo de statsmodels\n\n"
lm=smf.ols(formula="Sales~TV",data=data).fit()
print lm.params
print "\n\nSales=7.032594+0.047537*TV\n\n"
print lm.pvalues
print lm.rsquared
print lm.summary()

sales_pred=lm.predict(pd.DataFrame(data["TV"]))

print sales_pred
data.plot(kind="scatter",x="TV", y= "Sales")
plt.plot(pd.DataFrame(data["TV"]),sales_pred,c="red",linewidth=3)
data["prediccion"]=7.032594+0.047537*data["TV"]
data["RSE"]=(data["Sales"]-data["prediccion"])**2
SSD=sum(data["RSE"])
RSE=np.sqrt(SSD/(len(data)-2))
sales_m=np.mean(data["Sales"])
error=RSE/sales_m
print RSE,error
print data.head()


print "\n\nRegresion multiple ventas~TV~Newspaper\n\n"

lm2=smf.ols(formula="Sales~TV+Newspaper",data=data).fit()
print "\nParamentros::",lm2.params
print "\nLos pvalores son los siguientes::\n",lm2.pvalues
print "El modelo es el siguiente>> 5.77+0.0469TV+0.044219Newspaper\n"
sales_pred2=lm2.predict(data[["TV","Newspaper"]])
print sales_pred2
SSD2=sum((data["Sales"]-sales_pred2)**2)
print "\nSSD3::",SSD2
RSE=np.sqrt(SSD2/(len(data)-2-1))
print RSE
error2=RSE/sales_m
print RSE,error2
print lm2.summary()

print "\n\n Add another model ecuation RADIO  and TV\n\n"

lm3=smf.ols(formula="Sales~TV+Radio",data=data).fit()
print "\nParamentros::",lm3.params
print "\nLos pvalores son los siguientes::\n",lm3.pvalues
print "El modelo es el siguiente>> 5.77+0.0469TV+0.044219Newspaper\n"
sales_pred3=lm3.predict(data[["TV","Radio"]])
print sales_pred3
SSD3=sum((data["Sales"]-sales_pred3)**2)
print "\nSSD3::",SSD3
RSE=np.sqrt(SSD3/(len(data)-2-1))
print RSE
error3=RSE/sales_m
print RSE,error3
print lm3.summary()

print "\n\n\nPROBLEMAS CON LA MULTICOLINALIDAD\n\n\n"

lm_tv=smf.ols(formula="TV~Newspaper+Radio",data=data).fit()
rsquaredtv=lm_tv.rsquared
VIF1=1/(1-rsquaredtv)
print "\n\nTV::",VIF1

lm_newspaper=smf.ols(formula="Newspaper~Radio+TV",data=data).fit()
rsquarednewspaper=lm_newspaper.rsquared
VIF2=1/(1-rsquarednewspaper)
print "\n\nperiodico\n\n", VIF2

lm_radio=smf.ols(formula="Radio~TV+Newspaper",data=data).fit()
rsradio=lm_radio.rsquared
VIF3=1/(1-rsradio)
print "\n\nRadio\n\n",VIF3
plt.show()
