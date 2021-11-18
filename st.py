
import pandas as pd 
import numpy as np
import datetime as dt
import streamlit as st


opp = pd.read_json("http://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json")
opp['valor'] = opp['valor'].replace(r'^\s*$', np.nan, regex=True).astype(float)
opp['data'] = pd.to_datetime(opp['data'], format = '%d/%m/%Y')
opp.columns = ['data','ipca']

x = st.slider('x')  # 👈 this is a widget

st.write(x, 'Mova o cursor para alterar o índice', opp.iloc[0:x,:])


for i in range(3):
    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
           np.random.randn(20, 3),
           columns=['a', 'b', 'c'])

        chart_data




