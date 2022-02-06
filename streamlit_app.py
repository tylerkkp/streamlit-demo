import streamlit as st

def hello():
  st.text('Hello World!')
  
st.button('Click Me!', on_click=hello())
