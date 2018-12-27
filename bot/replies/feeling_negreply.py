import random

def reply(activity, bot, data):
    responses = [
        "Sorry to hear that, take help of someone who will make you feel better",
        "I wish you a speedy recovery",
        "Take care, i hope you recover fast",
        "Get some help, I hope you get back to being fine ASAP",
        "That doesn't sound good, I hope you will be doing fine soon"
    ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)