import random

async def reply(activity, bot, data):
    responses = [
        "I'm glad I'm helpful!", 
        "You're welcome!",
        "I'm glad I could be of assistance",
        "Your're very welcome!",
        "glad to help",
        "It's my pleasure",
        "Sure thing!",
        "I'm touched"
    ]
    response = random.choice(responses)
    await bot.send_text_activity(activity, response)