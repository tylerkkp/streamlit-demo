import streamlit as st

counter = 0
st.text(counter)
st.button('Click Me!', on_click=count())

def count():
  counter += 1
