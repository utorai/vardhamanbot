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
        entities = data.get_entities()
        if 'semester' in entities:
            gpa = scraper.get_gpa(entities['semester'])
            reply = "Your SGPA is " + str(gpa)
        else:
            gpa = scraper.get_cgpa()
            reply = "Your CGPA is " + str(gpa)
        bot.send_text_activity(activity, reply)
        if gpa > 9.5:
            responses = [
                "Woah! Look at you going all out on your tests! Awesome! 💯",
                "Watch out! We've got a badass over here. 😎"
            ]    
        elif gpa > 9.0:
            responses = [
                "Are you sure you aren't Einstein? 🧐 Keep up the good work! 👍",
                "If maintaining your grades up was an art, You'd be the Picasso of it. 😏"
            ]    
        elif gpa > 8.0:
            responses = [
                "We've got a champ here! You are doing great! 👏",
                "Seems like you’ve got what it takes to make it to the top. 😉"
            ]
        elif gpa > 7.0:
            responses = [
                "Hang in there bud! You're on the right track! ✌",
                "You'd probably think it's enough but hey, a little hard work never killed anyone. 😊"
            ]
        elif gpa > 6.0:
            responses = [
                "Who needs a good CGPA when you're cool no? 😎 JK, you still need it.. 😅",
                "You are hanging by a thread here bud. But it's never too late though. 🙂"
            ]
        else:
            responses = [
                "It's okay, you don't have to be a topper!  The only one you have to beat is the one you were last semester. Work harder this time! 😉",
                "Don't get disheartened yet. There's a lot to look forward to, if you make sure you study harder. 😇",
                "\"If at first you don't succeed, then skydiving isn't for you.\" - Steven Wright 😊"
            ]
        reply = random.choice(responses)
        bot.send_text_activity(activity, reply)
    else:
        bot.send_text_activity(activity, "Authentication failed. Please message your rollno and web access key again.")
        bot.send_text_activity(activity, "Enter roll no. and web access key seperated by a single space.")