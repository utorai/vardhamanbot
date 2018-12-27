import random
from japronto import Application
from botbuilder.schema import Activity, ActivityTypes
from botframework.connector import ConnectorClient
from botframework.connector.auth import MicrosoftAppCredentials, JwtTokenValidation, SimpleCredentialProvider

bot = None

class Bot:
    def __init__(self, app_id, app_password):
        self.id = app_id
        self.password = app_password
        self.credentials = MicrosoftAppCredentials(self.id, self.password)
        self.initial_activity_handler = None
        self.message_activity_handler = None
    
    def create_reply_activity(self, request_activity, activity_type, text = None, attachment = None):
        activity = Activity(type=activity_type, channel_id=request_activity.channel_id, conversation=request_activity.conversation, recipient=request_activity.from_property, from_property=request_activity.recipient, service_url=request_activity.service_url)
        if text:
            activity.text = text
        if attachment:
            activity.attachments = [attachment]
        return activity
    
    def send_typing_activity(self, activity):
        reply = self.create_reply_activity(activity, ActivityTypes.typing)
        connector = ConnectorClient(self.credentials, base_url=reply.service_url)
        return connector.conversations.send_to_conversation(reply.conversation.id, reply)
    
    def send_text_activity(self, activity, text):
        reply = self.create_reply_activity(activity, ActivityTypes.message, text)
        connector = ConnectorClient(self.credentials, base_url=reply.service_url)
        return connector.conversations.send_to_conversation(reply.conversation.id, reply)
    
    def send_rich_activity(self, activity, text, attachment):
        reply = self.create_reply_activity(activity, ActivityTypes.message, text, attachment)
        connector = ConnectorClient(self.credentials, base_url=reply.service_url)
        return connector.conversations.send_to_conversation(reply.conversation.id, reply)
    
    def handle_initial_activity(self, activity):
        if activity.members_added[0].id != activity.recipient.id:
            self.initial_activity_handler(activity)
    
    def handle_message_activity(self, activity):
        self.message_activity_handler(activity)
    
    async def authenticate(self, request, activity):
        credential_provider = SimpleCredentialProvider(self.id, self.password)
        try:
            await JwtTokenValidation.authenticate_request(activity, request.headers.get("Authorization"), credential_provider)
            return True
        except Exception:
            return False
    
    def start(self, action):
        self.initial_activity_handler = action
    
    def replies(self, action):
        self.message_activity_handler = action

async def handle_all_activity(request):
    global bot
    data = request.json
    activity = Activity.deserialize(data)
    if not await bot.authenticate(request, activity):
        return request.Response(code=500)
    if activity.type == ActivityTypes.conversation_update.value:
        bot.handle_initial_activity(activity)
        return request.Response(code=202)
    elif activity.type == ActivityTypes.message.value:
        bot.handle_message_activity(activity)
        return request.Response(code=200)
    else:
        return request.Response(code=404)
    
def start(current_bot):
    global bot
    bot = current_bot
    server = Application()
    server.router.add_route('/', handle_all_activity)
    server.run(debug=True)