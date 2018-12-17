import random
from tools.scraper import Scraper
from tinydb import TinyDB, Query

async def reply(activity, bot, data):
    query = Query()
    db = TinyDB('./db.json')
    result = db.search(query.userid == activity.from_property.id)
    scraper = Scraper()
    if len(result) > 0:
        result = result[0]
        rollno = str(result['rollno'])
        wak = str(result['wak'])
        scraper.authenticate(rollno, wak)
        attendance = scraper.get_attendance()
        reply  = "Your attendance is " + str(attendance)
        await bot.send_text_activity(activity, reply)
        if attendance > 95:
            reply = "What are you? A book worm? 😏"
        elif attendance > 85: 
            responses = [
                "Good Going! 😁",
                "Perfectly balanced. As all things should be. 😉"
            ]
            reply = random.choice(responses)
        elif attendance > 80:
            reply = "Making the best of both worlds huh? 😎",
        elif attendance > 75: 
            responses =  [
                "I see you've been bunking a lot of classes lately. 🤨 Be cautious and attend your classes.",
                "Phew, Someone likes to live on the edge."
            ]
            reply = random.choice(responses)
        elif attendance > 65:
            reply = "You should go to your classes if you don't want to burn a hole in your pocket. 😕"
        else:
            reply = "I hope your okay with sitting amongst your juniors next year. 🤭"
        await bot.send_text_activity(activity, reply)
    else:
        await bot.send_text_activity(activity, "Authentication failed. Please message your rollno and web access key again.")
        await bot.send_text_activity(activity, "Enter roll no. and web access key seperated by a single space.")