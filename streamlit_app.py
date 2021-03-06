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
    
points = st.slider('Samples', 1, 10000, help='''
    This is a test. See streamlit issue #4000 for more info.
    We expect all text in this tooltip to be the same size.
    1. This is a test -normal
    2. *This is a test* -italic
    3. **This is a test** -bold
    4. ~This is a test~ -strikethrough
    - This is a test -normal
    - *This is a test* -italic
    - **This is a test** -bold
    - ~This is a test~ -strikethrough
    This is a code block
    
        print("Hello, world!")
        for i in range(10):
            print(i)
    ''')

draw = st.button('Sample and Plot')
if draw:
    st.session_state.points = points
    df = pd.DataFrame(np.random.normal(1, 100, size=(st.session_state.points, 2)), columns = ['x', 'y'])

    c = alt.Chart(df).mark_circle().encode(
         x='x', y='y', tooltip=['x', 'y'])

    st.altair_chart(c, use_container_width=True)


st.title('Sample Geospatial Visualization - Airports in the US')

data_url ='https://raw.githubusercontent.com/altair-viz/vega_datasets/master/vega_datasets/_data/airports.csv'

df = pd.read_csv(data_url)

airports= alt.Chart(df).mark_circle(size=10).encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    color='state:N',
    tooltip=['iata:N', 'name:N', 'city:N', 'state:N']
).project(
    type='albersUsa'
).properties(
    width=1000,
    height=600
)

st.altair_chart(airports)
                 
