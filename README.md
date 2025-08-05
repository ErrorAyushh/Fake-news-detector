📰 Fake News Detector 🔍
A Deep Learning project to detect whether a news headline is real or fake using an LSTM-based model and a Streamlit web app.

💡 About the Project
With the rise of misinformation across digital platforms, the ability to automatically detect fake news has become increasingly important. This project uses an LSTM (Long Short-Term Memory) neural network model to classify news headlines as either real or fake.

🚀 Features
Built with TensorFlow/Keras and trained using an LSTM architecture.

Simple and intuitive Streamlit interface for real-time predictions.

Preprocessed dataset with cleaned headlines.

Supports live user input via a web UI.

Includes a tokenizer to process new inputs consistently.

🧠 Model Details
Model: LSTM

Accuracy: ~97%

Input: News headline text

Output: "Real" or "Fake"


📊 Dataset Used
Dataset: Fake and real news dataset - Kaggle

It contains:

fake.csv: Headlines and text labeled as fake

true.csv: Headlines and text labeled as real


📝 Requirements
Python ≥ 3.8

TensorFlow

Keras

Numpy

Pandas

Streamlit

Pickle


🤔 Limitations

Predictions depend on the training dataset — newer news might not be evaluated correctly if they differ from training data trends.

The model checks patterns in text only (no fact-checking against real-time sources).




