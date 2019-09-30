import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("GenderPurchase.csv")
print df.head()

print "\n\nCreando la tabla de contigencia\n\n"

contigency_table=pd.crosstab(df["Gender"],df["Purchase"])
print contigency_table
print "\n\n"
print contigency_table.sum(axis=0)
print "\n\n"
print contigency_table.sum(axis=1)
print "\n\n"
print contigency_table.astype("float").div(contigency_table.sum(axis=1),axis=0)
