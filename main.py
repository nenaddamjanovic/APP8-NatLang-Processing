import streamlit as st
import glob
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("files/*.txt"))

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []

for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

dates = [name.strip(".txt").strip("files/") for name in filepaths]

st.title("Diary tone")
st.header("Positivity")

figure1 = px.line(x=dates, y=positivity)
st.plotly_chart(figure1, theme="streamlit")

st.header("Negativity")

figure2 = px.line(x=dates, y=negativity)
st.plotly_chart(figure2, theme="streamlit")