# SMS Spam Classifier
# Author: Sai Charan AK 

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

print("SMS Spam Classifier is running...")

# Load dataset
data = pd.read_csv("spam.csv", encoding="latin-1")

# Keep only required columns
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['message'])

y = data['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Check accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Test prediction
test_message = ["Congratulations! You won a free prize!"]

test_vector = vectorizer.transform(test_message)

prediction = model.predict(test_vector)

print("Test Message:", test_message[0])
print("Prediction:", prediction[0])
