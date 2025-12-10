import streamlit as st
import pandas as pd

df = pd.read_csv("top_books_for_dashboard.csv")

st.title("Top 20 Books (Weighted Score)")
st.dataframe(df)

# example filters
tag = st.selectbox("Filtrar por tag:", ["Todos"] + sorted(df["tag_name"].dropna().unique().tolist()))

if tag != "Todos":
    df = df[df["tag_name"] == tag]

st.dataframe(df.head(20))