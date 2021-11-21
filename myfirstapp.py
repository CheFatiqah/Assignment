import streamlit as st
import numpy as np
import pandas as pd

st.header("BMI Calculator")
st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I agree the terms and conditions')

if show:
    st.write('Thank You')

st.header('User Input Parameters')

def user_input_features():
    age = st.slider('age', 20, 80, 40)
    data = {'age': age}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

option = st.sidebar.selectbox(
    'Select gender',
     ['Male','Female'])

Weight = st.number_input ("Weight:",min_value=1.0)
Height = st.number_input ("Height:",min_value=1.0)
BMI = Weight / (Height ** 2)

if(st.button("Calculate")):
    st.text("Your BMI is " + str(round(BMI)))
    
    if (BMI < 18):
        st.warning ("Underweight")
    elif (BMI >=18 and BMI < 25):
        st.success ("Healhty")
    elif (BMI >=25):
        st.warning ("Overweight")
