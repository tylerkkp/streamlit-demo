import streamlit as st

count = 0
counter = st.write(count)

def hello():
  count += 1
  
st.button('Click Me!', on_click=hello())
