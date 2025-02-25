''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector", 
            template_folder='EmotionDetection/templates',
            static_folder='EmotionDetection/static')

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Get dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Check if dominant emotion is None, if so display error message
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # If dominant emotion is not None return a formatted string with the emotion label and score
    else:

        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        

        return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)