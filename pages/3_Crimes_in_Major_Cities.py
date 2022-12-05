import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import seaborn as sns


import seaborn as sns
st.set_page_config(
    page_title="Major Crime Cities",
    page_icon="👋",
) 

st.header("Major Cities by Selected Crime")

st.subheader("The following chart compares the five largest by population.  Select a crime to view how the cities compare.")

df = pd.read_csv("data/crimedata.csv")

suffixes = ['township', 'city', 'borough']

for suffix in suffixes:
    df['communityName'] = df['communityName'].str.replace(suffix, '')

cities = df.iloc[[21,55,127,764,1581]].copy()
crimelist = {'murdPerPop':'Murders', 'rapesPerPop':'Rapes', 'robbbPerPop':'Robberies',
              'assaultPerPop': 'Assaults', 'burglPerPop':'Burglaries', 'larcPerPop':'Larcenies', 
              'autoTheftPerPop':'Auto Thefts', 'arsonsPerPop':'Arsons', 'ViolentCrimesPerPop':'ViolentCrimes',
              'nonViolPerPop':'Non violent crimes'}

crimekeys = list(crimelist.keys())
crimevalues = list(crimelist.values())
selected_crime = st.selectbox("Select a Crime",crimevalues)
crime = crimevalues.index(selected_crime)
plt.figure(figsize=(12,6))
sns.barplot(data=cities, x='communityName', y=crimekeys[crime])
plt.xlabel(None)
st.pyplot(plt)




