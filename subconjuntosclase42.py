import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv("CustomerChurnModel.txt")
print data.head()

data1=data[data["Day Mins"]>300]
print data1

print "\nUsuarios de NY\n\n"
data2=data[data["State"]=="NY"]
print data2

print "\n\nIprimiendo con los operadores logicos and or "
data3=data[(data["State"]=="NY") & (data["Day Mins"]>300)]
print data3

print"\n\nImprimiendo con el operador logico or\n\n"

data4=data[(data["State"]=="NY") | (data["Day Mins"]>300)]
print data4.shape

print "\n\nImprimiendo los datos Days call < nigth call\n\n"
data5=data[(data["Day Mins"]) < (data["Night Mins"])]
print data5.shape

print "\n\nImprimiendo por columnas\n\n"
subset_50=data[["Day Mins","Night Mins","Account Length"]][:50]
print subset_50
print subset_50.shape

print "\n\nUsando el metodo iloc para filtrado de : filas--columnas \n\n"
data6=data.iloc[1:10,3:6]
print data6

print "\n\nOtro metodo paara el filtrado usando mediante etiqueta fila --columna\n\n"
data7=data.loc[[1,5,8,36],["Area Code","VMail Plan","Day Mins"]]
print data7

print "\n\nCreando una columna en el dataset\n\n"
data["Total Mins"]=data["Day Mins"]+data["Night Mins"]+data["Eve Mins"]
data["Total Calls"]=data["Day Calls"]+data["Night Calls"]+data["Eve Calls"]
print data.shape
print data.head()



