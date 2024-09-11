from db import client
from models.notifications import NotificationRequest
import pymongo

coll = client.bitgo.notifications


async def create_notification(data: NotificationRequest):
    """
    This funct will add the notification to the db
    :param data:
    :return:
    """
    response = await coll.insert_one(data.dict())
    return str(response.inserted_id)
