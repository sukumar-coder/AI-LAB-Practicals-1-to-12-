
# Mini AI Application: Sentiment Analysis

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Step 1: Create Dataset
data = {
    "Review": [
        "This product is amazing",
        "I love this product",
        "Excellent quality and service",
        "Very happy with the purchase",
        "The product is fantastic",
        "Worst product ever",
        "I hate this product",
        "Very poor quality",
        "Completely disappointed",
        "Waste of money"
    ],

    "Sentiment": [
        "Positive", "Positive", "Positive",
        "Positive", "Positive",
        "Negative", "Negative", "Negative",
        "Negative", "Negative"
    ]
}

df = pd.DataFrame(data)

# Step 2: Separate Features and Labels
X = df["Review"]
y = df["Sentiment"]

# Step 3: Create AI Model
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

# Step 4: Train Model
model.fit(X, y)

print("AI Model Training Completed!")

# Step 5: Test with User Input
print("\nSENTIMENT ANALYSIS APPLICATION")

while True:
    review = input("\nEnter a review (or type exit): ")

    if review.lower() == "exit":
        print("Thank you for using the application!")
        break

    if not review.strip():
        print("Please enter a valid review.")
        continue

    prediction = model.predict([review])
    probabilities = model.predict_proba([review])[0]

    print("\nPredicted Sentiment:", prediction[0])

    for label, probability in zip(
        model.classes_, probabilities
    ):
        print(f"{label}: {probability * 100:.2f}%")
