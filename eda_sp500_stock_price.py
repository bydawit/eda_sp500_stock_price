import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf

st.title('S&P 500 App')

st.markdown("""
This app retrieves the list of the **S&P 500** (from Wikipedia) and its corresponding **stock closing price** (year-to-date)!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header('User Input Features')

# Web scraping of S&P 500 data
#


@st.cache
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    df = html[0]
    return df


df = load_data()
sector = df.groupby('GICS Sector')
# df
# Sidebar - Sector selection
sorted_sector_unique = sorted(df['GICS Sector'].unique())
# sorted_sector_unique
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)
# selected_sector

# Filtering data
df_selected_sector = df[(df['GICS Sector'].isin(selected_sector))]
df_selected_sector

st.header('Displaye Companies in Selected Sector')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + " rows and " + str(df_selected_sector.shape[1]) + ' columns.')
