# 📦 Import libraries
import streamlit as st
import pandas as pd
import joblib

# 🛠 Load the trained model
model = joblib.load('Fraud_detection_pipeline.pkl')

# 🎨 Set Page Configuration
st.set_page_config(page_title="Fraud Detection App", page_icon="💳", layout="centered")

# 🎨 Set Background Image using custom CSS
def set_bg_image(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({url});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Background image URL (you can change to any)
bg_url = 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80'
set_bg_image(bg_url)

# ✨ Sidebar Information
st.sidebar.title("🧾 About App")
st.sidebar.info(
    """
    Welcome to the Fraud Detection Prediction App!

    🔍 This tool predicts whether a financial transaction is fraudulent based on user input.

    🚀 Built with:
    - Python 🐍
    - Machine Learning 🤖
    - Streamlit 🎨

    **Developer:** Shashidhar Hullavarad
    """
)
st.sidebar.markdown("---")
st.sidebar.write("🔗 Connect with me on [GitHub](https://github.com/ShashidharHullavarad)")

# 🖥️ Main App
st.title("💳 Fraud Detection Prediction App")
st.markdown("Please enter the transaction details below and click **Predict**.")

st.divider()

# 📥 User Inputs
transaction_type = st.selectbox("Transaction Type", ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEPOSIT'])

amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.00)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.00)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

st.divider()

# ✨ Predict Button with custom style
predict_button = st.button("🚀 Predict Transaction")

if predict_button:
    with st.spinner('🔎 Predicting... Please wait...'):
        # Prepare the input data
        input_data = pd.DataFrame([{
            "type": transaction_type,
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest,
        }])

        # Make prediction
        prediction = model.predict(input_data)[0]

    # 🎯 Show Prediction Result
    if prediction == 1:
        st.error('⚠️ This transaction is potentially **fraudulent**! Please verify carefully.')
    else:
        st.success('✅ This transaction looks **safe** and **legitimate**.')
        st.balloons()  # 🎈 Show balloons if safe
