from fastapi import APIRouter
from logging import log
from db import create_notification as create_notification_db
from models.notifications import NotificationRequest

router = APIRouter()


@router.post("/notification", tags=["notification"],
             description="Creates the notification and returns the notification id")
async def create_notification(data: NotificationRequest):
    """
    Will add the data to the db
    :param data:
    :return:
    """
    try:
        notification_id = await create_notification_db.create_notification(data)
    except Exception as ex:
        return {"message": "Some issue occurred while creating the notifs"}

    return {"notification_id": notification_id}

