import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import plotly.express as px

count = 0
a = []

st.header("Question 1")

img= Image.open("q1.jpg")
st.image(img)
st.text(" \n")
st.text(" \n")




st.write('What did you saw first?')


option_11 = st.checkbox('zebra')

if option_11 :
    st.write("Then you are an extrovert; someone who loves meeting and talking to new people, partying and doing new things. You don’t like following the same routine as it isn’t your style.")
    count += 1
    a.append(1)
option_12 = st.checkbox('lion')
if option_12 :
    st.write("Then you’re unmistakably an introvert who likes spending quality time alone or with the company of a loved one. You’d rather be at home enjoying a few episodes of your favorite TV show with a glass of your favorite drink rather than go out and party.")
    count += 1
    a.append(1)



st.header("Question 2")

img= Image.open("q2.jpg")
st.image(img)
st.text(" \n")
st.text(" \n")




st.write('What did you saw first?')


option_21 = st.checkbox('baby')

if option_21 :
    st.write("You prefer your own company more so than others and don’t exactly feel like going out too often. You shouldn’t feel guilty for who you are, and just enjoy being yourself.")
    count += 1
    a.append(2)
option_22 = st.checkbox('couple')
if option_22 :
    st.write("You care a great deal for your friends and would even do absolutely anything for them. At the same time, you don not exactly enjoy hanging out in big groups or going to noisy parties.")
    count += 1
    a.append(2)


option_23 = st.checkbox('trees')
if option_23 :
    st.write("You are always ready to experience something new and have a bubbly personality. Change is what you love and you just happen to crave it.")
    count += 1
    a.append(2)



st.header("Question 3")

img= Image.open("q3.jpg")
st.image(img)
st.text(" \n")
st.text(" \n")




st.write('What did you saw first?')


option_31 = st.checkbox('Trees')

if option_31 :
    st.write("Your intuition is always right which is why you tend to completely follow it. You have a very laid-back personality and like to spend time in silence doing nothing at all.")
    count += 1
    a.append(3)
option_32 = st.checkbox('Tiger')
if option_32 :
    st.write("Your mind is strong and whenever you make a decision, you will never ever doubt if it’s right or wrong. The saying: “don’t trouble the trouble if the trouble does not trouble you”, is perfect for you.")
    count += 1
    a.append(3)


st.header("Question 4")

img= Image.open("q4.jpg")
st.image(img)
st.text(" \n")
st.text(" \n")




st.write('What did you saw first?')


option_41 = st.checkbox('pillars')

if option_41 :
    st.write("It could point to the possibility that you prefer comfort and security over most things. Accomplishing your big goals in life will not be possible unless you learn to break out of your comfort zone. It’s also a sign that you focus on dreaming about your goals too much and not enough time actually working on them.")
    count += 1
    a.append(4)
option_42 = st.checkbox('people')
if option_42 :
    st.write("It means that you are a free spirit whose ready to leave your current surroundings at the drop of a hat. Life hardly ever seems dull to you. In fact it’s full of incredible people and adventures! You are a curious and kind soul, but don’t wander for too long. Be ready when the right time comes to settle down.")
    count += 1
    a.append(4)


st.header("Question 5")

img= Image.open("q5.jpg")
st.image(img)
st.text(" \n")
st.text(" \n")




st.write('What did you saw first?')


option_51 = st.checkbox('A Lips')

if option_51 :
    st.write("you always take things the way they are and judge them by their true value. You don’t try to change or decipher things around you or understand their hidden meaning.")
    count += 1
    a.append(5)
option_52 = st.checkbox('B Trees')
if option_52 :
    st.write("you are an ambitious person who always looks further than others. Moreover, you are a perfectionist to the core and search for the best things in any situation.")
    count += 1
    a.append(5)
option_53 = st.checkbox("C Roots")
if  option_53:
     st.write("you are an extremely progressive person always trying to improve or change a situation. ")
     count += 1
     a.append(5)




st.header("Question 6")


img1= Image.open("Q6.jpg")
st.image(img1)
st.text(" \n")
st.text(" \n")




st.write('What did you saw first?')

option_61 = st.checkbox("A Crocodile")

if option_61 :
    st.write(" That means you’re most likely someone who tends to look at the bigger picture of things. You may take the little things for granted, like walking through nature, as you don’t see the overall importance, when there are bigger things you can focus on.You are probably a very practical person and don’t take much risks.You live more on the cautious side of things and don’t make much room for new experiences or things.")
    count += 1
    a.append(6)
option_62 = st.checkbox('B Boat')

if option_62 :
    st.write("It means you’ve got a good eye for small details, and not much gets past you without noticing it. You are often described as a unique, quirky and creative individual. But don’t get too caught up on focusing on the little details and forget about the big picture. This is especially important if you are an artist or a student.You can get wrapped up in one small part of a project and forget to complete the entire assignment as a whole.")
    count += 1
    a.append(6)

st.text(" \n")
st.text(" \n")


st.header("Question 7")


img1= Image.open("q7.jpg")
st.image(img1)
st.text(" \n")
st.text(" \n")




st.write('What did you saw first?')

option_71 = st.checkbox("A car")

if option_71 :
    st.write("It most likely means that freedom is very important to you. Traveling is dear to your heart. The ability to hit the road and go on an adventure is something you highly prioritize. You take life at your own pace, and do what comes naturally.")
    count += 1
    a.append(7)
option_72 = st.checkbox('B binoculars')

if option_72 :
    st.write("It alludes to the idea that you’re a more analytical person. You tend to focus on the big picture and disregard minor details. You are a visual learner and pick up lessons quickly. But you may want to make an effort to pay a bit more attention to the details, as important things can be lost there.")
    count += 1
    a.append(7)


st.header("Question 8")

img1= Image.open("q8.jpg")
st.image(img1)
st.text(" \n")
st.text(" \n")




st.write('What did you saw first?')

option_81 = st.checkbox("A duck")

if option_81 :
    st.write("It’s possible that your life consists of emotional impulses. You often have rapid mood swings, and you tend to make decisions abruptly.")
    count += 1
    a.append(8)
option_82 = st.checkbox('B rabbit')

if option_82 :
    st.write("You like considering all the consequences of each action. Logic usually takes first place in your life, although this doesn’t necessarily mean that you are a cold and insensitive person.")
    count += 1
    a.append(8)


st.text(" \n")
st.text(" \n")

st.header("Total Questions Answered")
st.write(str(len(set(a))))

if len(set(a))>0:
    st.write(str(set(a)))

st.header("Total Answers given by the user")
st.write(str(count))

import pandas as pd



t = {1,2,3,4,5,6,7,8}
A=  set(a)
n =  t-A
a1 = "TOTAL QUESTIONS ANSWERED : "+ str(list(A))
a2 = "TOTAL QUESTIONS ARE NOT ANSWERED : "+str(list(n))
df =pd.DataFrame([[a1,len(list(A))],[a2,len(list(n))]],columns = ["TYPE","VALUE"])
print(df)
import random
list1 = [0,1, 2, 3, 4, 5, 6,7,8]


ans = ["You have a good personality",
"You  are a good human",
"Your brain is fast",
"Your are very emotional",
"You are little sensitive",
"You seem to be intelligent",
"You are a loving human",
"You are  strong human being",
"You have good nature"]

fig = px.pie(df, values='VALUE', names='TYPE')
st.plotly_chart(fig,use_container_width=15)
S = "QUIZ MARKS: " + str((len(A)/8)*100)
st.header(ans[random.choice(list1)])
