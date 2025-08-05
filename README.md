📰 Fake News Detector using LSTM (Deep Learning)
Detect fake news with high accuracy using an LSTM-based deep learning model built with TensorFlow/Keras and deployed using Streamlit.


📌 Table of Contents
About

Tech Stack

Model Accuracy

How It Works

Installation

Usage

Project Structure

Screenshots

Contributors

License

 About
Fake news spreads misinformation and causes real-world harm. This project uses LSTM (Long Short-Term Memory) neural networks to accurately classify whether a news article is Fake or Real based on its content. It includes:

A trained LSTM model with 97%+ accuracy

Tokenizer saved and reused for consistent predictions

Clean and simple UI built using Streamlit

Ready to deploy on Streamlit Cloud or locally

 Tech Stack
Python 

TensorFlow / Keras 

Streamlit 

Pandas & NumPy

Sklearn

Pickle (for tokenizer saving/loading)

✅ Model Accuracy
Metric	Value
Training Accuracy	97.5%
Validation Accuracy	97.3%
Loss (Val)	0.0822

Model was trained for 10 epochs using preprocessed news headlines and text content.

🔍 How It Works
The input news text is tokenized using a pre-trained tokenizer (news_tokenizer.pkl).

The text is padded and passed into the LSTM model (lstm_fake_news_model.keras).

The model outputs a prediction (Fake or Real) based on learned patterns.

