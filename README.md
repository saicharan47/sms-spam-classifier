# SMS Spam Classifier using Machine Learning

A machine learning project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Python and Scikit-learn.

---

## Overview

This project demonstrates a basic Natural Language Processing (NLP) and Machine Learning pipeline to detect spam messages automatically.

The model is trained on a labeled dataset of SMS messages and can predict whether a new message is spam or not.

This is one of my first machine learning projects as I build my foundation in Artificial Intelligence and Automation Systems.

---

## Features

* Loads and cleans SMS spam dataset
* Converts text into numerical features using CountVectorizer
* Trains a Machine Learning model using Naive Bayes
* Evaluates model accuracy
* Predicts whether a message is Spam or Ham

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Natural Language Processing (NLP)

---

## How It Works

1. Load dataset containing labeled SMS messages
2. Clean and prepare the data
3. Convert text into numerical format
4. Train a Naive Bayes classification model
5. Test model accuracy
6. Predict new messages

---

## Example

Input:
You won a free lottery! Claim now!

Output:
Spam

---

## Project Structure

spam-email-classifier/

│

├── spam.csv

├── main.py

├── README.md

---

## Future Improvements

* Add web interface using Flask or Streamlit
* Improve model accuracy
* Deploy as a web application
* Integrate into email automation systems

---

## Author

Computer Science student building AI, Machine Learning, and Automation Systems.

---

## License

MIT License
