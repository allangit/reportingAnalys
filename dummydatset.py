import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.DataFrame (

		{
			'A':np.random.randn(10),
			'B':1.5+2.5*np.random.randn(10),
			'C':np.random.uniform(5,32,10)
		}
)

print data.head()
print data.shape
print data.columns.values
print data.describe()


df=pd.read_csv("CustomerChurnModel.txt")
columns_names=df.columns.values.tolist()
print columns_names
a=len(columns_names)
print a

new_data=pd.DataFrame(

	{

		"Columns names":columns_names,
		'A':np.random.randn(a),
                'B':np.random.uniform(0,1,a)



	}
)

print new_data
