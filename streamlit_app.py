import streamlit as st
import pandas as pd
import numpy as np

st.title("My Streamlit App")

with st.sidebar:
    st.header("About app")
    st.write("This is my first app!")

st.header("Bryce's First go at Streamlit")

st.subheader("DataFrame example 1")
st.markdown("This is an example data frame")
df = pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [10,20,30,40,50]
})
df

st.subheader("Slider example")
## setting up columns for slider and text
col1, col2 = st.columns(2)

with col1:
    x = st.slider("Choose an x value", 1,10)
with col2:
    st.write("The value of :red[***x***] is", x)

st.subheader("Chart Example")
## numpy and pandas usage for area chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)


