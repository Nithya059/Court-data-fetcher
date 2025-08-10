import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv("cleaned_output.csv", encoding='ISO-8859-1')  # safe encoding

st.title("⚖️ Court Case Dashboard")

# Show the full data
st.subheader("📄 All Court Cases Data:")
st.dataframe(df)

# Add filters
attorney_selected = st.selectbox("Filter by Attorney", ["All"] + sorted(df["Attorney"].unique().tolist()))
court_selected = st.selectbox("Filter by Court", ["All"] + sorted(df["Court"].unique().tolist()))

# Apply filters
filtered_df = df.copy()
if attorney_selected != "All":
    filtered_df = filtered_df[filtered_df["Attorney"] == attorney_selected]

if court_selected != "All":
    filtered_df = filtered_df[filtered_df["Court"] == court_selected]

# Show filtered data
st.subheader("🔍 Filtered Results:")
st.dataframe(filtered_df)

# Show stats
st.write("🔢 Total Cases:", len(filtered_df))
st.write("🏛️ Unique Courts:", filtered_df["Court"].nunique())
st.write("👨‍⚖️ Unique Attorneys:", filtered_df["Attorney"].nunique())