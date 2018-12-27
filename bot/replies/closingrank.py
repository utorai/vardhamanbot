def reply(activity, bot, data):
    entities = data.get_entities()
    department  = str(entities['department']).lower()
    reply  = f"The Closing rank for General Category of {department} is "
    if department == 'mechanical':
        reply += "18275"
    elif department == 'cse':
        reply += "6684"
    elif department == 'ece':
        reply += "9874"
    elif department == 'eee':
        reply += "11365"
    elif department == 'it':
        reply += "10635"
    elif department == 'civil':
        reply += "12835"
    bot.send_text_activity(activity, reply)