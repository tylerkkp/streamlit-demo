import streamlit as st

def count():
  counter += 1

counter = 0
st.text(counter)
st.button('Click Me!', on_click=count())
