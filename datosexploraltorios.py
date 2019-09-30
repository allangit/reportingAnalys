



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("bank.csv",sep=";")
print df.head()
print df.shape
print df.columns.values
df["yes"]=(df["y"]=="yes").astype(int)
df["education"]=np.where(df["education"]=="basic.4y","Basic",df["education"])
pd.crosstab(df.education, df.y).plot(kind="bar")
plt.title("Frecuencia de compra en funcion del nivel de educacion")
plt.xlabel("Nivel de educacion")
plt.ylabel("Frecuencia de compra del producto")
plt.show()

