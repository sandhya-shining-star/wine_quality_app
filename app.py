import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Wine Quality Predictor",
    page_icon="🍷",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #1a0a0a; }
    h1 { color: #c0392b; }
    .stButton > button {
        background-color: #c0392b;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 2rem;
        font-size: 1rem;
        font-weight: 600;
    }
    .stButton > button:hover { background-color: #922b21; }
    .result-box {
        padding: 1.2rem 1.5rem;
        border-radius: 10px;
        font-size: 1.3rem;
        font-weight: bold;
        text-align: center;
        margin-top: 1rem;
    }
    .good  { background: #1e8449; color: white; }
    .bad   { background: #922b21; color: white; }
</style>
""", unsafe_allow_html=True)

# ── Load & train model (cached) ───────────────────────────────────────────────
@st.cache_resource
def load_model():
    url = "https://raw.githubusercontent.com/dsrscientist/dataset1/master/winequality-red.csv"
    try:
        df = pd.read_csv(url)
    except Exception:
        st.error("Could not load the dataset. Please check your internet connection.")
        st.stop()

    X = df.drop("quality", axis=1)
    Y = df["quality"].apply(lambda v: 1 if v >= 7 else 0)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=3
    )
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, Y_train)
    return clf, X.columns.tolist()

model, feature_names = load_model()

# ── UI ────────────────────────────────────────────────────────────────────────
st.title("🍷 Wine Quality Predictor")
st.markdown(
    "Adjust the chemical properties below and click **Predict** "
    "to find out whether the wine is **Good** (quality ≥ 7) or **Not Good**."
)
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    fixed_acidity        = st.number_input("Fixed Acidity",        min_value=4.0,  max_value=16.0, value=7.5,  step=0.1)
    volatile_acidity     = st.number_input("Volatile Acidity",     min_value=0.1,  max_value=1.6,  value=0.5,  step=0.01)
    citric_acid          = st.number_input("Citric Acid",          min_value=0.0,  max_value=1.0,  value=0.36, step=0.01)
    residual_sugar       = st.number_input("Residual Sugar",       min_value=1.0,  max_value=16.0, value=6.1,  step=0.1)

with col2:
    chlorides            = st.number_input("Chlorides",            min_value=0.01, max_value=0.62, value=0.071,step=0.001, format="%.3f")
    free_sulfur_dioxide  = st.number_input("Free Sulfur Dioxide",  min_value=1.0,  max_value=72.0, value=17.0, step=1.0)
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=6.0,  max_value=290.0,value=102.0,step=1.0)

with col3:
    density              = st.number_input("Density",              min_value=0.990,max_value=1.004,value=0.9978,step=0.0001,format="%.4f")
    pH                   = st.number_input("pH",                   min_value=2.7,  max_value=4.1,  value=3.35, step=0.01)
    sulphates            = st.number_input("Sulphates",            min_value=0.3,  max_value=2.0,  value=0.8,  step=0.01)
    alcohol              = st.number_input("Alcohol (%)",          min_value=8.0,  max_value=15.0, value=10.5, step=0.1)

st.divider()

if st.button("🔍 Predict Quality"):
    input_data = np.array([[
        fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
        chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
        density, pH, sulphates, alcohol
    ]])

    prediction = model.predict(input_data)[0]
    proba      = model.predict_proba(input_data)[0]
    confidence = round(proba[prediction] * 100, 1)

    if prediction == 1:
        st.markdown(
            f'<div class="result-box good">✅ Good Quality Wine &nbsp;|&nbsp; Confidence: {confidence}%</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="result-box bad">❌ Not Good Quality Wine &nbsp;|&nbsp; Confidence: {confidence}%</div>',
            unsafe_allow_html=True,
        )

st.caption("Model: Random Forest Classifier · Dataset: Red Wine Quality (UCI)")