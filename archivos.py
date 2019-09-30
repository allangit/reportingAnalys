import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

df=pd.read_excel("titanic3.xls")
print df.shape
print df.head()
df.to_csv("alan.csv")
df.to_excel("alan.xls")
df.to_json("alan.json")
df2=pd.read_csv("alan.csv")
print df2.columns.values
print df2[["pclass", "survived"]]
plt.plot(df2["pclass"],df2[ "survived"])
plt.show()
