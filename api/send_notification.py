from fastapi import APIRouter
from db import send_notifications
router = APIRouter()


@router.get("/notify/{notification_id}", tags=["notification"],
             description="sends the notification to emails")
async def send_notification(notification_id: str):
    """
    send the required notifications to the email id provided
    :param notification_id:
    :return:
    """
    try:
        status = await send_notifications.send_notification(notification_id)
        pass
    except Exception as ex:
        return {"message": "Some issue occured while sending the notifs"}

    return status

