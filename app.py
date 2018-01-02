import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '487603589:AAFhOOhsrrYuAZ5G7CUNngu6wb1EYlsxXYI'
WEBHOOK_URL = 'https://f75f0a76.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)

machine = TocMachine(
    states=[
        'user',
        'breakfast','lunch','dinner',
        'noodle','rice', 'below100','100up',
        'rest50', 'rest100','restt50','restt100'
    ],
    transitions=[
{
            'trigger': 'sayhi',
            'source': 'user',
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },


        {
            'trigger': 'time',
            'source': 'user',
            'dest': 'breakfast',
            'conditions': 'is_going_to_breakfast'
        },


        {
            'trigger': 'time',
            'source': 'user',
            'dest': 'lunch',
            'conditions': 'is_going_to_lunch'
        },
        {
            'trigger': 'time',
            'source': 'user',
            'dest': 'dinner',
            'conditions': 'is_going_to_dinner'
        },

        {
            'trigger': 'money1',
            'source': 'breakfast',
            'dest': 'below100',
            'conditions': 'is_going_to_below100'
        },
{
            'trigger': 'money1',
            'source': 'breakfast',
            'dest': '100up',
            'conditions': 'is_going_to_100up'
        },


        {
            'trigger': 'food1',
            'source': 'lunch',
            'dest': 'noodle',
            'conditions': 'is_going_to_noodle'
        },
        {
            'trigger': 'food1',
            'source': 'lunch',
            'dest': 'rice',
            'conditions': 'is_going_to_rice'
        },

{
            'trigger': 'food2',
            'source': 'dinner',
            'dest': 'noodle',
            'conditions': 'is_going_to_noodle'
        },

{
            'trigger': 'food2',
            'source': 'dinner',
            'dest': 'rice',
            'conditions': 'is_going_to_rice'
        },

        {
            'trigger': 'money2',
            'source': 'noodle',
            'dest': 'rest50',
            'conditions': 'is_going_to_rest50'
        },
        {
            'trigger': 'money2',
            'source': 'noodle',
            'dest': 'rest100',
            'conditions': 'is_going_to_rest100'
        },
{
            'trigger': 'money3',
            'source': 'rice',
            'dest': 'restt50',
            'conditions': 'is_going_to_restt50'
        },
{
            'trigger': 'money3',
            'source': 'rice',
            'dest': 'restt100',
            'conditions': 'is_going_to_restt100'
        },


       {
           'trigger': 'go_back1',
            'source': [
                'breakfast',
                'lunch',
                'dinner'
            ],
            'dest': 'user',
            'conditions': 'is_going_back_to_user'
        },
        {
            'trigger': 'go_back2_1',
            'source': [
                'below100',
                '100up'
            ],
            'dest': 'breakfast',
            'conditions': 'is_going_back_to_breakfast'
},
{
            'trigger': 'go_back2_2',
            'source': [
                'noodle',
                'rice'
            ],
            'dest': 'lunch',
            'conditions': 'is_going_back_to_lunch'
},
{
            'trigger': 'go_back2_3',
            'source': [
                'noodle',
                'rice'
            ],
            'dest': 'dinner',
            'conditions': 'is_going_back_to_dinner'
},
{
            'trigger': 'go_back3_1',
            'source': [
                'rest50',
                'rest100'
            ],
            'dest': 'noodle',
            'conditions': 'is_going_back_to_noodle'
},
{
            'trigger': 'go_back3_2',
            'source': [
                'restt50',
                'restt100'
            ],
            'dest': 'rice',
            'conditions': 'is_going_back_to_rice'
},


    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
    ignore_invalid_triggers = True
)

def on_enter_menu1(self, update):
        bot.send_photo(chat_id=chat_id, photo='https://i.imgur.com/qT6skLk.jpg')

def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
    print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.time(update)
    machine.food1(update)
    machine.food2(update)
    machine.money1(update)
    machine.money2(update)
    machine.money3(update)
    machine.sayhi(update)
    machine.go_back1(update)
    machine.go_back2_1(update)
    machine.go_back2_2(update)
    machine.go_back2_3(update)
    machine.go_back3_1(update)
    machine.go_back3_2(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
