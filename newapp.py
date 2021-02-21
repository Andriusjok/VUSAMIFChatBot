import os
from flask import Flask, request
from fbmessenger import BaseMessenger
from fbmessenger import quick_replies
from fbmessenger.elements import Text
from fbmessenger.thread_settings import GreetingText, GetStartedButton, MessengerProfile
from fbmessenger import elements
from fbmessenger import templates

ACCESS_TOKEN = "Baisiai slaptas"
VERIFY_TOKEN = "Dar slaptesnis"

class Messenger(BaseMessenger):
    def __init__(self, page_access_token):
        self.page_access_token = page_access_token
        super(Messenger, self).__init__(self.page_access_token)

    def message(self, message):
        response = Text(text= str(message["message"]["text"]))
        action = response.to_dict()
        res = self.send(action)
        app.logger.debug("Response: {}".format(res))

    def delivery(self, message):
        pass

    def read(self, message):
        pass

    def account_linking(self, message):
        pass

    def postback(self, message):
        payload = message["postback"]["payload"]
        print(message["postback"]["payload"])
        if "start" in payload:
            elem = elements.Text("Sveiki, norėdami pasinaudoti VU SA MIF DUK skiltimi, pasirinkite vieną iš žemiau pateiktų temų, kitu atveju užduokite savo klausimą.")
            self.send(elem.to_dict(),"RESPONSE")
            btn1 = elements.Button(button_type = "postback", title="VU SA+LSP+Apeliacijos", payload="VU SA+LSP+Apeliacijos")
            btn2 = elements.Button(button_type = "postback", title="BUS+PD", payload="BUS+PD")
            btn3 = elements.Button(button_type = "postback", title="Studijos+Finansai", payload="Studijos+Finansai")
            btns = templates.ButtonTemplate(
                text = "DUK temos",
                buttons = [btn1, btn2, btn3]
            )
            self.send(btns.to_dict(),"RESPONSE")
        if "VU SA+LSP+Apeliacijos" == payload:
            btn1 = elements.Button(button_type = "postback", title="VU SA", payload="VU SA")
            btn2 = elements.Button(button_type = "postback", title="LSP", payload="LSP")
            btn3 = elements.Button(button_type = "postback", title="Apeliacijos", payload="Apeliacijos")
            btns = templates.ButtonTemplate(
                text = "Potemės",
                buttons = [btn1, btn2, btn3]
            )
            self.send(btns.to_dict(),"RESPONSE")
        if "BUS+PD" == payload:
            btn1 = elements.Button(button_type = "postback", title="BUS", payload="BUS")
            btn2 = elements.Button(button_type = "postback", title="PD", payload="PD")
            btns = templates.ButtonTemplate(
                text = "Potemės",
                buttons = [btn1, btn2]
            )
            self.send(btns.to_dict(),"RESPONSE")
        if "Studijos+Finansai" == payload:
            btn1 = elements.Button(button_type = "postback", title="Studijos", payload="Studijos")
            btn2 = elements.Button(button_type = "postback", title="Finansai", payload="Finansai")
            btns = templates.ButtonTemplate(
                text = "Potemės",
                buttons = [btn1, btn2]
            )
            self.send(btns.to_dict(),"RESPONSE")
        if "Studijos" == payload:
            btn1 = elements.Button(
            button_type = "web_url",
            title="Atsakymai", 
            url="https://docs.google.com/document/d/1e_1jSsdjlfoIYJrIuCZELJX0nv4F5IIp2ar-CMUmn98/edit"
            )
            btns = templates.ButtonTemplate(
                text = "Nuoroda į DUK apie Studijų programų / dalykų keitimą bei gretutines studijas / individualų studijų planą",
                buttons = [btn1]
            )
            print(self.send(btns.to_dict(),"RESPONSE"))
        if "Finansai" == payload:
            btn1 = elements.Button(
            button_type = "web_url",
            title="Atsakymai", 
            url="https://docs.google.com/document/d/1e_1jSsdjlfoIYJrIuCZELJX0nv4F5IIp2ar-CMUmn98/edit"
            )
            btns = templates.ButtonTemplate(
                text = "Nuoroda į DUK apie mokesčius už mokslą bei stipendijas",
                buttons = [btn1]
            )
            print(self.send(btns.to_dict(),"RESPONSE"))
        if "BUS" == payload:
            btn1 = elements.Button(
            button_type = "web_url",
            title="Atsakymai", 
            url="https://docs.google.com/document/d/1e_1jSsdjlfoIYJrIuCZELJX0nv4F5IIp2ar-CMUmn98/edit"
            )
            btns = templates.ButtonTemplate(
                text = "Nuoroda į DUK apie Bendrasias universitetines studijas",
                buttons = [btn1]
            )
            print(self.send(btns.to_dict(),"RESPONSE"))
        if "PD" == payload:
            btn1 = elements.Button(
            button_type = "web_url",
            title="Atsakymai", 
            url="https://docs.google.com/document/d/1e_1jSsdjlfoIYJrIuCZELJX0nv4F5IIp2ar-CMUmn98/edit"
            )
            btns = templates.ButtonTemplate(
                text = "Nuoroda į DUK apie Pasirenkamuosius dalykus",
                buttons = [btn1]
            )
            print(self.send(btns.to_dict(),"RESPONSE"))
        if "VU SA" == payload:
            btn1 = elements.Button(
            button_type = "web_url",
            title="Atsakymai", 
            url="https://docs.google.com/document/d/1e_1jSsdjlfoIYJrIuCZELJX0nv4F5IIp2ar-CMUmn98/edit"
            )
            btns = templates.ButtonTemplate(
                text = "Nuoroda į DUK apie VU SA bei VU SA MIF",
                buttons = [btn1]
            )
            print(self.send(btns.to_dict(),"RESPONSE"))
        if "LSP" == payload:
            btn1 = elements.Button(
            button_type = "web_url",
            title="Atsakymai", 
            url="https://docs.google.com/document/d/1e_1jSsdjlfoIYJrIuCZELJX0nv4F5IIp2ar-CMUmn98/edit"
            )
            btns = templates.ButtonTemplate(
                text = "Nuoroda į DUK apie LSP",
                buttons = [btn1]
            )
            print(self.send(btns.to_dict(),"RESPONSE"))
        if "Apeliacijos" == payload:
            btn1 = elements.Button(
            button_type = "web_url",
            title="Atsakymai", 
            url="https://docs.google.com/document/d/1e_1jSsdjlfoIYJrIuCZELJX0nv4F5IIp2ar-CMUmn98/edit"
            )
            btns = templates.ButtonTemplate(
                text = "Nuoroda į DUK apie Apeliacijas bei skundus",
                buttons = [btn1]
            )
            print(self.send(btns.to_dict(),"RESPONSE"))

    def optin(self, message):
        pass

    def init_bot(self):
        greeting_text = GreetingText("VU SA MIF konsultavimas")
        messenger_profile = MessengerProfile(greetings=[greeting_text])
        messenger.set_messenger_profile(messenger_profile.to_dict())

        get_started = GetStartedButton(payload="start")

        messenger_profile = MessengerProfile(get_started=get_started)
        messenger.set_messenger_profile(messenger_profile.to_dict())


app = Flask(__name__)
app.debug = True
messenger = Messenger(ACCESS_TOKEN)


@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            messenger.init_bot()
            return request.args.get("hub.challenge")
        raise ValueError("FB_VERIFY_TOKEN does not match.")
    elif request.method == "POST":
        messenger.handle(request.get_json(force=True))
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0")