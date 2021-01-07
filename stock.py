import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""

# this is a simple stock price prediction app using the streamlit library

below are the stock closing and volume of Goolge


""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id',start='2005-5-31',end='2020-5-31')

st.write("""
## Closing chart
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume chart
""")
st.line_chart(tickerDf.Volume)
