import random

def reply(activity, bot, data):
    responses = [
        "Sure you can, this is my github repository : https://github.com/utorai/vardhamanbot",
        "There you go https://github.com/utorai/vardhamanbot",
        "https://github.com/utorai/vardhamanbot Feel free to explore it",
        "Wish granted ! https://github.com/utorai/vardhamanbot ",
        "Here you go https://github.com/utorai/vardhamanbot "
    ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)