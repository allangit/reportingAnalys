import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("GenderPurchase.csv")
print df.head()
print df.columns.values
print df.shape

print "\n\nCreando una tabla de contingencia\n\n"

contigence=pd.crosstab(df["Gender"],df["Purchase"])
print contigence
print "\ningresaron a las tienda\n"
print contigence.sum(axis=1)
print "\nCompraron y no Compraron el producto\n"
print contigence.sum(axis=0)
print "\nProporcion de los que compraron\n"
print contigence.astype("float").div(contigence.sum(axis=1),axis=0)
