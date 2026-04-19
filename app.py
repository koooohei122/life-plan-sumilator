import streamlit as st
import json
from simulator.core import LifeSimulator
import pandas as pd

st.title("Life Plan Simulator")

uploaded_file = st.file_uploader("Upload profile JSON", type="json")

if uploaded_file:
    profile = json.load(uploaded_file)
else:
    with open("data/sample_profile.json") as f:
        profile = json.load(f)

sim = LifeSimulator(profile)
results = sim.simulate(30)

df = pd.DataFrame(results)

st.line_chart(df.set_index("year")["assets"])
st.dataframe(df)
