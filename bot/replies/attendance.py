import random
from tools.scraper import Scraper
from tinydb import TinyDB, Query

def reply(activity, bot, data):
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
        reply  = "Your attendance % is " + str(attendance)
        bot.send_text_activity(activity, reply)
        if attendance == 100:
            responses = [
                "Are you insane?! 😮 Take a break dude!",
                "Someone needs to take a day off. 😒"
            ]
        elif attendance > 95:
            responses = [
                "Your parents must be so proud of you. 🤗",
                "You do love your college a bit too much, Don't you think? 🤔",
                "What are you? A book worm? 😏"
            ]
        elif attendance > 85: 
            responses = [
                "Perfectly balanced. As all things should be. 😉",
                "Good Going! 😁"
            ]
        elif attendance > 80:
            responses = [
                "You're certainly someone who can balance work and life. 👍",
                "Making the best of both worlds huh? 😎"
            ]
        elif attendance > 75: 
            responses =  [
                "Phew! Someone likes to live on the edge. 😳",
                "I see you've been bunking a lot of classes lately. 🤨 Be cautious and attend your classes."
            ]
        elif attendance > 65:
            responses = [ 
                "Keep the condonation money handy mate. 😬",
                "You should go to your classes if you don't want to burn a hole in your pocket. 😕"
            ]
        else:
            responses = [
                "Looks like you've been too lazy for your own good. 😴",
                "I hope your okay with sitting amongst your juniors next year. 🤭"
            ]
        reply = random.choice(responses)
        bot.send_text_activity(activity, reply)
    else:
        bot.send_text_activity(activity, "Authentication failed. Please message your roll no. and web access key again.")
        bot.send_text_activity(activity, "Enter roll no. and web access key seperated by a single space.")