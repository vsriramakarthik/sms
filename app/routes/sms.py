# from fastapi import APIRouter, HTTPException
# from app.services.sms_service import send_sms

# router = APIRouter()

# @router.post("/send-sms/")
# async def send_sms_endpoint(to_number: str, message_body: str):
#     """
#     API Endpoint to send an SMS.

#     :param to_number: Recipient's phone number
#     :param message_body: SMS content
#     :return: Status of the SMS operation
#     """
#     if not to_number or not message_body:
#         raise HTTPException(status_code=400, detail="Invalid input. Both 'to_number' and 'message_body' are required.")

#     response = send_sms(to_number, message_body)
#     if response["status"] == "success":
#         return {"message": "SMS sent successfully", "sid": response["sid"]}
#     else:
#         raise HTTPException(status_code=500, detail=response["message"])
# app/api/sms_routes.py
from fastapi import APIRouter, HTTPException
from app.services.sms_service import send_sms
from app.model.sms_model import SmsRequest  # Import the SmsRequest model

router = APIRouter()

@router.post("/send-sms/")
async def send_sms_endpoint(request: SmsRequest):
    """
    API Endpoint to send an SMS.

    :param request: JSON body containing 'to_number' and 'message_body'
    :return: Status of the SMS operation
    """
    to_number = request.to_number
    message_body = request.message_body

    # Validate inputs, although Pydantic already does this automatically
    if not to_number or not message_body:
        raise HTTPException(status_code=400, detail="Both 'to_number' and 'message_body' are required.")

    # Send SMS using Twilio
    response = send_sms(to_number, message_body)

    # Check if the response from the SMS service is successful
    if response.get("status") == "success":
        return {"message": "SMS sent successfully", "sid": response.get("sid")}
    else:
        raise HTTPException(status_code=500, detail=response.get("message", "Unknown error"))
