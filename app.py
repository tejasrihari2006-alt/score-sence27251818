import streamlit as st
import joblib
import numpy as np
import time

st.set_page_config(page_title="Score-sense", layout="wide")

# 🌈 Animated Gradient Background + Glass Effect
st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #ff6ec4, #7873f5, #42e695, #f9ca24);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.title {
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:white;
}

.glass {
    background: rgba(255,255,255,0.15);
    padding:40px;
    border-radius:20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 32px 0 rgba(0,0,0,0.37);
}

label {color:white !important; font-size:18px !important;}

.stButton>button {
    background: linear-gradient(45deg,#ff416c,#ff4b2b);
    color:white;
    font-size:20px;
    padding:12px 30px;
    border-radius:15px;
    border:none;
}
</style>
""", unsafe_allow_html=True)

model = joblib.load("model.pkl")

st.markdown("<div class='title'>🎓 Score-Sense</div>", unsafe_allow_html=True)
st.write("")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    sleep = st.number_input("😴 Sleep Hours", 0, 12)
    social = st.number_input("📱 Social Media Hours", 0, 12)
    study = st.number_input("📚 Study Hours", 0, 12)
    attendance = st.number_input("🏫 Attendance Percentage", 0, 100)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.write("### 📊 Prediction Result")
    
    if st.button("🚀 Predict GPA"):
        data = np.array([[sleep, social, study, attendance]])

        with st.spinner("Analyzing Performance..."):
            time.sleep(2)
            result = model.predict(data)[0]

        # GPA Color Indicator
        if result >= 8:
            color = "🟢 Excellent"
        elif result >= 6:
            color = "🟡 Average"
        else:
            color = "🔴 Needs Improvement"

        st.success(f"🎯 Predicted GPA: {result:.2f}")
        st.write(f"Performance Level: {color}")

        # Progress Bar Animation
        progress = st.progress(0)
        for i in range(int(result * 10)):
            time.sleep(0.02)
            progress.progress(i)


    st.markdown("</div>", unsafe_allow_html=True)

