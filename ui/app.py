import streamlit as st
import requests

st.title("Semantic Guardian Demo")

age = st.number_input("Age", 0, 120, 25)
education = st.selectbox("Education", ["High School", "Bachelor", "Master", "PhD"])
employment = st.selectbox("Employment Type", ["Full-time", "Part-time", "Unemployed"])

if st.button("Validate"):

    data = {
        "age": age,
        "education": education,
        "employment_type": employment
    }

    response = requests.post(
        "http://localhost:8000/validate",
        json=data
    )

    st.write(response.json())
