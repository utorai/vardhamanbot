import tools.server
import tools.nlu
import json
import replies

try:
    with open('./vardhamanbot/bot/config/app.json') as app_config_file:
        app_config = json.load(app_config_file)
except FileNotFoundError:
    app_config = {}
    app_config["appId"] = ""
    app_config["appPassword"] = ""

bot = tools.server.Bot(app_id = app_config["appId"], app_password = app_config["appPassword"])
engine = tools.nlu.Engine()

@bot.start
async def start(activity):
    await replies.start.reply(activity, bot, {})

@bot.replies
async def reply(activity):
    await bot.send_typing_activity(activity)
    data = engine.parse(activity.text)
    intent = data.get_intent()
    entities = data.get_entities()
    print(intent)
    print(entities)
    try:
        intent_handler = getattr(replies, intent)
        await intent_handler.reply(activity, bot, data)
    except (AttributeError, TypeError):
        await replies.default.reply(activity, bot, data)

tools.server.start(bot)