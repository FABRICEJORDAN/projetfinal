import streamlit as st
import json
import requests
import pandas as pd
import plotly.express as px
from mod_data import pollution

st.set_page_config(
    page_title="SCEBEC",
    page_icon="🏭",
)

po=pollution()

st.markdown(f'<h1 style="color:black;font-size:24px; text-align: center;text-decoration: underline">{"Consommation annauel des batiments en fonction du type denergie"}</h1>', unsafe_allow_html=True)

fig = px.line(po,
              x="SteamUse(kBtu)", y="PropertyName", 
              markers=True,
             )
st.plotly_chart(fig)