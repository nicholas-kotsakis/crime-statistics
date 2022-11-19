import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Crime Dashboard",
    page_icon="👋",
) 

st.title("Crime Dashboard")

df = pd.read_csv("data/crimedata.csv")
st.bar_chart(data=df,x='state',y='assaults')
