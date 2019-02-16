# -*- coding: utf-8 -*-
import pandas as pd


df_chicago = pd.read_csv("chicago.csv")
df_nyc = pd.read_csv("new_york_city.csv")
df_washington = pd.read_csv("washington.csv")

print(df_chicago.head())
print(df_nyc.head())
print(df_washington.head())

print(df_nyc.info())
print(df_nyc.info())
print(df_washington.info())


print(df_nyc.columns)
print(df_nyc.columns)
print(df_washington.columns)
df.mode()