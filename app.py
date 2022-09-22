from flask import Flask, request
from flask import request
from flask_cors import CORS
from flask_mail import Mail, Message
from flask import Response
import chatbot
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/getanswer/<question>", methods=['GET'])
def getAnswer(question):
        message = question.lower()
        intents = chatbot.pred_class(message, chatbot.words, chatbot.classes)
        result = chatbot.get_response(intents, chatbot.chatBotData)
        return result

# dotenv secured data
USERNAME = os.environ.get("EMAIL")
SERVER = os.environ.get("SERVER")
PASSWORD = os.environ.get("PASSWORD")

app.config['MAIL_SERVER'] = SERVER
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = USERNAME

app.config['MAIL_PASSWORD'] = PASSWORD
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/sendmail", methods=['GET', 'POST'])
def sendmail():
        try: 
                if request.method == 'POST':
                        fullname = request.args['fullname']
                        sender = request.args['sender']
                        recipient = request.args['recipient']
                        message = request.args['message']
                        title = request.args['title']
                        subject = fullname +  " | " + title
                        
                        msg = Message(subject,sender=sender, recipients = [recipient])
                        msg.body = message
                        mail.send(msg)
                return 'Message sent!'
        except Exception as e:
                return Response("Fail! Try again later.", status=404, mimetype='application/json')

if(__name__ == '__main__'):
        app.run(debug=False, use_reloader=False)