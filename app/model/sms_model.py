# app/models/sms_model.py
from pydantic import BaseModel

class SmsRequest(BaseModel):
    to_number: str
    message_body: str
