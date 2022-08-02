from flask import Flask
from flask_cors import CORS, cross_origin
from requests import request
import chatbot
from data import chatBotData

app = Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/getanswer/<name>", methods=['GET'])
def hello_world(name):
    # print(name)
    message = name
    intents = chatbot.pred_class(message, chatbot.words, chatbot.classes)
    result = chatbot.get_response(intents, chatBotData)
    return result
