"""  
server.py - A Flask application for emotion detection based on user input.  
"""  

from flask import Flask, request, jsonify, render_template  
from EmotionDetection import emotion_detector  

app = Flask(__name__)  

@app.route('/', methods=['GET'])  
def index():  
    """Render the index HTML page."""  
    return render_template('index.html')  

@app.route('/emotionDetector', methods=['POST'])  
def emotion_detector_route():  
    """Process the phrase to detect emotions and return the result.  

    Returns:  
        json: A JSON response containing the emotion analysis  
        or an error message if the input is invalid.  
    """  
    data = request.json  
    phrase = data.get('phrase', '')  


    result = emotion_detector(phrase)  

    if result['dominant_emotion'] is None:  
        return jsonify({"message": "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"}), 400  
    
    return jsonify(result)  # Return the result in JSON format  

if __name__ == '__main__':  
    app.run(debug=True, host='0.0.0.0', port=5000)  # Run the server on localhost:5000