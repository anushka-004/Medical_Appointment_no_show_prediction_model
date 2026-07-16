import streamlit as st

st.set_page_config(
    page_title="Medical Appointment Dashboard",
    page_icon="🏥",
    layout="wide"
)
from pathlib import Path

css_path = Path(__file__).parent / "style.css"

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.markdown("""
<div class="hero">

<div>

<h1>🏥 Medical Appointment Dashboard</h1>

<p>
Predict patient attendance and forecast appointment demand
using <b>Random Forest</b> and <b>ARIMA</b>.
</p>

</div>

<div class="status">

🟢 AI Ready

</div>

</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <div class="icon">👥</div>
        <h2>109,593</h2>
        <p>Total Patients</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="icon">🧠</div>
        <h2>31</h2>
        <p>Features</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="icon">❌</div>
        <h2>20.4%</h2>
        <p>No Show Rate</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <div class="icon">🎯</div>
        <h2>71.06%</h2>
        <p>Model Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="overview">

<h2>📋 Project Overview</h2>

<p>
This dashboard predicts whether a patient is likely to attend or miss a medical
appointment using a <b>Random Forest Classifier</b>. It also forecasts future
appointment demand using the <b>ARIMA Time Series Model</b>.
</p>

<div class="overview-grid">

<div>
<h4>🎯 Objective</h4>
<p>Reduce patient no-shows and improve hospital resource planning.</p>
</div>

<div>
<h4>🤖 Machine Learning</h4>
<p>Random Forest Classifier</p>
</div>

<div>
<h4>📈 Forecasting</h4>
<p>ARIMA (1,0,1)</p>
</div>

<div>
<h4>📊 Dataset</h4>
<p>109,593 Medical Appointments</p>
</div>

</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns([2,1], gap="large")

# ---------------- LEFT SIDE ---------------- #

with left:

    st.markdown("""
    <div class="section-card">
    <h2>🤖 Appointment Prediction</h2>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        age = st.number_input(
            "Age",
            0,
            110,
            25
        )

        gender = st.selectbox(
            "Gender",
            ["Female","Male"]
        )

        appointment_time = st.slider(
            "Appointment Time",
            0,
            23,
            10
        )

        appointment_month = st.selectbox(
            "Appointment Month",
            list(range(1,13))
        )

    with c2:

        appointment_shift = st.selectbox(
            "Appointment Shift",
            ["Morning","Afternoon"]
        )

        hipertension = st.checkbox("Hypertension")

        diabetes = st.checkbox("Diabetes")

        alcoholism = st.checkbox("Alcoholism")

        sms = st.checkbox("SMS Received")

    st.markdown("### 🌦 Weather Information")

    w1, w2 = st.columns(2)

    with w1:

        avg_temp = st.number_input(
            "Average Temperature",
            value=25.0
        )

        avg_rain = st.number_input(
            "Average Rainfall",
            value=0.0
        )

    with w2:

        max_temp = st.number_input(
            "Maximum Temperature",
            value=30.0
        )

        max_rain = st.number_input(
            "Maximum Rainfall",
            value=0.0
        )

    predict = st.button(
        "🔍 Predict Appointment",
        use_container_width=True
    )

# ---------------- RIGHT SIDE ---------------- #

with right:

    st.markdown("""
    <div class="prediction-card">

    <h2>🤖 Prediction Result</h2>

    <br>

    <h3 style="color:#64748B;">
    Waiting for Prediction...
    </h3>

    <p>
    Fill the patient information and click
    <b>Predict Appointment</b>.
    </p>

    </div>
    """, unsafe_allow_html=True)

[
'appointment_time',
'gender',
'appointment_shift',
'age',
'under_12_years_old',
'over_60_years_old',
'patient_needs_companion',
'average_temp_day',
'average_rain_day',
'max_temp_day',
'max_rain_day',
'rainy_day_before',
'storm_day_before',
'rain_intensity',
'heat_intensity',
'Hipertension',
'Diabetes',
'Alcoholism',
'Handcap',
'Scholarship',
'SMS_received',
'appointment_month',
'specialty_enf',
'specialty_occupational therapy',
'specialty_pedagogo',
'specialty_physiotherapy',
'specialty_psychotherapy',
'specialty_sem especialidade',
'specialty_speech therapy',
'disability_intellectual',
'disability_motor'
]