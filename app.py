import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title="Rank Prediction of Smartphone")
st.header("Rank Prediction of Smartphone")
st.subheader("Feed me with your CSV file")
uploaded_file = st.file_uploader('Choose CSV file', type='csv')
if uploaded_file:
    st.markdown('-----')
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)