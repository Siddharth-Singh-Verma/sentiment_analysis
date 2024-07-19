from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('model/sentiment_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        prediction = model.predict([text])
        return render_template('index.html', prediction=prediction[0], text=text)

if __name__ == '__main__':
    app.run(debug=True)
