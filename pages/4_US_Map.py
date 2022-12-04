import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/crimedata.csv')

d = {'population':'Population', 'murdPerPop':'Murders','rapesPerPop':'Rape', 'robbbPerPop':'Robbery', 
    'assaultPerPop':'Assault', 'burglPerPop':'Burglary', 'larcPerPop':'Larceny', 'autoTheftPerPop':'Auto Theft',
    'arsonsPerPop':'Arson', 'nonViolPerPop': 'Nonviolent Crime', 'ViolentCrimesPerPop':'Violent Crime'}

df = df.groupby('state', as_index = False).agg({'population':'sum', 'murdPerPop':'mean','rapesPerPop':'mean',
                                                'robbbPerPop':'mean', 'assaultPerPop':'mean','burglPerPop':'mean',
                                                'larcPerPop':'mean', 'autoTheftPerPop':'mean', 'arsonsPerPop':'mean',
                                                'nonViolPerPop':'mean','ViolentCrimesPerPop':'mean'}).rename(columns=d)

df['Crime'] = df['Nonviolent Crime'] + df['Violent Crime']

df = df.round({'Crime': 3}) 
df = df.round({'Violent Crime':2})
df = df.round({'Nonviolent Crime':2})

highest_crime = df[['Murders', 'Rape', 'Robbery', 'Assault', 
            'Burglary', 'Larceny', 'Auto Theft', 'Arson']].idxmax(axis=1)

st.header("State Crime Data Per 100K Population")

st.subheader("Hover the map to view state crime data")

map = px.choropleth(df, 
                locations = 'state',
                color='Crime',
                color_continuous_scale="gnbu",
                locationmode='USA-states',
                scope="usa",
                range_color=(0, 10000),
                height=800,
                hover_name='state', hover_data=['Population', highest_crime],
                custom_data=['state', 'Population', highest_crime, 'Crime','Violent Crime','Nonviolent Crime'],
            )

map.update_traces(
    hovertemplate="<br>".join([
        "State: %{customdata[0]}",
        "Population: %{customdata[1]}",
        "Non Violent Crime: %{customdata[5]}",
        "Violent Crime : %{customdata[4]}",
        "Crime per 100k: %{customdata[3]}"
    ])
)

st.plotly_chart(map)
