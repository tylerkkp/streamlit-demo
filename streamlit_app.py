import streamlit as st

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

amount = st.slider('Amount', 1, 50)
    
increment = st.button('Increment')
if increment:
    st.session_state.count += amount

clear = st.button('Clear')
if clear:
    st.session_state.count = 0

st.write('Count = ', st.session_state.count)

import pandas as pd
import numpy as np
import altair as alt

st.title('Plot Normal Distribution (X and Y axis)')
if 'points' not in st.session_state:
    st.session_state.points = 0
    
points = st.slider('Samples', 1, 10000)

draw = st.button('Sample and Plot')
if draw:
    st.session_state.points = points
    df = pd.DataFrame(np.random.normal(1, 100, size=(st.session_state.points, 2)), columns = ['x', 'y'])

    c = alt.Chart(df, width=400.0, height=400.0).mark_circle().encode(
         x='x', y='y', tooltip=['x', 'y'])

    st.altair_chart(c, use_container_width=True)
                 
