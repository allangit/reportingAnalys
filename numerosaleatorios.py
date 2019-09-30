import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def rand_int(n,a,b):

	x=[]

	for i in range(n):

		x.append(np.random.randint(a,b))

	return x


print rand_int(25,1,100)
print"\n\nGenerando la semilla aleatorio\n\n"

np.random.seed(2018)

for i in range(5):

	print (np.random.random())

