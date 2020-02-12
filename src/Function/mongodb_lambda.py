import json
import os
from pymongo import MongoClient

connection_string = os.environ['MONGODB_CONNECTION_STRING']
client = MongoClient(connection_string)
db = client.conference

def handler(event, context):
    item = json.loads(event['body'])
    print(item)

    result=db.learnings.insert_one(item)

    response_body = { "id": str(result.inserted_id) }

    return {
        'statusCode': 201,
        'body': json.dumps(response_body)
    }
