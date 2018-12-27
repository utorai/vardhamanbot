import random

def reply(activity, bot, data):
    responses = [
        "Hi", 
        "Hi there!", 
        "Hello", 
        "Hey there!"
    ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)