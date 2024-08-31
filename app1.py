# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import numpy as np
import pickle
import pandas as pd
import streamlit as st
import os

import os
print(os.getcwd())

def welcome():
    return 'Welcome All'

file_path = os.path.join(r'C:\Users\prave\.spyder-py3',  'to', r'C:\Users\prave\Deployment', 'Classifierout.pkl')

pickle_in = open("saving.sav", "rb")
classifier = pickle.load(pickle_in)

def predict1(variance,skewness,curtosis,entropy):
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction
    
def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style = 'background-color = tomato; padding = 10px'>
    <h2 style = 'color: white;text-align: center;'>Streamlit Bank Auithenticator ML App
    """
    st.markdown(html_temp, unsafe_allow_html= True)
    variance = st.text_input('Variance')
    skewness = st.text_input('Skewness')
    curtosis = st.text_input('Curtosis')
    entropy = st.text_input('Entropy')
    result = ""
    if st.button('Predict'):
        result = predict1(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    
main()