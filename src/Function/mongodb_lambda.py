import json
import os
from pymongo import MongoClient

connection_string = os.environ['MONGODB_CONNECTION_STRING']
database = os.environ['DATABASE']
collection = os.environ['COLLECTION']

client = MongoClient(connection_string)
db = client[database]

def handler(event, context):
    item = json.loads(event['body'])
    print(item)

    result=db[collection].insert_one(item)

    response_body = { "id": str(result.inserted_id) }

    return {
        'statusCode': 201,
        'body': json.dumps(response_body)
    }
