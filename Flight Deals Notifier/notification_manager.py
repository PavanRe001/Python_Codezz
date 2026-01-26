import os
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()

class NotificationManager:
    """Class to send SMS notifications using Twilio"""
    
    def __init__(self):
        self.client = Client(os.environ['Twilio_API_ID'], os.environ['Twilio_API_KEY'])
        self.twilio_phone = os.environ.get('Twilio_Phone_Number', '+15017250604')
        self.user_phone = os.environ.get('User_Phone_Number', '+15558675309')
    
    def send_notification(self, message_body):
        """Send SMS notification with flight details"""
        message = self.client.messages.create(
            to=self.user_phone,
            from_=self.twilio_phone,
            body=message_body
        )
        print(f"Message sent with status: {message.status}")
        return message.status
