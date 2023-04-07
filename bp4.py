import streamlit as st
import seaborn as sns

# create a list of sample data for the boxplot
data = [1, 2, 3, 4, 5]

# create input fields for x-axis and y-axis labels
x_label = st.text_input("Enter x-axis label:")
y_label = st.text_input("Enter y-axis label:")

# create a boxplot using Seaborn and specify axis labels
fig = sns.boxplot(x=data, y=data, xlabel=x_label, ylabel=y_label)

# display the boxplot in Streamlit
st.pyplot(fig)
