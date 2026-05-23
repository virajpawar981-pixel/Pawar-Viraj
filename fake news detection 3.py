import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Mock Data Setup (Replace this with a real dataset like Kaggle's Fake News Dataset)
# In real scenarios, read from your CSV files: pd.read_csv('news.csv')
raw_data = {
    'text': [
        "The president signed the new economic relief bill into law today after congressional approval.",
        "Breaking: Aliens have landed in New York City and are demanding pizza from local shops!",
        "Scientists discover a new species of deep-sea jellyfish in the Mariana Trench.",
        "Shocking secret! Drinking this tap water turns your skin completely blue instantly.",
        "The local library will host a community book fair this upcoming Saturday morning.",
        "Leaked documents prove the moon is actually made of ancient green cheese."
    ],
    'label': ['REAL', 'FAKE', 'REAL', 'FAKE', 'REAL', 'FAKE']
}

# Load into a Pandas DataFrame
df = pd.DataFrame(raw_data)

# 2. Extract features and target labels
X = df['text']
y = df['label']

# 3. Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize a TfidfVectorizer
# This converts text into numerical vectors, ignoring common English stop words
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

# Fit and transform the training set, transform the testing set
tfidf_train = tfidf_vectorizer.fit_transform(X_train) 
tfidf_test = tfidf_vectorizer.transform(X_test)

# 5. Initialize and train the PassiveAggressiveClassifier
# This model is highly effective for text classification and online learning
pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train, y_train)

# 6. Evaluate the model on the test data
y_pred = pac.predict(tfidf_test)
score = accuracy_score(y_test, y_pred)
print(f'Accuracy: {round(score*100, 2)}%\n')

# Display detailed metrics
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 7. Function to predict new, unseen news articles
def predict_news(news_text):
    # Transform the input text using the fitted vectorizer
    vectorized_text = tfidf_vectorizer.transform([news_text])
    # Make a prediction
    prediction = pac.predict(vectorized_text)
    return prediction[0]

# --- Test the predictive function ---
sample_headline = "Government passes a bipartisan infrastructure funding package."
result = predict_news(sample_headline)
print(f"Headline: '{sample_headline}'\nPrediction: {result}")
