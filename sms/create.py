from pprint import pprint
from urllib.parse import parse_qs
import boto3
import uuid, os, json

dynamodb = boto3.resource('dynamodb')

def create(event, context):
    parsed_body = parse_qs(
        event['body'], 
        encoding='euc-kr'
    )

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    item = {
        'id': str(uuid.uuid1()),
        'received_at': parsed_body['rcv_date_list'][0],
        'account_id': parsed_body['id_list'][0],
        'to': parsed_body['mo_number_list'][0],
        'sender': parsed_body['callback_list'][0],
        'message': parsed_body['msg_list'][0]
    }
    
    table.put_item(Item=item)
    
    return {
        "statusCode": 200,
        "body": json.dumps(item, ensure_ascii=False)
    }

