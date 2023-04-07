import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Line Plot Example with CSV Upload')

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

    # get user input for x-axis and y-axis labels
    # create input fields for x-axis and y-axis labels

    # Create the box plot
    fig, ax = plt.subplots()
    sns.lineplot(data = df, linestyle = 'dotted')
    ax.set_title('Box Plot')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Values')
    # create a "Update Plot" button



    # Display the plot
    st.pyplot(fig)
    st.write('Upload a csv file.')
    # create a "Update Plot" button
    

    
#else:
    #st.write('No file was uploaded.')