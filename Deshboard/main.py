import pandas as pd
import numpy as np
import os
import glob
import streamlit as st
from datetime import date
import warnings
# hide future warnings (caused by st_aggrid)
warnings.simplefilter(action='ignore', category=FutureWarning)

#set page layout and define basic variables
st.set_page_config(layout="wide", page_icon='⚡', page_title="Website Traffic Forecasting")
path = os.path.dirname(__file__)
today = date.today()

# Create a sidebar navigation bar
st.sidebar.header("Navigation")
# Add links or options to the navigation bar
selected_page = st.sidebar.radio("Select a Page", ["All Countries", "Setting"])

if selected_page=='All Countries':
    
    meta_information_country = {}
    for path in glob.glob('../plots/*.html'):
        country = path.split('/')[-1].split('.')[0]
        meta_information_country[country] =path
    

    st.title("Interactive Plot for each Country")

    selected_sku_id = st.selectbox("Select Country:", list(meta_information_country.keys()))
    st.write(f"Selected country: {selected_sku_id}")
    
    if selected_sku_id:
        
        plot_url = meta_information_country[selected_sku_id]
        st.write(f"Selected country: {plot_url}")

        with open(plot_url, 'r') as file:
            html_plot = file.read()
            st.components.v1.html(html_plot,height=800,width=1800,scrolling=False)
    
