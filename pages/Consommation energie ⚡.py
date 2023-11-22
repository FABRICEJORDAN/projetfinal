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

st.markdown(f'<h1 style="color:black;font-size:24px; text-align: center;text-decoration: underline">{"Consommation annuel de chaque energie(en Kbtu) par batiment"}</h1>', unsafe_allow_html=True)

# city_counts = po.groupby('BuildingType').size().reset_index(name='Counts')

# Affichage du nombre de lignes par ville
#st.write('Nombre dhabitations par type:')
#st.write(city_counts)
choix = st.radio(
        "Voir la consommation energetique 👇 ",
        ["Sur tout le dataframe", "Par type dhabitation","generalité"],
        key="visibility",
        horizontal=True,
    )
if choix == 'Par type dhabitation':
    valeurs_uniques = po['BuildingType'].unique()
    val = ['Electricity(kBtu)','NaturalGas(kBtu)','SteamUse(kBtu)']
    selected_option = st.selectbox('Selectionner un type dhabitation pour voir les les batiments les plus energivores', valeurs_uniques)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write('Je souhaite voir les')
    with col2:
        n = st.number_input("", value=6, step=1, format="%d")
    with col3:
        st.write("Habitations les plus énergivores")
    with col4:
        selected_option2 = st.selectbox('', val)
    

    filtre = po[po['BuildingType'] == selected_option]
    first=filtre.sort_values(by=selected_option2, ascending=False)[:n]

    data2 = [
        go.Scatter(x = first['PropertyName'], y=first[selected_option2], name='Quantité électricité utilisé', text=first[selected_option2])
    ]
    fig2 = go.Figure(data=data2)

    st.plotly_chart(fig2)

    st.write(first.loc[:,['PropertyName',selected_option2,'YearBuilt']])
elif choix == 'generalité':
    st.write('En général voici la quantité denergie consommé par type dhabitation')
    tp= po.groupby("BuildingType", as_index=False).agg({'Electricity(kBtu)': 'sum', 'NaturalGas(kBtu)': 'sum','SteamUse(kBtu)': 'sum'}).reset_index()

    data = [
        go.Scatter(x = tp['BuildingType'], y=tp["Electricity(kBtu)"], name='Quantité électricité utilisé', text=tp["Electricity(kBtu)"]),
        go.Scatter(x = tp['BuildingType'], y = tp["NaturalGas(kBtu)"], name='Quantité Gas utilisé', text=tp["NaturalGas(kBtu)"]),
        go.Scatter(x = tp['BuildingType'], y = tp["SteamUse(kBtu)"], name='Quantité vapeur utilisé', text=tp["SteamUse(kBtu)"])
    ]
    fig = go.Figure(data=data)
    st.plotly_chart(fig)

else:
    val = ['Electricity(kBtu)','NaturalGas(kBtu)','SteamUse(kBtu)']
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write('Je souhaite voir les')
    with col2:
        m = st.number_input("", value=6, step=1, format="%d")
    with col3:
        st.write("Habitations les plus énergivores")
    with col4:
        selected_option2 = st.selectbox('', val)

    first=po.sort_values(by=selected_option2, ascending=False)[:m]
    data2 = [
        go.Scatter(x = first['PropertyName'], y=first[selected_option2], name='Quantité électricité utilisé', text=first[selected_option2])
    ]
    fig2 = go.Figure(data=data2)

    st.plotly_chart(fig2)

    st.write(first.loc[:,['PropertyName',selected_option2,'YearBuilt']])
