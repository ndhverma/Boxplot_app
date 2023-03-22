import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


# Create a function to generate the box plot
def generate_boxplot(data, x_column, y_column):
    fig, ax = plt.subplots()
    ax.boxplot(data[y_column], labels=data[x_column])
    ax.set_title('Box Plot')
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    st.pyplot(fig)

# Load data
data = pd.read_csv('data.csv')

# Create sidebar inputs
x_column = st.sidebar.selectbox('Select X column', options=data.columns)
y_column = st.sidebar.selectbox('Select Y column', options=data.columns)

# Display box plot
generate_boxplot(data, x_column, y_column)
