import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os

st.set_page_config(
    page_title="AlphaPipeline",
    layout="wide"
)

st.title("🚀 AlphaPipeline")

st.subheader(
    "End-to-End Cloud Data Engineering & Machine Learning Project"
)

# --------------------------------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Historical Data",
        "Technical Indicators",
        "Model Evaluation",
        "Future Prediction",
        "About"
    ]
)

# --------------------------------------------------

if page=="Dashboard":

    st.header("Project Overview")

    df=pd.read_parquet("data/ml/AAPL_ml.parquet")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Trading Days",len(df))
    c2.metric("Highest Price",round(df["Close"].max(),2))
    c3.metric("Lowest Price",round(df["Close"].min(),2))
    c4.metric("Average Volume",f"{int(df['Volume'].mean()):,}")

# --------------------------------------------------

elif page=="Historical Data":

    st.header("Historical Stock Price")

    df=pd.read_parquet("data/ml/AAPL_ml.parquet")

    fig=px.line(
        df,
        y="Close",
        title="Close Price"
    )

    st.plotly_chart(fig,use_container_width=True)

# --------------------------------------------------

elif page=="Technical Indicators":

    st.header("Technical Indicators")

    df=pd.read_parquet("data/ml/AAPL_ml.parquet")

    fig=px.line(
        df,
        y=["Close","MA_5","MA_20","EMA_20","EMA_50"],
        title="Moving Averages"
    )

    st.plotly_chart(fig,use_container_width=True)

    fig=px.line(
        df,
        y="RSI_14",
        title="RSI"
    )

    st.plotly_chart(fig,use_container_width=True)

    fig=px.line(
        df,
        y=["MACD","MACD_Signal"],
        title="MACD"
    )

    st.plotly_chart(fig,use_container_width=True)

# --------------------------------------------------

elif page=="Model Evaluation":

    st.header("Model Evaluation")

    if os.path.exists("reports/training_loss.png"):
        st.image(
            "reports/training_loss.png",
            caption="Training Loss"
        )

    if os.path.exists("reports/actual_vs_predicted_real_price.png"):
        st.image(
            "reports/actual_vs_predicted_real_price.png",
            caption="Actual vs Predicted"
        )

# --------------------------------------------------

elif page=="Future Prediction":

    st.header("Next 30-Day Prediction")

    pred=pd.read_csv(
        "data/predictions/predictions.csv"
    )

    fig=px.line(
        pred,
        x="Day",
        y="Predicted_Close",
        markers=True
    )

    st.plotly_chart(fig,use_container_width=True)

    st.dataframe(pred)

    st.download_button(
        "Download Prediction CSV",
        pred.to_csv(index=False),
        file_name="predictions.csv",
        mime="text/csv"
    )

# --------------------------------------------------

else:

    st.header("About")

    st.markdown("""

### Technologies Used

- Python
- Pandas
- PySpark
- PostgreSQL
- Azure Data Lake Storage Gen2
- Azure Databricks
- Azure Data Factory
- TensorFlow
- Streamlit

### Architecture

Yahoo Finance

↓

Bronze

↓

Silver

↓

Gold

↓

Machine Learning

↓

Prediction Dashboard

""")