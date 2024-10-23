"""
Database interaction module
"""


from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME, CONVERSATIONS_COLLECTION
from datetime import datetime

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

def store_conversation(user_input, bot_response):
    conversation = {
        "user_input": user_input,
        "bot_response": bot_response,
        "timestamp": datetime.now()
    }
    db[CONVERSATIONS_COLLECTION].insert_one(conversation)

def get_conversations():
    return list(db[CONVERSATIONS_COLLECTION].find())