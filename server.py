"""
This module is a flask app that detects emotion using IBM WATSON NLP.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_page():
    """
    This route handles render index file.
    """

    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    This route handle emotion detection.
    """

    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if not result["dominant_emotion"]:
        return "Invalid text! Please try again!"

    return f"""For the given statement,
    the system response is 'anger':{result['anger']},
    'disgust': {result['disgust']}, 'fear': {result['fear']},
    'joy': {result['joy']} and 'sadness': {result['sadness']}.
    The dominant emotion is {result['dominant_emotion']}."""


if __name__ == "__main__":
    app.run(debug=True)
