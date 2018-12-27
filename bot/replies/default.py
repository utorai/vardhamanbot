import random

def reply(activity, bot, data):
    responses = [
        "Sorry, I could not understand your message.", 
        "Sorry, your enquiry is either beyond my reach or I wasn't clever enough."
    ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)