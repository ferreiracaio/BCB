
import pandas as pd 
import numpy as np
import datetime as dt
import streamlit as st

opp = pd.read_json("http://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json")
opp['valor'] = opp['valor'].replace(r'^\s*$', np.nan, regex=True).astype(float)
opp['data'] = pd.to_datetime(opp['data'], format = '%d/%m/%Y')
opp.columns = ['data','ipca']
opp = opp.set_index('data')

x = st.slider('x')

st.write(x, 'Mova o cursor para alterar o índice', opp.iloc[0:x,:])
st.line_chart(opp.iloc[0:x,:])




# with st.echo(code_location='below'):
#     import plotly.express as px

#     fig = px.scatter(
#         x=opp["data"].iloc[0:x,:],
#         y=opp["ipca"].iloc[0:x,:],
#     )
#     fig.update_layout(
#         xaxis_title="data",
#         yaxis_title="ipca",
#     )

#     st.write(fig)





# with st.echo(code_location='below'):
#     import matplotlib.pyplot as plt

#     fig = plt.figure()
#     ax = fig.add_subplot(1,1,1)

#     ax.scatter(
#         opp["data"].iloc[0:x,:],
#         opp["ipca"].iloc[0:x,:],
#     )

#     ax.set_xlabel("data")
#     ax.set_ylabel("ipca")

#     st.write(fig)

