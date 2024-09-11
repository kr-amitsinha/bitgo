from fastapi import APIRouter

from db import list_notifcations as list_notifications_db

router = APIRouter()


@router.get("/notification/{notification_status}", tags=["notification"],
             description="Lists all the notifications")
async def list_notification(notification_status: str):
    """
    Get the notifications from the db
    :param notification_status:
    :return:
    """
    try:
        notifications = await list_notifications_db.list_notifications(notification_status)
    except Exception as ex:
        return {"message": "Some error occurred while getting the data"}

    return {"notifications": notifications}

