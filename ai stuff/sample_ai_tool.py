import streamlit as st
from transformers import pipeline, DistilBertTokenizer, DistilBertForSequenceClassification, AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load pre-trained sentiment analysis model
nlptown = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizerNLP = AutoTokenizer.from_pretrained(nlptown)
model_nlptown = AutoModelForSequenceClassification.from_pretrained(nlptown)
# sentiment_classifier = pipeline("sentiment-analysis", model=model_nlptown, tokenizer=tokenizerNLP)

# Load pre-trained DistilBERT model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
# tokenizing text inputs - The DistilBertTokenizer is responsible for converting text into numerical
tokenizer_sentiment = DistilBertTokenizer.from_pretrained(model_name)
# representations suitable for feeding into the DistilBERT model.
model_sentiment = DistilBertForSequenceClassification.from_pretrained(
    model_name)  # sequence classification


def analyze_text(text=None):
    if text is None:
        return None
    inputs = tokenizer_sentiment(
        text, max_length=256, return_tensors="pt", truncation=False)
    with torch.no_grad():
        outputs = model_sentiment(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    probabilities = torch.softmax(outputs.logits, dim=1)
    confidence = torch.max(probabilities).item()
    return prediction, confidence


def analyze_text_sentiment(text=None):
    if text is None:
        return None
    classifier = pipeline("sentiment-analysis",
                          model=model_sentiment, tokenizer=tokenizer_sentiment)
    result = classifier(text)
    return result


def analyze_text_NLP(text=None):
    if text is None:
        return None
    sentiment_classifier = pipeline(
        "sentiment-analysis", model=model_nlptown, tokenizer=tokenizerNLP)
    result = sentiment_classifier(text)
    return result


def display_result(prediction, confidence):
    st.subheader("Analysis Result:")
    if prediction == 1:
        st.write(
            f"Suspicious data is detected, with confidence: {confidence:.4f}")
    else:
        st.write(
            f"No suspicious pattern is found, with confidence: {confidence:.4f}")


def display_sentiment_result(result):
    st.subheader("Suspicious Analysis Result:")
    st.write(
        f"* {result[0]['label']} with confidence: {result[0]['score']:.4f}")


# Streamlit app
def main():
    st.title("Cybersecurity - Pentest Web Application")
    st.sidebar.title("Suspicious Data Analysis")

    analysis_type = st.sidebar.radio("Select Analysis Type:", ("Finetuned Distilbert LLM-1",
                                                               "Finetuned Distilbert LLM-2",
                                                               "Finetuned NLPTOWN LLM"))

    if analysis_type == "Finetuned Distilbert LLM-1":
        # Analyze Suspicious Data via LLM
        st.subheader(
            "Analyze Suspicious Data via Finetuned Distilbert LLM Tokenizer")
        text_input = st.text_area("Enter your text for analysis:", "")
        file_uploaded = st.file_uploader(
            "Or upload a text file:", type=["txt"])
        if st.button("Analyze"):
            if text_input:
                prediction, confidence = analyze_text(text_input)
                display_result(prediction, confidence)
            elif file_uploaded is not None:
                text = file_uploaded.getvalue().decode("utf-8")
                prediction, confidence = analyze_text(text)
                display_result(prediction, confidence)
            else:
                st.warning(
                    "Please enter text or upload a text file for analysis.")

    elif analysis_type == "Finetuned Distilbert LLM-2":
        # Analyze Suspicious Data via Finetuned LLM
        st.subheader(
            "Analyze Suspicious Data via Finetuned DistilBert LLM Classification")
        text_input = st.text_area("Enter text for analysis :", "")
        file_uploaded = st.file_uploader(
            "Or upload a text file:", type=["txt"])
        if st.button("Test Data"):
            if text_input:
                result = analyze_text_sentiment(text_input)
                display_sentiment_result(result)
            elif file_uploaded is not None:
                text = {}
                text = file_uploaded.getvalue().decode("utf-8")
                result = analyze_text_sentiment(text)
                display_sentiment_result(result)
            else:
                st.warning(
                    "Please enter text or upload a text file for analysis.")

    elif analysis_type == "Finetuned NLPTOWN LLM":
        # Analyze Suspicious Data using NLPTOWN Model
        st.subheader("Analyze Suspicious Data using NLPTOWN Model")
        text_input = st.text_area("Enter text for analysis:", "")
        file_uploaded = st.file_uploader(
            "OR upload a text file:", type=["txt"])
        if st.button("Evaluate"):
            if text_input:
                result = analyze_text_NLP(text_input)
                display_sentiment_result(result)
            elif file_uploaded is not None:
                text = {}
                text = file_uploaded.getvalue().decode("utf-8")
                result = analyze_text_NLP(text)
                display_sentiment_result(result)
            else:
                st.warning(
                    "Please enter text or upload a text file for analysis.")


if __name__ == "__main__":
    main()
