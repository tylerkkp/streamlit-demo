import streamlit as st

global counter
counter = 0
def count():
  counter += 1
  
st.text(counter)
st.button('Click Me!', on_click=count())
