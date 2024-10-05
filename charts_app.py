import plotly.express as px
import streamlit as st

st.title('Streamlit for charts')

df1 = px.data.gapminder().query("year == 2007")
fig1 = px.treemap(df1, path=[px.Constant('World'), 'continent','country'], values = 'pop' , color = 'lifeExp')
st.plotly_chart(fig1)
