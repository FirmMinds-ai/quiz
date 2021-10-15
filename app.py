import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


count = 0
st.header("Question 5")

img= Image.open("5 (2).jpg")
st.image(img)
st.text(" \n")
st.text(" \n")




st.write('What did you saw first?')


option_51 = st.checkbox('A Lips')

if option_51 :
    st.write("you always take things the way they are and judge them by their true value. You don’t try to change or decipher things around you or understand their hidden meaning.")
    count += 1
option_52 = st.checkbox('B Trees')
if option_52 :
    st.write("you are an ambitious person who always looks further than others. Moreover, you are a perfectionist to the core and search for the best things in any situation.")
    count += 1
option_53 = st.checkbox("C Roots")
if  option_53:
     st.write("you are an extremely progressive person always trying to improve or change a situation. ")
     count += 1




st.header("Question 6")


img1= Image.open("6.jpg")
st.image(img1)
st.text(" \n")
st.text(" \n")




st.write('What did you saw first?')

option_61 = st.checkbox("A Crocodile")

if option_61 :
    st.write(" you can be a little careless and inattentive to details by nature. Moreover, you are a practical person who doesn’t like to take risks")
    count += 1
option_62 = st.checkbox('B Boat')

if option_62 :
    st.write("you like nuances and slightly visible details. You prefer to stand out of the crowd as well as be a creative and unique person. Anyway, try to picture the world as a holistic thing, and don’t waste your time on the meaningless details")
    count += 1

st.text(" \n")
st.text(" \n")


st.header("Total Answers given")
st.write(str(count))
