from fastapi import APIRouter
from api import create_notification
from api import send_notification
from api import list_notifications

api_router = APIRouter()

api_router.include_router(create_notification.router)
api_router.include_router(send_notification.router)
api_router.include_router(list_notifications.router)

