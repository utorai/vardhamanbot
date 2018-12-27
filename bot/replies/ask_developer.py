import random

def reply(activity, bot, data):
    responses = [
        "I am the brainchild of Utor AI, you can find more about the team who developed me on www.utorai.com", 
        "I was developed by Utor AI you can find more about the team on www.utorai.com"
    ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)