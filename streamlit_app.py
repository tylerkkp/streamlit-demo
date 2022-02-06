import streamlit as st

def hello():
  st.write('Hello World!')
  
st.button('Click Me!', on_click=hello())
