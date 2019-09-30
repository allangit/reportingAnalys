
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gender=["Male","Female"]
income=["Poor","Middle Class","Rich"]
n=500

gender_data=[]
income_data=[]

for i in range(0,n):


	gender_data.append(np.random.choice(gender))
	income_data.append(np.random.choice(income))

print gender_data[:10]
print income_data[:10]


height=160+30*np.random.randn(n)
weight=65+25*np.random.randn(n)
age=30+12*np.random.randn(n)
income=18000+3500*np.random.rand(n)


final_data=pd.DataFrame(


	{
		"Gender":gender_data,
		"Economic Status":income_data,
		"Height":height,
		"Weight":weight,
		"Age":age,
		"Income":income
	}
)


print final_data
print "\n\nDATOS OPERACIONES DATOS AGRUPADOS\n\n"

grouped_gender=final_data.groupby("Gender")
print grouped_gender.groups

for names, groups in grouped_gender:

	print names
	print groups


print "\n\nImpriendo solo un grupo\n\n"

print grouped_gender.get_group("Female")
double_group=final_data.groupby(["Gender","Economic Status"])


print "\n\n\ Imprmiendo por un double grupo\n\n"

for names,groups in double_group:


	print names
	print groups
