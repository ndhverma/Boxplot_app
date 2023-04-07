import streamlit as st
import pandas as pd
import numpy as np

st.title('Box Plot Example with CSV Upload')

# Create file uploader
uploaded_file = st.file_uploader('Upload a CSV file', type='csv')

# If a file was uploaded
if uploaded_file is not None:
    # Read the data into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Load data
    #df = pd.read_csv('data.csv')

    # Display the DataFrame
    st.write('Original Data')
    st.write(df)