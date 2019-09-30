import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


data=pd.read_csv("Advertising.csv")
a=np.random.randn(len(data))
check= (a<0.8)
training=data[check]
testing=data[~check]
print len(data),len(training), len(testing)


lm=smf.ols(formula="Sales~TV+Radio",data=training).fit()
print lm.summary()
print "\nSales=2.93+0.056TV+0.1802Radio\n"
print "\n\nValidacion del modelo\n\n"


sales_pred=lm.predict(testing)
print sales_pred
SSD=sum((testing["Sales"]-sales_pred)**2)
RSE=np.sqrt(SSD/(len(testing)-2-1))
sales_mean=np.mean(testing["Sales"])
error=RSE/sales_mean

print "erro::",error
