import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df=pd.read_csv("EcomExpense.csv")
print df.head()

dummy_gender=pd.get_dummies(df["Gender"],prefix="Gender")
dummy_city_tier=pd.get_dummies(df["City Tier"],prefix="City")
print dummy_gender.head()
print dummy_city_tier.head()

columns_names=df.columns.values.tolist()
print columns_names

df_new=df[columns_names].join(dummy_gender)
print df_new.head()


columns_names=df_new.columns.values.tolist()
df_new=df_new[columns_names].join(dummy_city_tier)
print df_new.head()
print df_new.columns.values


features_cols=["Monthly Income","Transaction Time","Gender_Female","Gender_Male","City_Tier 1","City_Tier 2","City_Tier 3","Record"]
x=df_new[features_cols]
y=df_new["Total Spend"]
lm=LinearRegression()
lm.fit(x,y)
print lm.intercept_
print lm.coef_
print lm.score(x,y)
df_new["prediccion"]=-79.41+0.1475*df_new["Monthly Income"]+0.1549*df_new["Transaction Time"]-131.025*df_new["Gender_Female"]+131.025*df_new["Gender_Male"]+76.76*df_new["City_Tier 1"]+55.13*df_new["City_Tier 2"]-131.9*df_new["City_Tier 3"]+772.23*df_new["Record"]
print df_new.head()
print "\n\nImprimiendo la prediccion y la confiabilidad del metodo\n\n"
SSD=np.sum((df_new["prediccion"]-df_new["Total Spend"])**2)
RSE=np.sqrt(SSD/(len(df_new)-len(features_cols)-1))
sales_mean=np.mean(df_new["Total Spend"])
error=RSE/sales_mean
print SSD
print RSE
print sales_mean
print error
print df_new[["Total Spend","prediccion"]].head()
print "\n\nImprimiendo con el el metodo de predict\n\n"
df_new["prediccion2"]=lm.predict(pd.DataFrame(df_new[features_cols]))
print df_new["prediccion2"].head()

