#import pandas
import streamlit as st
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
from alertanalyzer import alert_analyzer
from causalanalyzer import causal_analysis
from onlinealertanalyzer import online_alert_analyzer






def main():

    # Setting up sidebar 
    st.sidebar.header('Analytics Menu')

    # Create List
    page = st.sidebar.selectbox("Pick your Analytics", ["Canned Alert Analyzer", "Causality Analysis", "Online Alert Analyzer"]) 
    if page == "Canned Alert Analyzer":
        alert_analyzer()
    elif page == "Causality Analysis":
        causal_analysis()
    elif page == "Online Alert Analyzer":
        online_alert_analyzer()

    


if __name__ == "__main__":
    main()