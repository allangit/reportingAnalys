import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=np.random.randn(1000)
x=range(1,101)
#plt.plot(x,data)
plt.hist(data)
plt.show()
