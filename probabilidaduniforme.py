import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


a=1
b=100
n=200000

data=np.random.uniform(a,b,n)
plt.title("Probabilidad vs muestras")
plt.hist(data)
plt.show()
