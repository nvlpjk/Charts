import plotly.express as px
import streamlit as st

st.title('Streamlit for sin and cos fuctioni visualiztion')


x_start = st.slider('x 시작값' ,  0.0, 10.0, 0.0)
x_end = st.slider('x 시작값' ,  10.0, 20.0, 10.0)

df1 = px.data.gapminder().query("year == 2007")
fig1 = px.treemap(df1, path=[px.Constant('World'), 'continent','country'], values = 'pop' , color = 'lifeExp')
st.plotly_chart(fig1)

