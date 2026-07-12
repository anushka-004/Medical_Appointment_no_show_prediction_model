import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Medical Appointment Prediction",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load CSS
# -----------------------------
css_path = Path(__file__).parent / "style.css"

if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Load Model
# -----------------------------
model_path = Path(__file__).parent.parent / "model" / "random_forest_model.pkl"

rf = joblib.load(model_path)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🏥 Medical Dashboard")

st.sidebar.markdown("---")

st.sidebar.success("Model : Random Forest")

st.sidebar.info("Accuracy : 71.06%")

st.sidebar.info("ROC AUC : 0.749")

st.sidebar.info("Cross Validation : 71%")

st.sidebar.markdown("---")

st.sidebar.write("### 👩‍💻 Developer")

st.sidebar.write("Anushka Tiwari")

# -----------------------------
# Header
# -----------------------------
st.markdown(
"""
<div class="header">

<h1>🏥 Medical Appointment No-Show Prediction</h1>

<p>
Predict whether a patient is likely to attend
or miss the medical appointment using
Machine Learning.
</p>

</div>
""",
unsafe_allow_html=True
)
st.markdown("---")
col1, col2 = st.columns(2)
with col1:

    st.subheader("👤 Patient Information")

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=110,
        value=25
    )

    gender = st.selectbox(
        "Gender",
        ["Female","Male","Other"]
    )

    appointment_time = st.number_input(
        "Appointment Time (Hour)",
        min_value=0,
        max_value=23,
        value=10
    )

    appointment_shift = st.selectbox(
        "Appointment Shift",
        ["Morning","Afternoon"]
    )

    appointment_month = st.slider(
        "Appointment Month",
        1,
        12,
        6
    )
with col2:

    st.subheader("❤️ Medical Information")

    hipertension = st.checkbox("Hypertension")

    diabetes = st.checkbox("Diabetes")

    alcoholism = st.checkbox("Alcoholism")

    handcap = st.checkbox("Handicap")

    scholarship = st.checkbox("Scholarship")

    sms = st.checkbox("SMS Received")
st.markdown("---")

st.subheader("🌦 Weather Information")

c1, c2 = st.columns(2)
with c1:

    avg_temp = st.number_input(
        "Average Temperature",
        value=25.0
    )

    avg_rain = st.number_input(
        "Average Rain",
        value=0.0
    )

    rain_before = st.checkbox(
        "Rainy Day Before"
    )

    rain_intensity = st.selectbox(
        "Rain Intensity",
        [
            "no_rain",
            "weak",
            "moderate",
            "heavy"
        ]
    )
with c2:

    max_temp = st.number_input(
        "Maximum Temperature",
        value=30.0
    )

    max_rain = st.number_input(
        "Maximum Rain",
        value=0.0
    )

    storm_before = st.checkbox(
        "Storm Day Before"
    )

    heat = st.selectbox(
        "Heat Intensity",
        [
            "cold",
            "mild",
            "warm",
            "heavy_cold",
            "heavy_warm"
        ]
    )
st.markdown("---")

predict = st.button(
    "🔍 Predict Appointment Status",
    use_container_width=True
)