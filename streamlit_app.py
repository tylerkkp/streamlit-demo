import streamlit as st

# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

def word_cloud(text):
  # Create and generate a word cloud image:
  wordcloud = WordCloud(width = 800, height = 800,
          background_color ='white',
          stopwords = stopwords,
          min_font_size = 10).generate(text)

  # Display the generated image:
  plt.figure() 
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.show()

txt = st.text_area('Text:')

if st.button('Create Word Cloud'):
  st.write(word_cloud(txt))
