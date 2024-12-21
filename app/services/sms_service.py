from twilio.rest import Client
from app.config.settings import settings

def send_sms(to_number: str, message_body: str):
    """
    Sends SMS using Twilio.
    
    :param to_number: Recipient's phone number
    :param message_body: SMS message content
    :return: Response from Twilio API
    """
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to_number,
            body=message_body
        )
        return {"status": "success", "sid": message.sid}
    except Exception as e:
        return {"status": "error", "message": str(e)}
