import random

def reply(activity, bot, data):
    responses = [
        "Sure you can, this is my github repository : https://github.com/utorai/vardhamanbot",
        "You are more than welcome to contribute, here's the repo https://github.com/utorai/vardhamanbot",
        "You are actually encouraged to, here's the repo https://github.com/utorai/vardhamanbot, have a look and get started!",
        "https://github.com/utorai/vardhamanbot Looking forward to merging your pull request!",
        "https://github.com/utorai/vardhamanbot Commit Push Pull Repeat!"
    ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)