import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle


model = load_model("lstm_fake_news_model.keras")

# ====== Load Tokenizer ======
with open("news_tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)


MAX_SEQUENCE_LENGTH = 300


st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("📰 Fake News Detector")
st.write("Enter a news headline or article below to check if it's **fake** or **real**.")


user_input = st.text_area("Enter News Text:", height=200)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some news text.")
    else:

        sequence = tokenizer.texts_to_sequences([user_input])
        padded = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH)


        prediction = model.predict(padded)[0][0]


        if prediction >= 0.5:
            st.error("🚨 This news is likely **FAKE**.")
            st.metric(label="Confidence", value=f"{prediction * 100:.2f}%")
        else:
            st.success("✅ This news appears to be **REAL**.")
            st.metric(label="Confidence", value=f"{(1 - prediction) * 100:.2f}%")
