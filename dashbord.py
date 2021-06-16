import streamlit as st
import pandas as pd


st.title('hi dashboard')

@st.cache
def get_data():
    d = pd.read_csv('temp/data.csv')
    d['date'] = pd.to_datetime(d['date'], infer_datetime_format=True)
    return d

data_to_show = get_data()

st.write(data_to_show)

st.map(data_to_show)
