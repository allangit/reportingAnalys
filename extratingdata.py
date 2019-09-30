import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl
import datetime
import pandas_datareader.data as web
from matplotlib.pyplot import style
style.use('ggplot')

start=datetime.datetime(2012,1,1)
end=datetime.datetime(2015,1,1)


#df=quandl.get('WIKI/GOOGL')
#print df.head()
df=web.DataReader("XOM","yahoo",start,end)
print df.head()
df["Adj Close"].plot()
plt.show()

print "\n\nLeyendo un archivo html\n\n"

#state2=pd.read_html("https://sa.ufidelitas.ac.cr/login/login.aspx")
#print state2
#print state2.columns.values
#print state2.shape

#print state2[0][(state2[0]['Numberof Reps.'])> 10]

