import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Crimes Per Capita by State')
st.subheader('The following selections allow you to view how states compare in terms of specific crimes and the categorization of crimes as Violent and Non-Violent Crime.')

df = pd.read_csv('data/crimedata.csv')


def graph_by_state(col, estimator='mean'):
    if estimator == 'mean':
        state = df.groupby('state')[col].mean().reset_index()
    elif estimator == 'median':
        state = df.groupby('state')[col].median().reset_index()
    elif estimator == 'sum':
        state = df.groupby('state')[col].sum().reset_index()
    else:
        print('estimator not recognized')
    state.sort_values(by=col, ascending=False, inplace=True)
    print(state)
    c = alt.Chart(state).mark_bar().encode(
        alt.X(col + ':Q'),
        alt.Y('state:O', sort='-x')
    ).properties(height=700)
    st.altair_chart(c)

#Set the NaN to 0
df['burglaries'] = df['burglaries'].fillna(0)
df['larcenies'] = df['larcenies'].fillna(0)
df['murders'] = df['murders'].fillna(0)
df['rapes'] = df['rapes'].fillna(0)
df['assaults'] = df['assaults'].fillna(0)
df['autoTheft'] = df['autoTheft'].fillna(0)
df['arsons'] = df['arsons'].fillna(0)
df['robberies'] = df['robberies'].fillna(0)

#Create column for Violent Crimes Total
df['ViolentCrimesTot'] = df['murders'] + df['rapes'] + df['robberies'] + df['assaults']

#Create column for Non Violent Crimes Total
df['NonViolentCrimesTot'] = df['burglaries'] + df['larcenies'] + df['autoTheft'] + df['arsons']

#Create calculated column for Violent Crimes Per Capita %
df['ViolentCrimePerCap'] = df['ViolentCrimesTot'] / df['population'] * 100
df['ViolentCrimePerCap'] = df['ViolentCrimePerCap'].round(2)

#Create calculated column for Non Violent Crimes Per Capita %
df['NonViolentCrimePerCap'] = df['NonViolentCrimesTot'] / df['population'] * 100
df['NonViolentCrimePerCap'] = df['NonViolentCrimePerCap'].round(2)

#Create per capita calculation for each crime
df['burglariesPerCap'] = df['burglaries'] / df['population'] * 100
df['burglariesPerCap'] = df['burglariesPerCap'].round(2)

df['larceniesPerCap'] = df['larcenies'] / df['population'] * 100
df['larceniesPerCap'] = df['larceniesPerCap'].round(2)

df['murdersPerCap'] = df['murders'] / df['population'] * 100
df['murdersPerCap'] = df['murdersPerCap'].round(2)

df['rapesPerCap'] = df['rapes'] / df['population'] * 100
df['rapesPerCap'] = df['rapesPerCap'].round(2)

df['assaultsPerCap'] = df['assaults'] / df['population'] * 100
df['assaultsPerCap'] = df['assaultsPerCap'].round(2)

df['autoTheftPerCap'] = df['autoTheft'] / df['population'] * 100
df['autoTheftPerCap'] = df['autoTheftPerCap'].round(2)

df['arsonsPerCap'] = df['arsons']/ df['population'] * 100
df['arsonsPerCap'] = df['arsonsPerCap'].round(2)

df['robberiesPerCap'] = df['robberies'] / df['population'] * 100
df['robberiesPerCap'] = df['robberiesPerCap'].round(2)

crimes = {
    'Murders': 'murdersPerCap',
    'Assaults': 'assaultsPerCap',
    'Robbery': 'robberiesPerCap',
    'Rapes': 'rapesPerCap',
    'Auto Theft':'autoTheftPerCap',
    'Larcenies': 'larceniesPerCap',
    'Burglaries': 'burglariesPerCap',
    'Arsons': 'arsonsPerCap',
    'Non-Violent Crimes': 'NonViolentCrimePerCap',
    'Violent Crimes': 'ViolentCrimePerCap'
}

opt1 = st.selectbox(label='Select a crime or category', options=list(crimes.keys()))
graph_by_state(crimes.get(opt1), 'mean')
