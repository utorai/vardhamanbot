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
        conducted, attended = scraper.getPeriods()
        percentageifpresent = round(((attended+7)/(conducted + 7) * 100), 2)
        percentageifabsent = round(((attended)/(conducted + 7) * 100), 2)
        response = "Your attendance will be %.2f if present, otherwise %.2f" % (percentageifpresent, percentageifabsent)
        await bot.send_text_activity(activity, response)