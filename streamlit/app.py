import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import joblib
from pathlib import Path
st.set_page_config(
    page_title="Medical Appointment Dashboard",
    page_icon="🏥",
    layout="wide"
)
# -----------------------------
# File Paths
# -----------------------------

css_path = Path(__file__).parent / "style.css"

model_path = Path(__file__).parent.parent / "model" / "random_forest_model.pkl"

forecast_path = Path(__file__).parent.parent / "data" / "arima_forecast.csv"

metrics_path = Path(__file__).parent.parent / "data" / "arima_metrics.csv"

# -----------------------------
# Load Files
# -----------------------------

rf = joblib.load(model_path)

forecast_df = pd.read_csv(forecast_path)

metrics_df = pd.read_csv(metrics_path)
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
if predict:

    input_data = {
        "appointment_time": appointment_time,
        "gender": 0 if gender == "Female" else 1,
        "appointment_shift": 1 if appointment_shift == "Morning" else 0,
        "age": age,

        "under_12_years_old": 1 if age < 12 else 0,
        "over_60_years_old": 1 if age >= 60 else 0,
        "patient_needs_companion": 1 if age < 12 or age >= 60 else 0,

        "average_temp_day": avg_temp,
        "average_rain_day": avg_rain,
        "max_temp_day": max_temp,
        "max_rain_day": max_rain,

        "rainy_day_before": 0,
        "storm_day_before": 0,

        "rain_intensity": 0,
        "heat_intensity": 0,

        "Hipertension": int(hipertension),
        "Diabetes": int(diabetes),
        "Alcoholism": int(alcoholism),
        "Handcap": 0,
        "Scholarship": 0,
        "SMS_received": int(sms),

        "appointment_month": appointment_month,

        "specialty_enf": 0,
        "specialty_occupational therapy": 0,
        "specialty_pedagogo": 0,
        "specialty_physiotherapy": 0,
        "specialty_psychotherapy": 0,
        "specialty_sem especialidade": 1,
        "specialty_speech therapy": 0,

        "disability_intellectual": 0,
        "disability_motor": 0
    }

    input_df = pd.DataFrame([input_data])

    prediction = rf.predict(input_df)[0]

    probability = rf.predict_proba(input_df)[0]

    confidence = max(probability) * 100


# ---------------- RIGHT SIDE ---------------- #

with right:

    

    st.markdown("## 🤖 Prediction Result")

    if predict:

        if prediction == 0:
            st.success("✅ Likely to Attend")
        else:
            st.error("❌ Likely No Show")

        st.metric(
            label="Confidence",
            value=f"{confidence:.1f}%"
        )

    else:

        st.info("Fill the patient details and click **Predict Appointment**.")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-card">
<h2>📈 Appointment Demand Forecast</h2>
</div>
""", unsafe_allow_html=True)

forecast_df["Date"] = pd.to_datetime(forecast_df["Date"])

forecast_col1, forecast_col2 = st.columns([3,1], gap="large")
with forecast_col1:

    st.subheader("📈 Actual vs Forecast")

    fig, ax = plt.subplots(figsize=(12,4))

    ax.plot(
        forecast_df["Date"],
        forecast_df["Actual"],
        linewidth=2,
        label="Actual"
    )

    ax.plot(
        forecast_df["Date"],
        forecast_df["Forecast"],
        linewidth=2,
        linestyle="--",
        label="Forecast"
    )

    ax.set_xlabel("Date")

    ax.set_ylabel("Appointments")

    ax.legend()

    plt.xticks(rotation=45)

    st.pyplot(fig)



with forecast_col2:

    st.subheader("📊 Model Performance")

    mae = metrics_df.loc[
        metrics_df["Metric"] == "MAE",
        "Value"
    ].values[0]

    rmse = metrics_df.loc[
        metrics_df["Metric"] == "RMSE",
        "Value"
    ].values[0]

    st.metric(
        "MAE",
        f"{mae:.2f}"
    )

    st.metric(
        "RMSE",
        f"{rmse:.2f}"
    )

    st.success("✅ ARIMA (1,0,1)")

    st.caption(
        "Forecast generated on the test dataset."
    )
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-card">
<h2>📊 Model Insights</h2>
</div>
""", unsafe_allow_html=True)

insight1, insight2, insight3 = st.columns(3)

with insight1:
    st.info("""
### 🤖 Prediction Model

**Random Forest**

Accuracy : **71.06%**

ROC-AUC : **0.749**
""")

with insight2:
    st.info(f"""
### 📈 Forecast Model

**ARIMA (1,0,1)**

MAE : **{mae:.2f}**

RMSE : **{rmse:.2f}**
""")

with insight3:
    st.info("""
### 📂 Dataset

Records : **109,593**

Features : **31**

Target : **No Show**
""")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-card">
<h2>💡 Recommendation</h2>
</div>
""", unsafe_allow_html=True)

if predict:

    if prediction == 0:

        st.success("""
### ✅ Patient is likely to attend

**Recommendations**

- No reminder required
- Appointment can remain unchanged
- Low no-show risk
""")

    else:

        st.warning("""
### ⚠ High No-Show Risk

**Recommendations**

- Send reminder SMS
- Make confirmation call
- Keep backup patient ready
""")
        
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<hr>

<div style="text-align:center;padding:20px;">

<h4>🏥 Medical Appointment Dashboard</h4>

<p>
Random Forest Classifier • ARIMA Forecasting
</p>

<p>
Developed by <b>Anushka Tiwari</b>
</p>

</div>
""", unsafe_allow_html=True)