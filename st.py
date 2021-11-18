
import pandas as pd 
import numpy as np
import datetime as dt
import streamlit as st
import seaborn
sns.set_theme(style="darkgrid")

opp = pd.read_json("http://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json")
opp['valor'] = opp['valor'].replace(r'^\s*$', np.nan, regex=True).astype(float)
opp['data'] = pd.to_datetime(opp['data'], format = '%d/%m/%Y')
opp.columns = ['data','ipca']

x = st.slider('x')  # 👈 this is a widget

st.write(x, 'Mova o cursor para alterar o índice', seaborn.lineplot(x="data", y="ipca",
             data=opp.iloc[0:x,:]))


#sns.lineplot(x="data", y="ipca",
 #            data=opp.iloc[0:x,:])
