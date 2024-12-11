"""
Developer Name: Sai Sundeep Rayidi
Creation Date: 11/20/2024
Last Update Date: 11/30/2024

"""


import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
from collections import Counter

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


# Helper Function to preprocess the job description

def clean_job_descriptions(text):
    text = re.sub(r'\*+', '', text)

    # email addresses, phone numbers, URLs, and lowercasing
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'\d{10}', '', text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = text.lower()

    # Remove numbers and punctuation
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'(\bresponsibilities\b|\bexperience\b|\bskills\b)', r'. \1', text)  # Add periods after sections

    # Tokenization, stopword removal, and lemmatization
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    # tokens = [lemmatizer.lemmatize(word) for word in tokens]
    cleaned_text = ' '.join(tokens)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text


def further_preprocessing(text):
    # Normalize non-standard characters
    text = text.replace('’', "'")
    text = text.replace('–', '-')

    # Expand contractions (e.g., "looking for" -> "looking for")
    text = re.sub(r"\b(s|ll|ve|d|re|ve|m)\b", r"\1", text)

    # Add missing punctuation (simplified approach: insert period after sections like responsibilities, qualifications)
    text = re.sub(r'(responsibilities|qualifications|requirements|experience)', r'. \1', text)

    # Split long phrases (example: skills --> "Skills" + bullet points)
    text = re.sub(r'\n|\r', ' ', text)  # Remove unwanted newlines or breaks
    text = re.sub(r'(\w)([A-Z])', r'\1. \2', text)  # Insert period between lowercase and capital letters

    # Normalize spaces (remove extra spaces between words)
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def preprocess_job_descriptions(descriptions):
    level1_preprocessing = descriptions.apply(clean_job_descriptions)
    cleaned_job_descriptions = level1_preprocessing.apply(further_preprocessing)
    return cleaned_job_descriptions