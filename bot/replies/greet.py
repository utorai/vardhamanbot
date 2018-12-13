import random

async def reply(activity, bot, data):
    responses = [
        "Hi", 
        "Hi there!", 
        "Hello", 
        "Hey there!"
    ]
    response = random.choice(responses)
    await bot.send_text_activity(activity, response)