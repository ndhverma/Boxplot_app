import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

# Create a function to generate the box plot
def generate_boxplot(data, columns):
    fig, ax = plt.subplots()
    data[columns].boxplot(ax=ax)
    ax.set_title('Box Plot')
    ax.set_xlabel(', '.join(columns))
    st.pyplot(fig)

# Load data
data = pd.read_csv('data.csv')

# Create sidebar inputs
columns = st.sidebar.multiselect('Select columns', options=data.columns)

# Display box plot
if columns:
    generate_boxplot(data, columns)
else:
    st.warning('Please select at least one column.')
