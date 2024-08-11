from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the CSV data
df = pd.read_csv("spam.csv", encoding='latin1')

# Splitting data into features (emails) and labels (categories)
X = df['v2']  # Assuming 'v2' contains the email text
y = df['v1']  # Assuming 'v1' contains the category (ham/spam)

# Train the model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X, y)

# Define route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for form submission
@app.route('/classify', methods=['POST'])
def classify():
    # Get the email text from the form
    email_text = request.form['email']
    # Classify the email
    prediction = model.predict([email_text])
    # Return the classification result
    return render_template('result.html', prediction=prediction[0])

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
