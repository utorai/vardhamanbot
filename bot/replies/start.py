async def reply(activity, bot, data):
    await bot.send_text_activity(activity, "Hi, I am the Vardhaman Bot.")
    await bot.send_text_activity(activity, "For, advanced features, please authenticate.")
    await bot.send_text_activity(activity, "To authenticate, enter your roll no. and web access key seperated by a space.")