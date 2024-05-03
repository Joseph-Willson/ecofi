import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Data visualisation F1",
)

st.sidebar.title("Mais qui gagnera !")

with st.sidebar:
    add_radio = st.radio(
        "Chapitres",
        ("Chapitre 1 : Histoire de la F1", "Chapitre 2 : 2020 une année importante", "Chapitre 3 : 2021 !")
    )

