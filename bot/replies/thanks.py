import random

async def reply(activity, bot, data):
    responses = [
        "I'm glad I'm helpful!", 
        "You're welcome!"
    ]
    response = random.choice(responses)
    await bot.send_text_activity(activity, response)