
# Naive Bayes Classifier for Weather Prediction

import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

# Step 1: Create Dataset
data = {
    "Outlook": [
        "Sunny", "Sunny", "Overcast", "Rainy",
        "Rainy", "Rainy", "Overcast", "Sunny",
        "Sunny", "Rainy", "Sunny", "Overcast",
        "Overcast", "Rainy"
    ],

    "Temperature": [
        "Hot", "Hot", "Hot", "Mild",
        "Cool", "Cool", "Cool", "Mild",
        "Cool", "Mild", "Mild", "Mild",
        "Hot", "Mild"
    ],

    "Humidity": [
        "High", "High", "High", "High",
        "Normal", "Normal", "Normal", "High",
        "Normal", "Normal", "Normal", "High",
        "Normal", "High"
    ],

    "Wind": [
        "Weak", "Strong", "Weak", "Weak",
        "Weak", "Strong", "Strong", "Weak",
        "Weak", "Weak", "Strong", "Strong",
        "Weak", "Strong"
    ],

    "Play": [
        "No", "No", "Yes", "Yes",
        "Yes", "No", "Yes", "No",
        "Yes", "Yes", "Yes", "Yes",
        "Yes", "No"
    ]
}

df = pd.DataFrame(data)

# Step 2: Separate Features and Target
X = df.drop("Play", axis=1)
y = df["Play"]

# Step 3: Encode Categorical Data
encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X)

# Step 4: Train Naive Bayes Model
model = CategoricalNB()
model.fit(X_encoded, y)

# Step 5: Test New Weather Condition
test_data = pd.DataFrame({
    "Outlook": ["Sunny"],
    "Temperature": ["Cool"],
    "Humidity": ["Normal"],
    "Wind": ["Weak"]
})

test_encoded = encoder.transform(test_data)

# Step 6: Perform Prediction
prediction = model.predict(test_encoded)

# Step 7: Calculate Probabilities
probabilities = model.predict_proba(test_encoded)

print("Weather Prediction")
print("------------------")

print("Outlook: Sunny")
print("Temperature: Cool")
print("Humidity: Normal")
print("Wind: Weak")

print("\nPrediction:", prediction[0])

print("\nPrediction Probabilities:")

for label, probability in zip(
    model.classes_, probabilities[0]
):
    print(f"Play {label}: {probability * 100:.2f}%")
