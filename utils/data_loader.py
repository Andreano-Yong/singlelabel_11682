import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Load and cache the dataset
    """
    df = pd.read_csv(r'C:\singlelabel_11682\data\train_preprocess.csv')
    return df
