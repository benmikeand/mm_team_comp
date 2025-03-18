import streamlit as st
import pandas as pd

# Function to filter data
def comp(d, t1, t2):
    return d[(d['TeamName'] == t1) | (d['TeamName'] == t2)][['TeamName', 'seed', 'RankAdjEM',
                                                             'underrated', 'overrated',
                                                             'RankOE', 'RankAdjOE', 'RankDE',
                                                             'RankAdjDE', 'OverallAvgRank', 
                                                             'RankTempo', 'RankAdjTempo']]

# Streamlit UI
st.title("Team Comparison App")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Team selection
    team_names = df["TeamName"].unique()
    t1 = st.selectbox("Select First Team", team_names)
    t2 = st.selectbox("Select Second Team", team_names, index=1)

    # Show results
    if t1 and t2:
        result = comp(df, t1, t2)
        st.write("### Comparison Results")
        st.dataframe(result)
