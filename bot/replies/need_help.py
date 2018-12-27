def reply(activity, bot, data):
    bot.send_text_activity(activity, "I can help you keep track of your attendance, CGPA, GPA, timetable and can provide you information related to our college")
    bot.send_text_activity(activity, "Please enter your roll number and Web Access Key in the form 12881A0175 #ABCD(Mind the space)")
    bot.send_text_activity(activity, "Once you are authenticated you can converse with me the way you usually do with your friends")

