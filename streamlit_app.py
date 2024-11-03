# -*- coding: utf-8 -*-
"""

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1927PN-bgPpqncjb5OVxdo01cTnjxQGeY

# --- Introduction ---
#### Welcome! In this notebook, you will practice creating interactive visualizations using Plotly Express.
##### Follow the instructions, run the code cells, and explore the outputs!
"""
# Plotly Workshop - Student Practice Notebook

# Import necessary libraries
import streamlit as st
import seaborn as sns 
import plotly.express as px
import pandas as pd

# --- Title and Introduction ---
st.title("Plotly and Streamlit Interactive Visualizations")
st.markdown(
    """
    Welcome! This app demonstrates how to use Plotly Express and Streamlit
    to create interactive visualizations with a clean layout.
    """
)


# Author information
st.markdown("<h5 style='color: teal;'>Created by:</h6>", unsafe_allow_html=True)
st.markdown("<h5 style='color: white;'>Ashwini M, Paras N, Evlin P and Ritesh N</h6>", unsafe_allow_html=True)

"""#### Load the very simple dataset from seaborn library"""


# Load the tips dataset from Seaborn
tips = sns.load_dataset('tips')  # Loading the dataset

# Display the first few rows of the dataset
print(tips.head())  # This will show the first 5 rows of the tips dataset


# --- Task 1: Bar Chart ---
st.subheader("Task 1: Bar Chart")
#Visualizations using Plotly
fig1 = px.bar(tips, x="day", y="tip")
fig1.show()
st.plotly_chart(fig1)

# --- Task 2: Bar Chart ---
st.subheader("Task 2: Bar Chart")
#Bar Chart: Average Tip by Day (With Color)
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white',  # Clean white background
)
fig2.show()
st.plotly_chart(fig2)

# --- Task 3: violin Chart ---
st.subheader("Task 3: violin Chart")
# Violin Plot: Total Bill Distribution by Day and Time
fig3 = px.violin(tips, x='sex', y='tip', color='time', title='Violin Plot: Total Bill by Day and Time', box=True, points="all")
fig3.show()
st.plotly_chart(fig3)

# --- Task 4: Scatter Chart ---
st.subheader("Task 4: Scatter Chart")
#Scatter Plot: Total Bill vs. Tip (Color-coded by Gender)
fig4 = px.scatter(
    tips, x='total_bill', y='tip', color='sex',
    title='Total Bill vs Tip (Colored by Gender)',
    labels={'total_bill': 'Total Bill ($)', 'tip': 'Tip ($)'},
    template='plotly_dark',  # Using a cool dark theme
    size='size'  # The size of points based on the size of the group
)
fig4.show()
st.plotly_chart(fig4)

# --- Task 5: Box Chart ---
st.subheader("Task 5: Box Chart")
#Box Plot: Distribution of Total Bill by Day (With Color by Time)
fig5 = px.box(
    tips, x='day', y='total_bill', color='time',
    title='Total Bill Distribution by Day and Time',
    labels={'total_bill': 'Total Bill ($)', 'day': 'Day'},
    template='ggplot2',  # Classic theme for a beautiful look
)
fig5.show()
st.plotly_chart(fig5)

# --- Task 6: Histogram Chart ---
st.subheader("Task 5: Histogram Chart")
#Histogram: Tip Distribution (With Color)
fig6 = px.histogram(
    tips, x='tip', color='sex',
    title='Distribution of Tips (Colored by Gender)',
    labels={'tip': 'Tip ($)', 'sex': 'Gender'},
    template='plotly_white',  # Clean and bright look
)
fig6.show()
st.plotly_chart(fig6)
