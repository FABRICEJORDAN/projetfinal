import streamlit as st
import json
import requests
import pandas as pd

st.set_page_config(
    page_title="SCEBEC",
    page_icon="🏭",
)

pollution = pd.read_csv('pollution.csv',sep=",", on_bad_lines='skip')