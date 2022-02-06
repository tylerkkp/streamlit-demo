import streamlit as st

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

amount = st.radio('Amount', [1, 5, 10, 20, 50, 100])
    
increment = st.button('Increment')
if increment:
    st.session_state.count += amount

st.write('Count = ', st.session_state.count)
