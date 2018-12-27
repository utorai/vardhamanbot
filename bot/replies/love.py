import random

def reply(activity, bot, data):
    responses = [
        "Me too, but you don’t see me bragging about it.",
        "How could you not when I'm this awesome?",
        "Who, me? This crazy, slightly neurotic me? Well, you have a weird choice.",
        "Roses are red, violets are blue. Sometimes you suck, but I love you too.",
        "If you love me that much, why don't you order a Biryani for me and then let me decide about the intensity of your love.",
        "Roger that!",
        "Tell me, for which guy/girl are you practicing this now?",
        "You are like a candy bar: Half-sweet and half-nuts!",
        "You better!"
        ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)