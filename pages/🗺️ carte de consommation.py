# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 14:08:54 2023

@author: Sam
"""

import pandas as pd
import streamlit as st
import folium
from mod_data import pollution
from streamlit_folium import folium_static

st.set_page_config(
    page_title="SCEBEC",
    page_icon="🏭",
)

po=pollution()


# st.title("Carte de la consommation en électricité par emplacement")

# # Création de la carte Folium
# folium_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=12)  # Ajustez le zoom et la position initiale selon vos besoins

# # Ajout des marqueurs pour chaque emplacement avec la consommation en électricité comme popup
# for index, row in df.iterrows():
#     folium.Marker(
#         location=[row['Latitude'], row['Longitude']],
#         popup=f"Latitude: {row['Latitude']}, Longitude: {row['Longitude']}<br>Consommation en électricité : {row['Electricity(kWh)']} kWh",
#     ).add_to(folium_map)

# # Convertir la carte Folium en HTML
# folium_map.save("map.html")
# with open("map.html", "r") as f:
#     map_html = f.read()

# # Afficher la carte dans Streamlit avec st.components.v1.html
# st.write("Carte de la consommation en électricité par emplacement :")
# html(map_html, width=800, height=600, scrolling=True)
def color_marker(electricity):
    if electricity < po['Electricity(kBtu)'].mean():
        return 'blue'
    else:
        return 'red'

#Titre de l'application
st.markdown(f'<h1 style="color:black;font-size:24px; text-align: center;text-decoration: underline">{"Carte de la consommation en électricité par adresse"}</h1>', unsafe_allow_html=True)

# Sélection de la colonne contenant l'adresse et la consommation en électricité
selected_columns = ['Address', 'Electricity(kBtu)']

# Création de la carte Folium
m = folium.Map(location=[po['Latitude'].mean(), po['Longitude'].mean()], zoom_start=12)

# Ajout des marqueurs pour chaque emplacement avec la consommation en électricité comme popup
for index, row in po[selected_columns].iterrows():
    popup_text = f"Adresse: {row['Address']}<br>Consommation en électricité : {row['Electricity(kBtu)']} kBtu"
    folium.Marker(
        location=[po.at[index, 'Latitude'], po.at[index, 'Longitude']],
        popup=folium.Popup(popup_text, max_width=300),
        icon=folium.Icon(color=color_marker(row['Electricity(kBtu)']))
    ).add_to(m)

# Ajouter une légende au-dessus de la carte
st.markdown("**Légende :**")
st.markdown("- bleu : consommation en dessous de la moyenne")
st.markdown("- Rouge : consommation au dessus de la moyenne")

folium_static(m)

st.write(f"Type de lieu où on consomme le plus {po[po['Electricity(kBtu)']==po['Electricity(kBtu)'].max()]['PrimaryPropertyType']}")
st.write(f"lieu où on consomme le plus {po[po['Electricity(kBtu)']==po['Electricity(kBtu)'].max()]['Address']}")
