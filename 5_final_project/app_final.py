import streamlit as st
from api_handler import BMEApiHandler
import plotly.graph_objects as go

st.header("mIAx API EXPLORER")

api_key = st.sidebar.text_input("Intrduce el api key")
if not api_key:
    st.error("no api key")
    st.stop()

market = st.selectbox(
    "Selecciona un mercado:",
    ["IBEX", "DAX", "EUROSTOXX"]
)

# llamada al tck master
ah = BMEApiHandler(user_key=api_key)

maestro = ah.get_ticker_master(market=market)
tcks = maestro.ticker.to_list()

ticker = st.selectbox(
    "Selecciona un ticker:",
    tcks
)
st.write("se ha seleccionado: ", market, ticker)

# sacar la grafica
df = ah.get_close_data(tck=ticker, market=market)

st.line_chart(df)


data_to_plot = ah.get_ohlc_data(market=market, tck=ticker)
fig = go.Figure(
    go.Candlestick(
        x=data_to_plot.index,
        open=data_to_plot['open'],
        high=data_to_plot['high'],
        low=data_to_plot['low'],
        close=data_to_plot['close']
    )
)
st.plotly_chart(fig)
