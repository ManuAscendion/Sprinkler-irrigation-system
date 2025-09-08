import numpy as np 
import pickle
import pandas as pd
import streamlit as st 
import sklearn

pickled_model = pickle.load(open('sprink.pkl', 'rb'))

def main():
    st.title("Sprinkler Irrgiation System App") 

    html_temp = """
    <div style="background-color:teal; padding:10px;">
    <h2 style="color:white; text-align:center;">Sprinkler Irrigation System</h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)

    temperature=st.number_input("Enter the temperature in celcius")
    humidity=st.number_input("Enter the humidity in %")

    inputs=[[temperature,humidity]]

    result = 0

    if st.button('Predict'):
        result=pickled_model.predict(inputs)[0]
        st.success('Predicted Sprinkler Duration is  : {}'.format(result))

if __name__ == '__main__':
    main()