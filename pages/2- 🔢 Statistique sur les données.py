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

st.markdown(f'<h1 style="color:black;font-size:30px; text-align: center;text-decoration: underline">{"Statistiques sur les données"}</h1>', unsafe_allow_html=True)

st.write(po.describe())
st.write("NB: std c'est l'ecartype, mesure de la dispersion des valeurs")
