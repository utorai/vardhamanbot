import random

def reply(activity, bot, data):
    responses = [
        "Glad to hear that!",
        "Awesome!",
        "Nice Nice!",
        "Sun kar acha laga!",
        "Fantastic!",
        "Happy to hear that!",
        "Sun kar khushi hui!",
    ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)