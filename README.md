# 🌾 Crop Recommendation System using Machine Learning

This project uses a Random Forest Classifier to recommend the most suitable crop to grow based on soil and environmental conditions like temperature, humidity, rainfall, and pH. It helps farmers and agriculture enthusiasts make informed decisions backed by data science.

## Key Features

- Trained ML model (`RandomForestClassifier`) for crop prediction
- Input features: Temperature, Humidity, pH, and Rainfall
- Simple and clean Streamlit web interface
- Agricultural-themed UI with crop insights

## How It Works

1. Collect input values: Temperature, Humidity, pH, Rainfall
2. Preprocess the data and scale/encode as required
3. Predict the recommended crop using the trained ML model
4. Display the result with additional crop information

## Model Info
Algorithm: Random Forest Classifier
Accuracy: ~99%
Dataset: Crop Recommendation Dataset
Features Used: NPK , temperature, humidity, ph, rainfall
Output: One of 22+ major Indian crops including Bajra, Cotton, Barley, etc.
