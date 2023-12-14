import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw
from color_picker import main

# title of the page
st.title('Image Color Picker')

# title for the sidebar
st.sidebar.title('Menu')

# Number of top colors 
num_of_colors = st.sidebar.number_input(label='Number of Colors',
                        min_value=1,
                        max_value=10,
                        value=3,
                        step=1)

# upload the image
image = st.file_uploader('Upload an Image')

# show the uploaded image
if image:
    st.image(image=image)

# apply button
btn = st.sidebar.button(label='Apply')

st.subheader('Output Palette:')

if btn:    
    # get the color palette
    color_palette = main(image=image,n_clusters=num_of_colors)

    # show the palette
    st.image(color_palette)
