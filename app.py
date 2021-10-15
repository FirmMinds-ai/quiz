import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.header("Question 5")

img= Image.open("5 (2).jpg")
st.image(img)
st.text(" \n")
st.text(" \n")




st.write('What did you saw first?')
# option_51,option_52,option_53 = True ,True ,True

option_51 = st.button('A Lips')

if option_51 :
    st.write("you always take things the way they are and judge them by their true value. You don’t try to change or decipher things around you or understand their hidden meaning.")

option_52 = st.button('B Trees')
if option_52 :
    st.write("you are an ambitious person who always looks further than others. Moreover, you are a perfectionist to the core and search for the best things in any situation.")
option_53 = st.button('C Roots')
if  option_53:
     st.write("you are an extremely progressive person always trying to improve or change a situation. ")
