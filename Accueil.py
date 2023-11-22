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

st.markdown(f'<h1 style="color:blue;text-align: center; font-size: 40px;">{"_SCEBEC_"}</h1>', unsafe_allow_html=True)

st.markdown(f'<p style="color:black;text-align: center; font-size: 20px;">{"SUIVI DE LA CONSOMMATION ÉNERGÉTIQUE DES BÂTIMENTS ET DE ÉMISSION DU CO2"}</p>', unsafe_allow_html=True)

st.markdown(f'<h1 style="text-align: center; text-decoration: underline;font-size:30px; margin:15px">{"Infos clés"}</h1>', unsafe_allow_html=True)
st.write("➡️ Les données traités ont été récupéré dans la ville de SEATTLE en 2016")
st.write("➡️ Le nombre de batiments evalués:", po['OSEBuildingID'].count())
st.write("➡️ 3 types d'energie: gaz, vapeur, electricité")