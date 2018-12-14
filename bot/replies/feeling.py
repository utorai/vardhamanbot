import random

async def reply(activity, bot, data):
    responses = [
        "I’m fine as always, thank you. Yourself?", 
        "I'm great!, thanks for asking",
        "I'm good!",
        "Pretty well",
        "I'm alright!",
        "Everything is fine!"
     ]
    response = random.choice(responses)
    await bot.send_text_activity(activity, response)