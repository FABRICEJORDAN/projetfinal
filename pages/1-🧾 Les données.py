import streamlit as st
import json
import requests
import pandas as pd
from mod_data import pollution

st.set_page_config(
    page_title="SCEBEC",
    page_icon="🏭",
)

po=pollution()

st.markdown(f'<h1 style="color:black;font-size:30px; text-align: center;text-decoration: underline">{"Les données utilisés pour le dashboard"}</h1>', unsafe_allow_html=True)

st.write(po)
st.write("le TotalGHGEmissions est mesuré en tonnes métriques et c'est l'équivalent du dioxyde de carbone (CO2).")
