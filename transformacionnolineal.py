import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

data=pd.read_csv("autompg.csv")
print data.head()
data["mpg"]=data["mpg"].dropna()
data["horsepower"]=data["horsepower"].dropna()
plt.plot(data["horsepower"], data["mpg"],"ro")
plt.xlabel("Caballos de potencia")
plt.ylabel("Consumo millas por Galeon")
plt.title("CV vs MPG")

x=data["horsepower"].fillna(data["horsepower"].mean())
y=data["mpg"].fillna(data["mpg"].mean())
lm=LinearRegression()

x_data=x[:,np.newaxis]
lm.fit(x_data,y)
print lm.score(x_data,y)
plt.plot(x,y,"ro")
plt.plot(x,lm.predict(x_data),color='blue')

SSD=np.sum((y-lm.predict(x_data))**2)
RSE=np.sqrt(SSD/(len(x_data)-1))
sales_mean=np.mean(y)
error=RSE/sales_mean
print SSD,RSE,sales_mean,error

poly=PolynomialFeatures(degree=2)
x_data=poly.fit_transform(x_data)
lm=linear_model.LinearRegression()
lm.fit(x_data,y)
print lm.score(x_data,y)
print lm.intercept_
print lm.coef_


plt.show()

