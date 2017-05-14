import boto3
import json


def lambda_handler(event, context):
    order_id = event['order_id']
    table = boto3.resource('dynamodb').Table('Orders')
    response = table.get_item(Key={"order_id": order_id})

    if 'Item' in response:
        item_response = response['Item']
        item_response['order_status'] = 'processing'
        return item_response

    else:
        return 'Order not found !'
