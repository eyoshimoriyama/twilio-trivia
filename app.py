from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.twiml.voice_response import Play, VoiceResponse
from twilio.rest import Client
from trivia import Trivia
from config import twilio_account_sid, twilio_auth_token, secret_key
from urllib.parse import quote
import os

 
# Account SID and Auth Token
client = Client(twilio_account_sid, twilio_auth_token)
app = Flask(__name__)
app.secret_key = secret_key
app.config.from_object(__name__)


# A route to respond to SMS messages and kick off a phone call.
@app.route('/sms', methods=['POST'])
def inbound_sms():
    response = MessagingResponse()

    # Keep track of session to send either question or answer.
    counter = session.get('counter', 0)
    counter += 1
    session['counter'] = counter
    
    # If it's the first message sent, send a question.
    if counter == 1:
        trivia = Trivia()
        question = trivia.get_question()
        session['correct_letter'] = trivia.correct_letter
        session['correct_answer'] = trivia.correct_answer
        response.message(question)

    # Otherwise check the answer and reset the session.
    else:
        answer = quote(request.form['Body'])
        correct_letter = session['correct_letter']
        correct_answer = session['correct_answer']
        answer_check = Trivia.check_answer(answer, correct_letter, correct_answer)
        response.message(answer_check)
        session.clear()
    return str(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)