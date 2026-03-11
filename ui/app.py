import streamlit as st
import requests

st.set_page_config(page_title="Semantic Guardian", layout="centered")

st.title("Semantic Guardian")
st.subheader("Real-time survey validation prototype")

age = st.number_input("Age", 0, 120, 25)
education = st.selectbox("Education", ["Primary", "High School", "Bachelor", "Master", "PhD"])
employment = st.selectbox("Employment Type", ["Full-time", "Part-time", "Unemployed"])
job_title = st.text_input("Job Title", "")

if st.button("Validate"):

    data = {
        "age": age,
        "education": education,
        "employment_type": employment,
        "job_title": job_title
    }

try:
    response = requests.post("http://localhost:8000/validate", json=data, timeout=30)

    # st.write("HTTP Status Code:", response.status_code)
    # st.write("Raw Response Text:", response.text)

    result = response.json()

    status = result.get("status", "error")
    confidence = result.get("confidence_score", 0)
    message = result.get("message", "No message returned.")
    suggestion = result.get("suggestion", "")
    source = result.get("source", "unknown")

    if status == "ok":
        data_quality_score = confidence
    elif status == "warning":
        data_quality_score = max(0.05, 1 - confidence)
    else:
        data_quality_score = 0.0

    confidence_percent = round(confidence * 100, 1)
    data_quality_percent = round(data_quality_score * 100, 1)

    col1, col2 = st.columns(2)
    col1.metric("AI Confidence of the Data Quality Score", f"{confidence_percent}%")
    col2.metric("Data Quality Score", f"{data_quality_percent}%")



    if status == "ok":
        st.success(message)
    elif status == "warning":
        st.warning(message)
    else:
        st.error(message)

    st.write(f"**Suggestion:** {suggestion}")
    st.write(f"**Validation Source:** {source}")

except Exception as e:
    st.error(f"Could not connect to API: {str(e)}")