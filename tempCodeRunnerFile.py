from flask import Flask, render_template, request, jsonify

from flask_cors import CORS

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

CORS(app)
@app.route('/translate',methods=['POST'])
def translate():
    
    with sr.Microphone() as source2:
        
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        r.adjust_for_ambient_noise(source2, duration=0.2)
        
        #listens for the user's input
        audio2 = r.listen(source2)
        
        # Using google to recognize audio
        Mytext = r.recognize_google(audio2)
        MyText = Mytext.lower()
        print("MyText =", MyText) 
        # print("Did you say ",MyText)
        SpeakText(MyText)
    print(jsonify({'Text':MyText}))
    return jsonify({'Text':MyText})
        


if __name__ == '__main__':
    app.run()
