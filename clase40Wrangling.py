import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv("CustomerChurnModel.txt")
account_len=data["Account Length"]
print account_len.head()
print type(account_len)
subset=data[["Account Length","Phone","Eve Charge","Day Calls"]]
print subset.head()
print type(subset)
desired_columns=["Account Length","Phone","Eve Charge","Day Calls"]
subset2=data[desired_columns]
print subset2.head()
