#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
import requests
app = Flask(__name__)
ACCESS_TOKEN = 'SECRET'
VERIFY_TOKEN = 'SECRET'

import json

class VUSAMIFBOT(Bot):
    pass
    def set_get_started(self, gs_obj):
        request_endpoint = '{0}/me/messenger_profile'.format(self.graph_url)
        response = requests.post(
            request_endpoint,
            params = self.auth_args,
            json = gs_obj
        )
        result = response.json()
        return result

    def set_greetings(self, g_obj):
        request_endpoint = '{0}/me/messenger_profile'.format(self.graph_url)
        response = requests.post(
            request_endpoint,
            params = self.auth_args,
            json = g_obj
        )
        result = response.json()
        return result
    def set_persistent_menu(self, pm_obj):
        request_endpoint = '{0}/me/messenger_profile'.format(self.graph_url)
        response = requests.post(
            request_endpoint,
            params = self.auth_args,
            json = pm_obj
        )
        result = response.json()
        print(result)
        return result

bot = VUSAMIFBOT(ACCESS_TOKEN)

greetings = { 
  "get_started":{
    "payload":"Success"
  }
}

swx = {
    "greeting":[
  {
    "locale":"default",
    "text":"Sveiki, norėdami naudotis VU SA MIF DUK automatiniu atsakikliu pasirinkitę vieną iš žemiau pateiktų temų, kitu atveju užduokite savo klausimą"
  }]
}

menu = {
    "persistent_menu": [
        {
            "locale": "default",
            "composer_input_disabled" : True,
            "call_to_actions": [
                {
                    "type": "postback",
                    "title": "Dariuką duokit",
                    "payload": "CARE_HELP"
                },
                {
                    "type": "postback",
                    "title": "VU SA + LSP",
                    "payload": "VUSA"
                },
                {
                    "type": "postback",
                    "title": "BUS + PD",
                    "payload": "BUS"
                }
            ]
        }
    ]
}


bot.set_get_started(greetings)
bot.set_persistent_menu(menu)
bot.set_greetings(swx)
#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()