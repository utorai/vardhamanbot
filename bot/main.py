import tools.server
import tools.nlu
import importlib
import json

try:
    with open('./vardhamanbot/bot/config/app.json') as app_config_file:
        app_config = json.load(app_config_file)
except FileNotFoundError:
    app_config = {}
    app_config["appId"] = ""
    app_config["appPassword"] = ""

bot = tools.server.Bot(app_id = app_config["appId"], app_password = app_config["appPassword"])

@bot.start
async def start(activity):
    module = importlib.import_module("replies.start")
    await module.reply(activity, bot, {})

@bot.replies
async def reply(activity):
    await bot.send_typing_activity(activity)
    engine = tools.nlu.Engine()
    data = engine.parse(activity.text)
    intent = data.get_intent()
    entities = data.get_entities()
    print(intent)
    print(entities)
    try:
        module = importlib.import_module("replies." + intent)
        await module.reply(activity, bot, data)
    except (AttributeError, TypeError):
        module = importlib.import_module("replies.default")
        await module.reply(activity, bot, data)

tools.server.start(bot)