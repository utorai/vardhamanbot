import random

def reply(activity, bot, data):
    responses = [
        "I’m fine as always, thank you. Yourself?", 
        "I'm great!, thanks for asking. Wbu?",
        "I'm good! and you?",
        "Pretty well, how about you?",
        "I'm alright! what about you?",
        "Theek hoon, Shukriya poochne ke liye. Aap kaise ho?",
        "Everything is fine!, thank you. And you?",
        "I am doing great!,thanks. And you?",
        "I am happy! how are you doing?"
    ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)