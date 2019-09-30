import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("titanic3.csv")
print data.tail()
print data.shape
print data.columns.values

print "\nResumen de los estadisticos basicos\n"
print data.describe()
print data.dtypes
print "\n\nTratamiendo de los datos \n\n"

print "primera forma de borrar all"
data3=data.dropna(axis=0, how="all")
print data3.head()
print"\nBorrar datos con any\n"
data4=data.dropna(axis=0, how="any")
print data4
data5=data.fillna(0)
print "\nrellenando los datos con 0\n"
print data5
data6=data.fillna("Desconocido")
print "\nRellenando con datos deconocidos\n"
print data6


