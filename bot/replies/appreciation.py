import random

def reply(activity, bot, data):
    responses = [
        "Aww! Thank you so much.", 
        "But, really all this appreciation goes to my creators.",
        "I'm touched",
        "Thanks a million!",
        "Thanks a bunch!",
        "That’s very kind of you. Thank you.",
        "I appreciate your feedback",
        "Thanks"
    ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)