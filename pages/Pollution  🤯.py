import streamlit as st
import json
import requests
import pandas as pd
import plotly.express as px
from mod_data import pollution
from plotly import graph_objs as go

st.set_page_config(
    page_title="SCEBEC",
    page_icon="🏭",
)

po=pollution()

st.markdown(f'<h1 style="color:black;font-size:24px; text-align: center;text-decoration: underline">{"Les batiments les plus polluants"}</h1>', unsafe_allow_html=True)
val = [False,True]
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.write('Je souhaite voir les')
with col2:
    m = st.number_input("", value=6, step=1, format="%d")
with col3:
    st.write("Habitations les plus polluantes")
with col4:
    selected_option2 = st.selectbox('trier par ordre croissant', val)


first=po.sort_values(by='TotalGHGEmissions', ascending=selected_option2)[:m]
data2 = [
    go.Scatter(x = first['PropertyName'], y=first['TotalGHGEmissions'], name='Quantité électricité utilisé', text=first['TotalGHGEmissions'])
]
fig2 = go.Figure(data=data2)

st.plotly_chart(fig2)

st.write(first.loc[:,['PropertyName','TotalGHGEmissions','YearBuilt']])