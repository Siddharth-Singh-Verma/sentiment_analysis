# Sentiment Analysis Web Application

This project is a web application that performs sentiment analysis on text inputs using a machine learning model. The application is built using Python, Flask, HTML, and CSS. The model is trained on a Twitter dataset to classify sentiments as positive, negative, or neutral.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Model](#model)
- [Web Application](#web-application)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The goal of this project is to create a sentiment analysis web application that can identify the sentiment of a given text. The application uses a machine learning model trained on a Twitter dataset and provides a user-friendly interface for sentiment classification.

## Features
- **Sentiment Classification**: Classifies text into positive, negative, or neutral sentiments.
- **Web Interface**: User-friendly web interface built with HTML and CSS.
- **Flask Backend**: Backend powered by Flask to handle model predictions and API requests.
- **Real-time Predictions**: Provides real-time sentiment analysis results.

## Dataset
The model is trained on a Twitter dataset containing labeled tweets with sentiments. The dataset is split into training and testing sets to evaluate the model's performance.

## Model
The sentiment analysis model is built using Scikit-learn and trained on the Twitter dataset. The model uses basic machine learning algorithms and does not rely on advanced neural networks. The final model is saved and loaded for real-time predictions in the web application.

## Web Application
The web application is built using Flask for the backend and HTML/CSS for the frontend. Users can input text, and the application will display the predicted sentiment.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/sentiment-analysis-webapp.git
    cd sentiment-analysis-webapp
    ```

2. **Create a Conda environment**:
    ```sh
    conda create --name sentiment_env python=3.8
    conda activate sentiment_env
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```sh
    python app.py
    ```

5. **Open your browser** and go to `http://127.0.0.1:5000/` to see the application.

## Usage
1. Open the web application in your browser.
2. Enter a text input in the provided text box.
3. Click the "Analyze" button.
4. The application will display the sentiment of the input text.

## Directory Structure
sentiment_analysis/
├── app.py # Flask application
├── model/
│ ├── sentiment_model.py # Model training and prediction code
│ └── init.py # Model initialization
├── templates/
│ └── index.html # HTML template for the web interface
├── static/
│ └── style.css # CSS styling for the web interface
├── requirements.txt # List of required packages
├── README.md # Project readme file

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
