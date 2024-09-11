
from db import client

coll = client.bitgo.notifications


async def list_notifications(notification_status: str):
    """
    This funct will list all the notifications with the given status
    :param notification_status:
    :return:
    """
    cursor = coll.find({"status": notification_status}, {"_id": 0})
    return await cursor.to_list(length=None)

