import plotly.express as px
import streamlit as st

df = px.data.gapminder().query("year == 2007")
fig = px.treemap(df, path=[px.Constant('World'), 'continent','country'], values = 'pop' , color = 'lifeExp')
fig.show()
