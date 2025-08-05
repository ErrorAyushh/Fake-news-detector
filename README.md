Fake News Detection using LSTM
Overview
This project aims to detect fake news using a Long Short-Term Memory (LSTM) neural network model. Fake news is a growing concern in today's digital age, and being able to automatically identify whether a news article is real or fake can help combat misinformation and promote reliable content online.

The model is trained on a labeled dataset of news articles and uses deep learning (LSTM) for accurate binary classification of text data.


Features
Preprocessing of news articles (cleaning, tokenization, padding)

Binary classification using LSTM neural network

Streamlit UI for real-time fake news detection

Model trained on a labeled dataset of real and fake news

Accuracy of over 97% on validation data

Dataset
The dataset used is the Fake and Real News Dataset from Kaggle. It contains labeled data for fake and real news articles.

You can download it from here.

 Model Performance
Training Accuracy: ~97.5%

Validation Accuracy: ~97.3%

Loss: Decreasing trend, minimal overfitting

Model trained for 10 epochs with appropriate preprocessing and tokenizer saving for inference.



Future Improvements
Incorporate headlines and full-body text for better accuracy.

Use transformers (BERT) for more advanced NLP.

Add feedback and correction system to retrain model continuously.

Deploy the app on the web using platforms like Streamlit Cloud or HuggingFace Spaces.
