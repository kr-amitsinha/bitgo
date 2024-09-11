import random

from db import client
from models.notifications import StatusEnum
from bson import ObjectId

coll = client.bitgo.notifications


async def send_notification(notification_id: str):
    """
    This funct will add the notification to the db
    :param notification_id:
    :return:
    """
    notification_id = ObjectId(notification_id)
    await coll.find_one({"_id": notification_id})
    rand = random.randint(1, 1000)
    update_dict = {"status": "failed"}
    if rand % 2 == 0:
        update_dict = {"status": "sent"}
    await coll.update_one({"_id": notification_id}, {"$set": update_dict})
    return update_dict
