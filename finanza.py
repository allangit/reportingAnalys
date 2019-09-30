import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl
import datetime as dt
import pandas_datareader.data as web
from matplotlib.pyplot import style
style.use('ggplot')

start=dt.datetime(2012,1,1)
end=dt.datetime(2015,1,1)

df=web.DataReader('TSLA','yahoo',start,end)
print df.head()
df.to_csv('tsla.csv')

df2=pd.read_csv("tsla.csv")
df2.plot()
plt.show()
