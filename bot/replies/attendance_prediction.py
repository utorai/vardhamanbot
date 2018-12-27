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
        conducted, attended = scraper.getPeriods()
        percentageifpresent = round(((attended+7)/(conducted + 7) * 100), 2)
        percentageifabsent = round(((attended)/(conducted + 7) * 100), 2)
        response = "Your attendance will be %.2f if present, otherwise %.2f" % (percentageifpresent, percentageifabsent)
        bot.send_text_activity(activity, response)
        if percentageifabsent > 95:
            responses = [
                "Go ahead and take a break, You deserve it. 🤗",
                "Seriously, take a day off. 😒",
                "You've been regular to the college. You've earned a day for yourselves. 👍"
            ]
        elif percentageifabsent > 90:
            responses = [
                "Well, your attendance % will still be quite good. But it's upto you. 😊",
                "You are very much eligible to skip college tomorrow. 😁",
                "You can skip college without any guilt. 😏"
            ]
        elif percentageifabsent > 85:
            responses = [
                "It is probably okay to skip college tomorrow. Exercise some caution though. 🙂",
                "You've been doing great. Try to keep it up... or just stay back for once. 😅",
                "Aaj Jaane Ki Zidd Naa Karo.. 😝"
            ]
        elif percentageifabsent > 80:
            responses = [
                "I'd tell you to go to the class par meri kaun sunta hai? 🙄",
                "If you think you can manage 75%, you are more than welcome to try. 😬",
                "\"Laziness may seem attractive, but work gives satisfaction.\" - Anne Frank 😇" 
            ]
        elif percentageifabsent > 75:
            responses = [
                "I see you like to live dangerously ☠... But give a little thought to it.",
                "You can probably get away with this one. 😈",
                "You've been skipping college way too much but you just might get another day."
            ]
        elif percentageifabsent > 65:
            responses = [
                "Please just get off your butt and go to the class. 😒",
                "I know the bed looks very cozy right now but you should definitely go. 😐",
                "Your laziness is really not worth paying that extra money to the college. 😔"
            ]
        else:
            responses = [
                "Beta tumse naa ho paayega 😐",
                "I'm sorry but you probably can't afford to take even a single day off. 🤐",
                "Uhmm.. No way you can skip college right now. 😑"
            ]
        reply = random.choice(responses)
        bot.send_text_activity(activity, reply)