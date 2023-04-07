import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Box Plot Example with CSV Upload')

# Create file uploader
uploaded_file = st.file_uploader('Upload a CSV file', type='csv')

# If a file was uploaded
if uploaded_file is not None:
    # Read the data into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.write('Original Data')
    st.write(df)


    # get user input for x-axis and y-axis labels
    x_label = st.text_input('Enter x-axis label', 'Columns')
    y_label = st.text_input('Enter y-axis label', 'Values')


    # Create the box plot
    fig, ax = plt.subplots()
    sns.boxplot(data=df, ax=ax)
    ax.set_title('Box Plot')
    ax.set_xlabel('x_label')
    ax.set_ylabel('y_label')
    


    

    # Display the plot
    st.pyplot(fig)
    st.write('Upload a csv file.')
#else:
    #st.write('No file was uploaded.')
