import random

def reply(activity, bot, data):
    responses = [
        "Today a name, tomorrow a legend!",
        "Genius, billionaire, playboy, philanthropist.",
        "I am everything you wish you could be",
        "You don't remember who I am? This must be either starting signs of old age or Alzheimer's.",
        "I am the person that would’ve bought you a pizza, but now that you act as if we are strangers I’m free to spend that money on myself instead",
        "I am the Vardhaman Bot"

    ]
    response = random.choice(responses)
    bot.send_text_activity(activity, response)