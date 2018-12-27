import random

def reply(activity, bot, data):
    responses = [
        "Bye!", 
        "Goodbye! see you soon",
        "Talk to you soon",
        "Adios!",
        "See ya!",
        "Have a nice day!",
        "Bye! It was nice talking to you"
    ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)