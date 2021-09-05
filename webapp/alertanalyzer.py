import pandas
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




@st.cache
def read_data(data="data/alert-2.csv.gz"):
    """Read the data from local."""
    alert_total_df = pandas.read_csv(data,index_col=0,compression='gzip')
    # if the file is not gz, then command is: alert_total_df = pandas.read_csv(fname,index_col=0)
    alert_total_df["value"]=alert_total_df["value"].astype(float)
    # print(alert_total_df.head())
    return alert_total_df



def alert_analyzer():

    #plt.rcParams['figure.figsize'] = (30, 10)

    # Load data
    alert_total_df = read_data()

    # Title of Analysis
    st.markdown("## This notebook Analyzes the canned data collected about alerts")

    # Total Alert distribution
    alert_count_df = alert_total_df.groupby(["timestamp"])["value"].sum()
    print(alert_count_df.head())
    # ax=alert_count_df.plot(title="Total Number of Alerts")
    # ax.legend(bbox_to_anchor=(0., 1.06, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    # plt.show()
    st.title("Total Number of Alerts")
    #Line Chart
    st.line_chart(alert_count_df)

    # Number of Alerts by cluster
    alert_cluster_df = alert_total_df.groupby(["cluster","timestamp"])["value"].sum()
    alert_cluster_df=alert_cluster_df.unstack(level=0)
    st.title("Number of Alerts by cluster by time")
    #st.dataframe(alert_cluster_df.head())
    fig, ax = plt.subplots(figsize=(30, 10))
    #does not work
    #ax = alert_cluster_df.plot(title="Number of Alerts by cluster")
    ax.plot(alert_cluster_df)
    # st.title("Number of Alerts by Cluster by time")
    ax.set_title('Number of Alerts by Cluster by time')
    plt.xticks(rotation=90)
    plt.show()
    st.pyplot(fig)

    # Number of different Alerts
    alert_alert_df = alert_total_df.groupby(["alertname","timestamp"])["value"].sum()
    alert_alert_df=alert_alert_df.unstack(level=0)
    #print(alert_alert_df.head())
    fig, ax = plt.subplots(figsize=(30, 10))
    ax.plot(alert_alert_df)
    # ax=alert_alert_df.plot(title="Number of different Alerts")
    ax.legend(bbox_to_anchor=(0., 1.06, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.xticks(rotation=90)
    plt.show()
    st.title("Number of different Alerts")
    st.pyplot(fig)

    # Highest Grossing Alerts
    alert_slice_df = alert_total_df.groupby(["alertname"])["value"].sum()
    fig, ax = plt.subplots(figsize=(30, 10))
    ax = alert_slice_df.sort_values(ascending=True).plot.barh(x='alertname', y='value', rot=0)
    plt.show()
    st.title("Highest Grossing Alerts")
    st.pyplot(fig)


    # Heat Map
    alert_cluster_scatter = alert_total_df.groupby(["cluster","alertname"])["value"].sum()
    alert_cluster_scatter=alert_cluster_scatter.unstack(level=0)
    fig, ax = plt.subplots(figsize=(50, 20))
    ax=sns.heatmap(alert_cluster_scatter, cmap='coolwarm', robust=True)
    ax.set_xticks=(len(alert_total_df["cluster"].unique()))
    ax.set_title('Heatmap of clusters and Alerts')
    st.title("Heatmap of clusters and Alerts")
    st.write(fig)

    #alert_cluster_df = alert_total_df.groupby(["cluster","timestamp"])["value"].sum()
    #alert_cluster_df=alert_cluster_df.unstack(level=0)
    #st.title("Number of Alerts by Cluster")
    #Line Chart
    #st.line_chart(alert_cluster_df)

