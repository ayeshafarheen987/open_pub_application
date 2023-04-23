import streamlit as st
import os
import pandas as pd
import numpy as np
st.markdown("""
    <style>
        body {
            background-image: url("https://media.istockphoto.com/id/1287217096/photo/tasty-craft-beer-on-bar-table.jpg?b=1&s=170667a&w=0&k=20&c=yTtZjnnR3_P8PJmZoDVylWQeqk7bEknz2_E4RSNmcaQ=");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)
# Page Title
# Set page title color
st.markdown(
    """
    <style>
    .title {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Page title
st.markdown("<h1 class='title'> Open Pub Application </h1>",unsafe_allow_html=True)

#st.dataframe(pubs_df.head())
# absolute path to this file
st.markdown("<h3 class='title' >This app allows you to find pubs in the United Kingdom (UK) and discover their locations. </h3>",unsafe_allow_html=True)
st.markdown("<h5 class ='title'>This Application contains information about  pubs in the United Kingdom </h5>",unsafe_allow_html=True)

