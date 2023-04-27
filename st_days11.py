import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What is your favorite color?',
     (['Green','Yellow', 'Red', 'Blue'],['Yellow','Red'])

st.write('You selected: ', options)
