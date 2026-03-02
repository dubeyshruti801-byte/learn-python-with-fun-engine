from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL=  os.getenv("MONGODB_URL")
client= AsyncIOMotorClient(MONGO_URL)
db= client.python_game_db

users_collection = db.users