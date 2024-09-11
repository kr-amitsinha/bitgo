import asyncio

import pymongo
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
client.get_io_loop = asyncio.get_running_loop

