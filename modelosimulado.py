import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=1.5+2.5*np.random.randn(100)
res=0.8*np.random.randn(100)
y_pred=5+1.9*x
y_act=5+1.9*x+res

x_list=x.tolist()
y_pred_list=y_pred.tolist()
y_actual_list=y_act.tolist()


data=pd.DataFrame(

	{
		"x":x_list,
		"y_actual":y_actual_list,
		"y_prediccion":y_pred_list
	}
)

print data[10:100]
y_mean=[np.mean(y_act) for i in range(1,len(x_list)+1)]
plt.title("Metodo de modelo simulado con actual vs prediccion")
plt.xlabel("valores de X::")
plt.ylabel("Valores de Y::")
plt.plot(x,y_pred)
plt.plot(x,y_act,"ro")
plt.plot(x,y_mean)

data["SSR"]=(data["y_prediccion"]-np.mean(y_act))**2
data["SSD"]=(data["y_prediccion"]-data["y_actual"])**2
data["SST"]=(data["y_actual"]-np.mean(y_act))**2
SSR=sum(data["SSR"])
SSD=sum(data["SSD"])
SST=sum(data["SST"])
R2=SSR/SST
print SSR,SSD,SST,R2



print "\n\nModelo Regresion\n\n"
print data.head()

x_mean=np.mean(data["x"])
y_mean=np.mean(data["y_actual"])
data["beta_n"]=(data["x"]-x_mean)*(data["y_actual"]-y_mean)
data["beta_d"]=(data["x"]-x_mean)**2
beta=sum(data["beta_n"])/sum(data["beta_d"])
alpha=y_mean-beta*x_mean
print beta, alpha
print "\n\nModelo lineal es y=1.94553171644*x+ 5.01367432634136\n\n"
data["y_model"]=alpha+beta*data["x"]
print data.head()
plt.show()
