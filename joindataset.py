import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data_main=pd.read_csv("Medals.csv")
print data_main.head()
a=data_main["Athlete"].unique().tolist()
print "Valor de a::",len(a)

data_country=pd.read_csv("Athelete_Country_Map.csv")
print data_country.head()
print len(data_country)
duplicado=data_country[data_country["Athlete"]=="Aleksandar Ciric"]
print duplicado

data_sport=pd.read_csv("Athelete_Sports_Map.csv")
print data_sport.head()
print len(data_sport)
duplicado2=data_sport[(data_sport["Athlete"]=="Chen Jing") | ( data_sport["Athlete"]=="Richard Thompson") |
		       (data_sport["Athlete"]=="Matt Ryan")]
print duplicado2


data_country_dp=data_country.drop_duplicates(subset="Athlete")
data_sport_dp=data_sport.drop_duplicates(subset="Athlete")
print len(data_country_dp)
print len(data_sport_dp)





data_main_country=pd.merge(left=data_main, right=data_country_dp, left_on="Athlete", right_on="Athlete")
print data_main_country.head()
print data_main_country.shape
print data_main_country[data_main_country["Athlete"]=="Aleksandar Ciric"]

data_finaly=pd.merge(left=data_main_country, right=data_sport_dp, left_on="Athlete", right_on="Athlete")

print data_finaly.head()
print data_finaly.shape
