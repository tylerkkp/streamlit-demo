import streamlit as st

hello = st.write('Hello World!')

def hello():
  hello = 'test'
  
st.button('Click Me!', on_click=hello())
