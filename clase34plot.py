import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv("CustomerChurnModel.txt")
print data.head()
print "\nimprimiendo los graficos\n"
figure,axs=plt.subplots(2,2, sharey=True, sharex=True)
data.plot(kind="scatter",x="Day Mins",y="Day Charge",ax=axs[0][0])
data.plot(kind="scatter",x="Night Mins", y="Night Charge", ax=axs[0][1])
data.plot(kind="scatter",x="Day Calls", y="Day Charge", ax= axs[1][0])
data.plot(kind="scatter",x="Night Calls",y="Night Charge",ax=axs[1][1])
plt.show()
