from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    def is_going_to_user(self,update):
        text = update.message.text
        return text.lower() == 'hello'

    def is_going_to_breakfast(self, update):
        text = update.message.text
        return text.lower() == 'breakfast'

    def is_going_to_lunch(self, update):
        text = update.message.text
        return text.lower() == 'lunch'

    def is_going_to_dinner(self, update):
        text = update.message.text
        return text.lower() == 'dinner'

    def is_going_to_below100(self, update):
        text = update.message.text
        return text.lower() == 'a'

    def is_going_to_100up(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_noodle(self, update):
        text = update.message.text
        return text.lower() == 'noodle'

    def is_going_to_rice(self, update):
        text = update.message.text
        return text.lower() == 'rice'

    def is_going_to_rest50(self, update):
        text = update.message.text
        return text.lower() == '1'

    def is_going_to_rest100(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_restt50(self, update):
        text = update.message.text
        return text.lower() == '1'

    def is_going_to_restt100(self, update):
        text = update.message.text
        return text.lower() == '2'

    def is_going_back_to_user(self, update):
        text = update.message.text
        return text.lower() == 'back to user'

    def is_going_back_to_breakfast(self, update):
        text = update.message.text
        return text.lower() == 'back to breakfast'

    def is_going_back_to_lunch(self, update):
        text = update.message.text
        return text.lower() == 'back to lunch'

    def is_going_back_to_dinner(self, update):
        text = update.message.text
        return text.lower() == 'back to dinner'

    def is_going_back_to_noodle(self, update):
        text = update.message.text
        return text.lower() == 'back to noodle'

    def is_going_back_to_rice(self, update):
        text = update.message.text
        return text.lower() == 'back to rice'

    def on_enter_user(self, update):
        update.message.reply_text("Nice to meet you! What do you want to eat? Breakfast, lunch or dinner?")

    def on_exit_user(self, update):
        print('Leaving user')


    def on_enter_breakfast(self, update):
        update.message.reply_text("Good morning! How much budget do you have?\n\nEnter a for below NT100\nEnter b for NT100up")


    def on_exit_breakfast(self, update):
        print('Leaving breakfast')
    def on_enter_lunch(self, update):
        update.message.reply_text("Okay! Which one do you prefer? Noodle or rice?")

    def on_exit_lunch(self, update):
        print('Leaving lunch')


    def on_enter_dinner(self, update):
        update.message.reply_text("Okey! Which one do you prefer? Noodle or rice?")

    def on_exit_dinner(self, update):
        print('Leaving dinner')

    def on_enter_below100(self, update):
        update.message.reply_text("I recommend you to eat 元氣屋\nClick here to get location on the google map:\nhttps://goo.gl/qbaMtN")



    def on_exit_below100(self, update):
        print('Leaving below100')

    def on_enter_100up(self, update):
        update.message.reply_text("I recommend you to eat 紅豆早午餐(勝利路)\nClick here to get location on the google map:\nhttps://goo.gl/yDKRMw")

    def on_exit_100up(self, update):
        print('Leaving 100up')

    def on_enter_noodle(self, update):
        update.message.reply_text("How much is your budget?\n\nEnter 1 forNT50-100\nEnter 2 for NT100-200")

    def on_exit_noodle(self, update):
        print('Leaving noodle')


    def on_enter_rice(self, update):
        update.message.reply_text("How much is your budget?\n\nEnter 1 forNT50-100\nEnter 2 for NT100-200")


    def on_exit_rice(self, update):
        print('Leaving rice')


    def on_enter_rest50(self, update):
        update.message.reply_text("I recommend you to eat 甜麵屋\nClick here to get location on the google map:\nhttps://goo.gl/jcrf3e")

    def on_exit_rest50(self, update):
        print('Leaving rest50')

    def on_enter_rest100(self, update):
        update.message.reply_text("I recommend you to eat 那一家義大利麵\nClick here to get location on the google map:\nhttps://goo.gl/6ZtMZx")

    def on_exit_rest100(self, update):
        print('Leaving rest100')

    def on_enter_restt50(self, update):
        update.message.reply_text("I recommend you to eat 經典咖哩\nClick here to get location on the google map:\nhttps://goo.gl/nchiYF")

    def on_exit_restt50(self, update):
        print('Leaving restt50')

    def on_enter_restt100(self, update):
        update.message.reply_text("I recommend you to eat 唐家泡菜館\nClick here to get location on the google map:\nhttps://goo.gl/fWPvUSn")

    def on_exit_restt100(self, update):
        print('Leaving restt100')
