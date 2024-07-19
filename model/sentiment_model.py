import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load the training data
train_df = pd.read_csv('/dataset/train.csv', encoding='latin1')
test_df = pd.read_csv('/dataset/test.csv', encoding='latin1')

# Drop rows with NaN values
train_df.dropna(subset=['text', 'sentiment'], inplace=True)
test_df.dropna(subset=['text', 'sentiment'], inplace=True)

# Split the data
X_train = train_df['text']
y_train = train_df['sentiment']
X_test = test_df['text']
y_test = test_df['sentiment']

# Create a pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the model
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, '/content/drive/MyDrive/model/sentiment_model.pkl')
