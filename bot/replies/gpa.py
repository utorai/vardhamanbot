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
        entities = data.get_entities()
        if 'semester' in entities:
            gpa = scraper.get_gpa(entities['semester'])
            reply = "Your SGPA is " + str(gpa)
        else:
            gpa = scraper.get_cgpa()
            reply = "Your CGPA is " + str(gpa)
        await bot.send_text_activity(activity, reply)
        if gpa > 9.5:
            reply = "Woah! Look at you going all out on your tests! Awesome! 💯"
        elif gpa > 9.0:
            reply = "Are you sure you aren't Einstein? 🧐 Keep up the good work! 👍"
        elif gpa > 8.0:
            reply = "We've got a champ here! You are doing great! 👏"
        elif gpa > 7.0:
            reply = "Hang in there bud! You're on the right track! ✌"
        elif gpa > 6.0:
            reply = "Who needs a good CGPA when you're cool no? 😎 JK, you still need it.. 😅"
        else:
            reply = " It's okay, you don't have to be a topper!  The only one you have to beat is the one you were last semester. Work harder this time! 😉"
        await bot.send_text_activity(activity, reply)
    else:
        await bot.send_text_activity(activity, "Authentication failed. Please message your rollno and web access key again.")
        await bot.send_text_activity(activity, "Enter roll no. and web access key seperated by a single space.")