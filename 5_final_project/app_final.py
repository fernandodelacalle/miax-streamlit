import streamlit as st


st.header("mIAx API EXPLORER")


market = st.selectbox(
    "Selecciona un mercado:",
    ["IBEX", "DAX", "EUROSTOXX"]
)

ticker = st.selectbox(
    "Selecciona un ticker:",
    ["SAN", "TEF"]
)

st.write("se ha seleccionado: ", market, ticker)


