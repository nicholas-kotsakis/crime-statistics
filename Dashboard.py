import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Crime Dashboard",
) 

st.title("Crime Dashboard")
st.subheader('Overview of State Metrics')

df = pd.read_csv("data/crimedata.csv")

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

states = df.groupby('state').agg({'population':'sum',
                                'racepctblack':'mean',
                                'racePctWhite':'mean',
                                'racePctAsian':'mean',
                                'racePctHisp':'mean',
                                'householdsize':'mean',
                                'medIncome':'mean',
                                'medFamInc':'mean',
                                'PctPopUnderPov':'mean',
                                'PctVacantBoarded':'mean', 
                                'MedYrHousBuilt':'mean',
                                'NumInShelters':'sum',
                                'ViolentCrimePerCap':'mean',
                                'NonViolentCrimePerCap':'mean',
                                'ViolentCrimesTot':'sum',
                                'NonViolentCrimesTot':'sum',
                                'burglaries':'sum',
                                'larcenies':'sum',
                                'murders':'sum',
                                'rapes':'sum',
                                'assaults':'sum',
                                'autoTheft':'sum',
                                'arsons':'sum',
                                'robberies':'sum',
                                'PopDens':'mean'}).reset_index()


state = st.selectbox(label='State', options=df['state'].sort_values().unique())
dash_state = states[states['state'] == state]

col1, col2, col3 = st.columns(3)
col1.metric("Population (Sample Size)",round(dash_state['population'],2))
col2.metric("Population Density",round(dash_state['PopDens'],2))
col3.metric("Household Size",round(dash_state['householdsize'],2))

col1.metric("Non Violent Crimes Per Capita",round(dash_state['NonViolentCrimePerCap'],2))
col2.metric("Violent Crimes Per Capita",round(dash_state['ViolentCrimePerCap'],2))
col3.metric("Total Crimes Per Capita",round(dash_state['ViolentCrimePerCap'] + dash_state['NonViolentCrimePerCap'],2))

col1.metric("Median Income",round(dash_state['medIncome'],2))
col2.metric("Median Family Income",round(dash_state['medFamInc'],2))
col3.metric("% Population Under Poverty",round(dash_state['PctPopUnderPov'],2))

col1.metric("Number In Shelters",round(dash_state['NumInShelters'],2))
col2.metric("% Vacant Boarded Homes",round(dash_state['PctVacantBoarded'], 2))
col3.metric("Median Home Age (Years)",round(2018-dash_state['MedYrHousBuilt'], 2))
